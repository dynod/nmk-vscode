# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-vscode!plugin.yml
```

Then once the **nmk setup** phase is executed, settings are nicely generated so that when you open the project folder in [VS Code](https://code.visualstudio.com/), many features are integrated in the IDE workflow:
* Recommended extensions install
* Integrated **`nmk`** build tasks
* Language-specific integration (to be provided by extra **`nmk`** plugins)

Note that [VS Code](https://code.visualstudio.com/) integration has also been tested to be fully functional in web IDE (typically [Github Codespaces](https://github.com/features/codespaces)).
