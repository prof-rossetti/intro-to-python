# The VS Code Text Editor

We'll be writing Python scripts using software called a ["text editor"](https://idrh.ku.edu/text-editors-and-word-processors). Similar to word processing software like Microsoft Word, text editors allow us to write and save documents of text. But unlike word processors, which save extra metadata (e.g. styles and formatting) along with the underling text, text editors allow us to save files comprised of just text. This helps the computer more easily interpret them.

There are many good text editor options out there, including [VS Code](https://code.visualstudio.com/), [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), and [Notepad++](https://notepad-plus-plus.org/), and it seems each developer has their own preference.

Regardless of which text editor you choose, you are highly encouraged to configure it with certain plugins, packages and extensions to enhance your experience and save you time. There are two sets of functionality in particular which will prove especially valuable this semester. These are "Python syntax auto-completion" and "column-style selection", respectively (see basic configuration section below).

## Installation

[Download VS Code](https://code.visualstudio.com/Download).

## Basic Configuration

After you have downloaded VS Code, you'll want to take some time to familiarize yourself with its [settings](https://code.visualstudio.com/docs/getstarted/settings) and menus.

The Command Pallete (accessible by typing "shift + command + P") is perhaps the biggest time-saving tool, and is worth exploring.

### Shell Commands

On a Windows, you may not need to take any action. But on a Mac, follow [these steps](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line) to enable VS Code shell commands.

![](/img/notes/dev-tools/vs-code/vs-code-enable-shell-commands.png)

After enabling shell commands, you should be able to use the `code` command to open files and folders from the command-line:

```sh
# open all files and folders in the current working directory:
code .

# open all files and folders in the specified directory, e.g. "path/to/my-project":
code path/to/my-project
```

### Python Syntax Auto-completion

Once configured, the text editor is capable of automatically completing snippets of Python code for you. This helps improve accuracy, and saves time.

![a screenshot of the text editor's autocomplete functionality](https://user-images.githubusercontent.com/1328807/50870477-2e02ed80-1386-11e9-9a83-506d9c9d39ec.gif)

When you open a Python file in VS Code, it should prompt you to install the official Python extension (`ms-python.python`). You are recommended to install this extension to enable Python syntax auto-completion.

### Column Selection

If configured, your text editor can also enable vertical text selection. This comes in handy if you have to change multiple lines of text at the same time, including commenting-out many lines at once.

![a screenshot of the text editor's column selection](https://user-images.githubusercontent.com/1328807/50870478-2e9b8400-1386-11e9-9378-0afadc4a7dce.gif)

By default, you should be able to achieve column selection functionality in VS Code by pressing "shift + alt" then clicking and dragging up or down.

<hr>

## Further Optional Configurations

These are some of the professor's personal VS Code configurations, for your reference. Feel free but not obligated to use them.

### Extensions

A sample of the professor's installed extensions (results from running `code --list-extensions`):

```sh
HookyQR.beautify
mechatroner.rainbow-csv
mikestead.dotenv
ms-python.python
sleistner.vscode-fileutils
streetsidesoftware.code-spell-checker
whizkydee.material-palenight-theme
xamm.filepath
yzhang.markdown-all-in-one
```

You might try searching these manually or [importing them programmatically](https://stackoverflow.com/a/49398449/670433) via `code --install-extension EXTENSION_NAME`, where "EXTENSION_NAME" is the extension's identifier (see list above).

> DISCLAIMER: the professor has not tested the extension importing process, so if you experience issues, please report them immediately

### User Settings

A sample of relevant settings from the professor's `settings.json` file:

```json
{
  "workbench.activityBar.visible": false,
  "workbench.colorTheme": "Palenight Theme",
  "breadcrumbs.enabled": true,
  "editor.fontSize": 14,
  "editor.wrappingIndent": "none",
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,
  "editor.tabSize": 4,
  "explorer.confirmDragAndDrop": false,
  "explorer.confirmDelete": false,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
  "emmet.showSuggestionsAsSnippets": true,
  "diffEditor.ignoreTrimWhitespace": false,
  "window.zoomLevel": 0,
}
```
