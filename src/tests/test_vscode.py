import shutil
import subprocess
from pathlib import Path
from typing import Union

from _pytest.monkeypatch import MonkeyPatch
from buildenv import BuildEnvManager
from buildenv2.extension import BuildEnvInfo, BuildEnvRenderer
from jinja2 import Environment
from nmk.tests.tester import NmkBaseTester
from nmk.utils import is_windows

from nmk_vscode import __version__
from nmk_vscode._buildenv.extension import NmkVsCodeBuildEnvExtension
from nmk_vscode._buildenv.legacy import BuildEnvInit


class TestVSCodePlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def test_version(self):
        self.nmk(self.prepare_project("ref_vscode.yml"), extra_args=["version"])

    def test_settings(self):
        self.nmk(
            self.prepare_project("ref_vscode.yml"),
            extra_args=[
                "vs.settings",
                "--config",
                '{"vscodeSettingsItems": {'
                + '"editor.formatOnSave":false,'
                + '"cSpell.words": ["foo"],'
                + '"files.watcherExclude": {"**/bar/**": true}'
                + "} }",
            ],
        )
        assert (self.test_folder / ".vscode" / "settings.json").is_file()

    def test_launch(self):
        self.prepare_project("sample_launch.json")
        self.nmk(self.prepare_project("ref_vscode_launch.yml"))
        assert (self.test_folder / ".vscode" / "launch.json").is_file()

    def test_tasks(self):
        self.nmk(self.prepare_project("ref_vscode.yml"))
        assert (self.test_folder / ".vscode" / "tasks.json").is_file()

    def test_extensions(self):
        self.nmk(
            self.prepare_project("ref_vscode.yml"),
            extra_args=[
                "vs.extensions",
                "--config",
                '{"vscodeExtensionsNames": ["foo"] }',
            ],
        )
        assert (self.test_folder / ".vscode" / "extensions.json").is_file()

    def test_buildenv_extension_legacy(self, monkeypatch: MonkeyPatch):
        # Prepare extension instance
        fake_venv_bin = self.test_folder / "venv" / ("Scripts" if is_windows() else "bin")
        if fake_venv_bin.is_dir():
            shutil.rmtree(fake_venv_bin)
        activate_script = fake_venv_bin / "activate.d" / "01_vscode.sh"
        activate_script.parent.mkdir(parents=True)
        (activate_script.parent / "00_activate.sh").touch()
        m = BuildEnvManager(self.test_folder, fake_venv_bin)
        ext = BuildEnvInit(m)

        # Check version
        assert ext.get_version() == __version__

        # Check init without code command
        monkeypatch.setattr(shutil, "which", lambda _: None)  # type: ignore
        ext.init(True)
        assert not activate_script.is_file()
        self.check_logs("nmk-vscode: 'code' command not found!")
        monkeypatch.setattr(shutil, "which", lambda _: "code")  # type: ignore

        # Check init with code returning an error
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 1))  # type: ignore
        ext.init(True)
        assert not activate_script.is_file()
        self.check_logs("nmk-vscode: 'code --locate-shell-integration-path bash' command failed!")

        # Check init with code returning an invalid path
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 0, stdout="some/unknown/path/to/unknown/file"))  # type: ignore
        ext.init(True)
        assert not activate_script.is_file()
        self.check_logs("nmk-vscode: bash init script not found: ")

        # Check correct init
        fake_init = self.test_folder / "fake_vs_init.sh"
        fake_init.touch()
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 0, stdout=str(fake_init)))  # type: ignore
        ext.init(True)
        assert activate_script.is_file()

    def test_buildenv_extension(self, monkeypatch: MonkeyPatch):
        # Prepare extension instance
        ext = NmkVsCodeBuildEnvExtension(BuildEnvInfo(self.test_folder, self.test_folder))

        # Fake init
        ext.init(False)

        # Fake renderer
        class FakeRenderer(BuildEnvRenderer):
            def __init__(self):
                self.rendered = False

            def render(self, environment: Environment, template: str, executable: bool = False, keywords: Union[dict[str, str], None] = None):
                self.rendered = True

        fake_renderer = FakeRenderer()

        # Check init without code command
        monkeypatch.setattr(shutil, "which", lambda _: None)  # type: ignore
        ext.generate_activation_scripts(fake_renderer)
        self.check_logs("nmk-vscode: 'code' command not found!")
        monkeypatch.setattr(shutil, "which", lambda _: "code")  # type: ignore
        assert not fake_renderer.rendered

        # Check init with code returning an error
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 1))  # type: ignore
        ext.generate_activation_scripts(fake_renderer)
        assert not fake_renderer.rendered
        self.check_logs("nmk-vscode: 'code --locate-shell-integration-path bash' command failed!")

        # Check init with code returning an invalid path
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 0, stdout="some/unknown/path/to/unknown/file"))  # type: ignore
        ext.generate_activation_scripts(fake_renderer)
        self.check_logs("nmk-vscode: bash init script not found: ")
        assert not fake_renderer.rendered

        # Check correct init
        fake_init = self.test_folder / "fake_vs_init.sh"
        fake_init.touch()
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 0, stdout=str(fake_init)))  # type: ignore
        ext.generate_activation_scripts(fake_renderer)
        assert fake_renderer.rendered
