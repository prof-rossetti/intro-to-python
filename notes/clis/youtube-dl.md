# The `youtube-dl` Utility

The `youtube-dl` command-line utility provides capabilities for downloading videos from YouTube and other sites.

> DISCLAIMER: this guide is for instructional purposes only. Students, please obey all copyright laws!

References:

  + [Website](http://ytdl-org.github.io/youtube-dl/)
  + [Source Code](https://github.com/ytdl-org/youtube-dl)
  + [Installation](https://github.com/ytdl-org/youtube-dl#installation)
  + [Output Options](https://github.com/ytdl-org/youtube-dl#output-template)

## Installation

### Installation on Mac

Mac users can install `youtube-dl` via [Homebrew](/notes/clis/brew.md):

```sh
brew install youtube-dl
```

After installing, restart your terminal application, where you should now be able to execute `youtube-dl` commands (like `youtube-dl --help`).

### Installation on Windows

Windows users can install `youtube-dl` by visiting the [Installation Guide](https://github.com/ytdl-org/youtube-dl#installation) and clicking "Download an .exe file".

After downloading onto your local computer, locate the "youtube-dl.exe" file and move it to a more permanent location (like the Desktop).

Wherever you move it to, observe the absolute filepath location of the "youtube-dl.exe" file. When you need to use the `youtube-dl` utility in the future, reference it from this location (e.g. `~/Desktop/youtube-dl --help`).

## Usage

Note the URL of a YouTube video you'd like to download (e.g. "https://www.youtube.com/watch?v=ABC123").

Then download it, specifying the video URL and the desired local file name:

```sh
youtube-dl -o my_video.mp4 "https://www.youtube.com/watch?v=ABC123"
```

If you have issues downloading the video to MP4 (for example if you see the error message "requested-formats-are-incompatible-for-merge"), you may have luck [adjusting](https://askubuntu.com/questions/806258/requested-formats-are-incompatible-for-merge) the output file format:

```sh
youtube-dl -o my_video.mp4 "https://www.youtube.com/watch?v=ABC123" -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
```
