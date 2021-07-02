# Professor Rossetti's Mac Terminal Configuration

These are some of the professor's personal terminal configurations, for your reference. Feel free but not obligated to use them.

## Theme

[Download](http://ethanschoonover.com/solarized/files/solarized.zip) the [Solarized](http://ethanschoonover.com/solarized) color themes, and unzip.

In Terminal Settings, import a new Profile, and choose the **solaraized/osx-terminal.app-colors-solarized/Solarized Dark ansi.terminal** theme.

Set the Solarized Dark profile theme as default.

Increase font size to 18.

## Shortcuts

Optionally further configure the profile by setting specific variables in a special configuration file. This file is called "\~/.bash_profile" for bash shell users (older Macs, Windows Git Bash), or "\~/.zshrc" for zsh shell users (newer Macs). Files beginning with a "." are generally hidden files, so to access them we'll use the text editor's shell commands:

```sh
# Windows Git Bash, Older Macs:
code ~/.bash_profile

# Newer Macs:
code ~/.zshrc
```

After opening the file in your text editor, you can place any of the following contents inside:


``` sh
# this is the ~/.bash_profile file or the ~/.zshrc file...

#
# CONFIGURATIONS
#

# control the "prompt" message that shows up in the terminal
# ... see also: https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html
export PS1=" --->> "

# control some colors
# ... see also: https://osxdaily.com/2012/02/21/add-color-to-the-terminal-in-mac-os-x/
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

#
# SHORTCUTS / ALIASES
#

# listing all files in an easier to read format:
alias ll="ls -lahG"

# shortcuts for most common git commands:
alias gs="git status"
alias gd="git diff"
alias gl="git log"
alias gr="git remote -v"
alias gb="git branch"
alias gpom="git pull origin main"

# hiding or showing all icons on the desktop (when in screenshare or zen modes):
alias deskhide="defaults write com.apple.finder CreateDesktop false && killall Finder"
alias deskshow="defaults write com.apple.finder CreateDesktop true && killall Finder"

# changing scroll direction setting (when connecting my mouse):
# ... Preferences > Trackpad > Scroll & Zoom > Scroll Direction
# ... https://stackoverflow.com/questions/30767674/change-scroll-direction-on-mac-programatically-assign-to-key-combination-comman
#
# can read current setting with:
# ... defaults read -g com.apple.swipescrolldirection
alias scroll_natural="defaults write -g com.apple.swipescrolldirection -bool TRUE"
alias scroll_mouse="defaults write -g com.apple.swipescrolldirection -bool FALSE"

```

> NOTE: if you see some Anaconda-related stuff in this file, leave it as-is!

After editing the config file, save the file. You may need to close your terminal window and re-open a new one for the changes to take effect.
