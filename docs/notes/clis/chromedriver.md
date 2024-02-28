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

[Install `chromedriver`](http://chromedriver.chromium.org/getting-started), if necessary (on Mac or Windows), or on Mac, can do this via [`homebrew`](/notes/clis/brew.md):

```sh
# install (on Mac OS, via homebrew):
brew install chromedriver

# (if you need to upgrade chromedriver):
brew upgrade chromedriver
```

Observe the location where your `chromedriver` utility has been installed (e.g. "/usr/local/bin/chromedriver").

## Usage

Use [the `selenium` package](/notes/python/packages/selenium.md) to control the `chromedriver` from a Python script.

## Troubleshooting

If you're using `chromedriver` on Mac and you see an error like "chromedriver cannot be opened because the developer cannot be verified", see if one of the following remedies works for you:

  + try [adjusting your security and privacy settings](https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de) to "Allow Anyway", and afterwards it should work.
  + try telling your computer to [trust chromedriver](https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/): `xattr -d com.apple.quarantine /usr/local/bin/chromedriver`

