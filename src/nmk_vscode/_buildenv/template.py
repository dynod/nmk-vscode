from pathlib import Path

from nmk_base._buildenv.template import NmkBaseProjectTemplate, NmkReference


class NmkVsCodeProjectTemplate(NmkBaseProjectTemplate):
    """
    Template for **nmk-vscode** plugin project
    """

    @property
    def references(self) -> list[NmkReference]:
        return super().references + [NmkReference("nmk-vscode!plugin.yml", ["nmk-base!plugin.yml"])]

    @property
    def description(self) -> str:
        return "add VS Code support, including settings files generation"

    @property
    def generated_files(self) -> set[Path]:
        vscode_path = Path(".vscode")
        return super().generated_files | set(
            [
                vscode_path / "settings.json",
                vscode_path / "tasks.json",
                vscode_path / "launch.json",
                vscode_path / "extensions.json",
            ]
        )

    @property
    def post_generation_tasks(self) -> list[str]:
        return super().post_generation_tasks + ["vs.extensions", "vs.settings", "vs.tasks", "vs.launch"]
