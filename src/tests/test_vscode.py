from pathlib import Path

from nmk.tests.tester import NmkBaseTester


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
        assert self.test_folder / ".vscode" / "settings.json"
