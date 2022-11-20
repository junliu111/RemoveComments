# Remove Comments

[![GitHub](https://img.shields.io/github/license/mejunliu/RemoveComments?logo=GitHub)](https://github.com/mejunliu/RemoveComments/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/mejunliu/RemoveComments?logo=GitHub&style=flat-square)](https://github.com/mejunliu/RemoveComments/stargazers)

Sublime Text plugin: removes all comments in the current file based on syntax highlighting.

![text](images/cpp.gif)


![text](images/latex.gif)


## Installation

Download or clone the contents of this repository to a folder named exactly as the package name into the Packages/ folder of Sublime Text.

## Keybindings
Add your own key bindings: Preferences > Package Settings > Remove Comments > Key Bindings — User

For example, if you want to use "ctrl+alt+shift+r" as the shortcut, please add the following to the opened file.


```
    {
        "keys": [
            "ctrl+alt+shift+r"
        ],
        "command": "remove_file_comments"
    },
```
