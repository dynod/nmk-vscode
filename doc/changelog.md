# Changelog

Here are listed all the meaningfull changes done on **`nmk-vscode`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-vscode/releases)
```

## Release 1.2.0

- Update for buildenv 2 handling:
  - terminal integration in settings
  - nmk tasks for setup/build/tests

## Release 1.1.0

- Update generated settings:
  - disable environment activation in terminal (since it's already handled by buildenv integration)
  - enable yaml format on save through [Prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- Update generated tasks: identify test task as the default one
- New {ref}`${vscodeDefaultTestTask}<vscodeDefaultTestTask>` config item to identify the default test task name
- Added [Prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) to {ref}`${vscodeExtensionsNames}<vscodeExtensionsNames>` config item (list of extensions suggestions)
