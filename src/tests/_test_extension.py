import shutil
import subprocess
from pathlib import Path

from _pytest.monkeypatch import MonkeyPatch
from buildenv2.extension import BuildEnvInfo, BuildEnvRenderer
from jinja2 import Environment
from nmk.tests.tester import NmkBaseTester

from nmk_vscode._buildenv.extension import NmkVsCodeBuildEnvExtension


class TestVSCodePlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def test_buildenv_extension(self, monkeypatch: MonkeyPatch):
        # Prepare extension instance
        ext = NmkVsCodeBuildEnvExtension(BuildEnvInfo(self.test_folder, self.test_folder))

        # Fake init
        ext.init(False)

        # Fake renderer
        class FakeRenderer(BuildEnvRenderer):
            def __init__(self):
                self.rendered = False

            def render(self, environment: Environment, template: str, executable: bool = False, keywords: dict[str, str] | None = None):
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
