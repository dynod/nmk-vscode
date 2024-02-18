# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-vscode`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## Settings

VSCode generated settings may be extended by:
* plugins which want to add support for some language/feature integration in VSCode
* projects which want to customize some VSCode settings

Following config items may be extended for that purpose:
* **{ref}`${vscodeSettingsFiles}<vscodeSettingsFiles>`**: List of settings files to be merged into the generated one.
  Example:
  ```yaml
  vscodeSettingsFiles:
      - ${BASEDIR}/mysettings.json
  ```
* **{ref}`${vscodeSettingsItems}<vscodeSettingsItems>`**: Dictionary of VSCode settings to be merged into the generated settings file.
  Example:
  ```yaml
  vscodeSettingsItems:
      someSetting: some value
  ```

## Extensions

VSCode generated recommended extensions list may be extended by plugins which want to add support for some language/feature integration in VSCode.

Following config items may be extended for that purpose:
* **{ref}`${vscodeExtensionsNames}<vscodeExtensionsNames>`**: List of extensions names to be merged into the generated recommended extensions file.
  Example:
  ```yaml
  vscodeExtensionsNames:
      - some-extension-id
  ```

## Automated tasks

VSCode generated automated tasks file may be extended by plugins which want to add support for some language/feature integration in VSCode.

Following config items may be extended for that purpose:
* **{ref}`${vscodeTasksFiles}<vscodeTasksFiles>`**: List of task files to be merged into the generated one.
  Example:
  ```yaml
  vscodeTasksFiles:
      - ${BASEDIR}/mytasks.json
  ```
* **{ref}`${vscodeNmkTasks}<vscodeNmkTasks>`**: Dictionary of nmk tasks definitions to be merged into the generated automated tasks file.
  Example:
  ```yaml
  vscodeNmkTasks:
      taskName:
          group: build
          runOn: xxx
  ```
* **{ref}`${vscodeShellTasks}<vscodeShellTasks>`**: Dictionary of simple tasks definitions to be merged into the generated automated tasks file.
  Example:
  ```yaml
  vscodeShellTasks:
      taskName:
          group: build
          runOn: folderOpen
          command: ./buildenv.sh init
  ```

## Launch configurations

VSCode generated launch configurations file may be extended by plugins which want to add support for some language/feature integration in VSCode.

Following config items may be extended for that purpose:
* **{ref}`${vscodeLaunchFiles}<vscodeLaunchFiles>`**: List of launch configuration files to be merged into the generated one.
  Example:
  ```yaml
  vscodeLaunchFiles:
      - ${BASEDIR}/mylaunch.json
  ```
