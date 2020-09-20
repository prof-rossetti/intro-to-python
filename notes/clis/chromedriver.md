# The `chromedriver` Utility

The [`chromedriver`](http://chromedriver.chromium.org)utility enables automated web browsing via a Chrome-like web browser.

## Installation

Detect if `chromedriver` is already installed, and if so, where:

```sh
# is chromedriver installed?
chromedriver --version

# is chromedriver installed (via homebrew)?
/usr/local/bin/chromedriver --version
```

[Install `chromedriver`](http://chromedriver.chromium.org/getting-started), if necessary (on Mac or Windows), or on Mac, can do this via [`homebrew`](/notes/clis/brew.md) and [`brew cask`](https://github.com/Homebrew/homebrew-cask):

```sh
# install (on Mac OS, via homebrew):
brew cask install chromedriver

# (if you need to upgrade chromedriver):
brew cask upgrade chromedriver
```

Observe the location where your `chromedriver` utility has been installed (e.g. "/usr/local/bin/chromedriver").

## Usage

Use [the `selenium` package](/notes/python/packages/selenium.md) to control the `chromedriver` from a Python script.

## Troubleshooting

If you're using `chromedriver` on Mac and you see an error like "chromedriver cannot be opened because the developer cannot be verified", you must first [adjust your security  and privacy settings](https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de) to "Allow Anyway", and afterwards it should work.
