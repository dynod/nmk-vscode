# Tasks

The **`nmk-vscode`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

(vs.folder)=
### **`vs.folder`** -- .vscode folder creation

This task creates the **.vscode** folder in the project, if it doesn't exist yet.

| Property | Value/description |
|-         |-
| builder  | [**`nmk_base.common.MkdirBuilder`**](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.MkdirBuilder)
| output   | {ref}`${vscodeFolder}<vscodeFolder>` folder

(vs.settings)=
### **`vs.settings`** -- VSCode settings generation

This task generates the [VSCode workspace settings file](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings), from provided settings fragments and items.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_vscode.builders.SettingsBuilder`
| input    | {ref}`${vscodeSettingsFiles}<vscodeSettingsFiles>` fragment files
| output   | {ref}`${vscodeSettings}<vscodeSettings>` file
| deps     | {ref}`vs.folder<vs.folder>` task

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| files | **{ref}`${vscodeSettingsFiles}<vscodeSettingsFiles>`**
| items | **{ref}`${vscodeSettingsItems}<vscodeSettingsItems>`**


(vs.extensions)=
### **`vs.extensions`** -- VSCode recommended extensions generation

This task generates the [VSCode workspace recommended extensions file](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions), from provided config items.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_vscode.builders.ExtensionsBuilder`
| input    | ${BASEDIR}/extensions.yml
| output   | {ref}`${vscodeExtensions}<vscodeExtensions>` file
| deps     | {ref}`vs.folder<vs.folder>` task

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| names | **{ref}`${vscodeExtensionsNames}<vscodeExtensionsNames>`**

(vs.tasks)=
### **`vs.tasks`** -- VSCode automated tasks generation

This task generates the [VSCode workspace custom tasks file](https://code.visualstudio.com/docs/editor/tasks#_custom-tasks), from provided config items.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_vscode.builders.TasksBuilder`
| inputs    | {ref}`${vscodeTasksFiles}<vscodeTasksFiles>` files <br>{ref}`${vscodeNmkTaskTemplate}<vscodeNmkTaskTemplate>` file
| output   | {ref}`${vscodeTasks}<vscodeTasks>` file
| deps     | {ref}`vs.folder<vs.folder>` task

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| files | **{ref}`${vscodeTasksFiles}<vscodeTasksFiles>`**
| nmk_task_template | **{ref}`${vscodeNmkTaskTemplate}<vscodeNmkTaskTemplate>`**
| nmk_tasks | **{ref}`${vscodeNmkTasks}<vscodeNmkTasks>`**
| default_task | **{ref}`${vscodeDefaultBuildTask}<vscodeDefaultBuildTask>`**

(vs.launch)=
### **`vs.launch`** -- VSCode launch configurations generation

This task generates the [VSCode workspace launch configurations file](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations), from provided config items.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_vscode.builders.LaunchBuilder`
| input    | {ref}`${vscodeLaunchFiles}<vscodeLaunchFiles>` files
| output   | {ref}`${vscodeLaunch}<vscodeLaunch>` file
| deps     | {ref}`vs.folder<vs.folder>` task
| if       | {ref}`${vscodeLaunchFiles}<vscodeLaunchFiles>` item is not empty

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| files | **{ref}`${vscodeLaunchFiles}<vscodeLaunchFiles>`**
