# Configuration Reference

The **`nmk-vscode`** plugin handles the configuration items listed in this page.

All of them are initiliazed with convenient default values, so that you don't need to setup them for a default working behavior. You can anyway override them in your project if you need to fine tune the plugin behavior. [Some items](extend.md) are specifically designed to be extended by **`nmk`** projects and plugins.

## Settings

(vscodeFolder)=
### **`vscodeFolder`** -- VSCode settings folder

| Type | Default value |
|-     |-
| str  | ${PROJECTDIR}/.vscode

This is the path where VSCode reads its workspace configuration files.

(vscodeSettings)=
### **`vscodeSettings`** -- VSCode generated settings file

| Type | Default value |
|-     |-
| str  | {ref}`${vscodeFolder}<vscodeFolder>`/settings.json

This is the generated [VSCode workspace settings file](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings).

(vscodeSettingsFiles)=
### **`vscodeSettingsFiles`** -- VSCode settings files fragments

| Type | Default value |
|-     |-
| List[str]  | ["${BASEDIR}/base_settings.json"]

This is a list of VSCode settings file fragments to be merged into the target {ref}`${vscodeSettings}<vscodeSettings>` generated one.

(vscodeSettingsItems)=
### **`vscodeSettingsItems`** -- VSCode settings items

| Type | Default value |
|-     |-
| Dict[str,str]  | {}

Dictionary of VSCode settings items to be merged into the target {ref}`${vscodeSettings}<vscodeSettings>` generated one (after all {ref}`${vscodeSettingsFiles}<vscodeSettingsFiles>` files have been merged).

## Extensions

(vscodeExtensions)=
### **`vscodeExtensions`** -- VSCode generated recommended extensions file

| Type | Default value |
|-     |-
| str  | {ref}`${vscodeFolder}<vscodeFolder>`/extensions.json

This is the generated [VSCode workspace recommended extensions file](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions).

(vscodeExtensionsNames)=
### **`vscodeExtensionsNames`** -- VSCode recommended extensions list

| Type | Default value |
|-     |-
| List[str]  | []

List of VSCode recommended extensions to be generated in target {ref}`${vscodeExtensions}<vscodeExtensions>` file.

## Automated tasks

(vscodeTasks)=
### **`vscodeTasks`** -- VSCode generated automated tasks file

| Type | Default value |
|-     |-
| str  | {ref}`${vscodeFolder}<vscodeFolder>`/tasks.json

This is the generated [VSCode workspace custom tasks file](https://code.visualstudio.com/docs/editor/tasks#_custom-tasks).

(vscodeTasksFiles)=
### **`vscodeTasksFiles`** -- VSCode task files

| Type | Default value |
|-     |-
| List[str]  | []

This is a list of VSCode task files to be merged into the target {ref}`${vscodeTasks}<vscodeTasks>` generated one.

(vscodeTaskTemplate)=
### **`vscodeTaskTemplate`** -- nmk task template file

| Type | Default value |
|-     |-
| str  | ${BASEDIR}/templates/nmk-tasks.json.jinja

This is the template file for generated nmk tasks.

(vscodeNmkTasks)=
### **`vscodeNmkTasks`** -- VSCode nmk tasks definition

| Type | Default value |
|-     |-
| Dict[str,Dict[str,str]]  | see tasks.yml

This a dictionary defining the nmk tasks to be generated into the target {ref}`${vscodeTasks}<vscodeTasks>` generated task file.

(vscodeShellTasks)=
### **`vscodeShellTasks`** -- VSCode shell tasks definition

| Type | Default value |
|-     |-
| Dict[str,Dict[str,str]]  | see tasks.yml

This a dictionary defining the simple shell tasks to be generated into the target {ref}`${vscodeTasks}<vscodeTasks>` generated task file.

(vscodeDefaultBuildTask)=
### **`vscodeDefaultBuildTask`** -- Default build task

| Type | Default value |
|-     |-
| str  | build

This is the name of the generated task to be declared as default build one (the one invoked when hitting **`Ctrl+shift+B`** in VSCode) in the target {ref}`${vscodeTasks}<vscodeTasks>` generated file.

(vscodeDefaultTestTask)=
### **`vscodeDefaultTestTask`** -- Default build task

| Type | Default value |
|-     |-
| str  | tests

This is the name of the generated task to be declared as default test one (the one invoked when hitting **`Ctrl+shift+T`** in VSCode) in the target {ref}`${vscodeTasks}<vscodeTasks>` generated file.

*<span style="color:green">Added in version 1.1.0</span>*

## Launch configurations

(vscodeLaunch)=
### **`vscodeLaunch`** -- VSCode generated launch configurations file

| Type | Default value |
|-     |-
| str  | {ref}`${vscodeFolder}<vscodeFolder>`/launch.json

This is the generated [VSCode workspace launch configurations file](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations).

(vscodeLaunchFiles)=
### **`vscodeLaunchFiles`** -- VSCode launch configuration files

| Type | Default value |
|-     |-
| List[str]  | []

This is a list of VSCode launch configuration files to be merged into the target {ref}`${vscodeLaunch}<vscodeLaunch>` generated one.
