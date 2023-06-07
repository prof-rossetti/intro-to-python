# The `IPython` Package

This document provides examples of using the `IPython` package's `display` submodule to display images and play audio files in a notebook environment like Google Colab.

References:
  + https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
  + https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.Image
  + https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.Audio


## Installation

This package is already installed by default in Colab notebooks, so this installation step may not be necessary in the Colab notebook environment:

```sh
pip install IPython
```

## Usage

### Displaying Images

We can use the `display` submodule of the `IPython` package to display images, given an image filepath or image url:

```py
from IPython.display import Image, display 
 
print("-----------")
print("EXAMPLE IMAGES:")

print("-----------")
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Georgetown_Hoyas_logo.svg/64px-Georgetown_Hoyas_logo.svg.png"
display(Image(url=image_url, height=100))

print("-----------")
display(Image(url="https://www.python.org/static/community_logos/python-powered-w-200x80.png"))

print("-----------")
display(Image(url="https://banner2.cleanpng.com/20190914/tca/transparent-market-icon-news-icon-newspaper-icon-5d7ce8e6009aa0.6164315815684671740025.jpg", height=100))
```

<img width="312" alt="Screenshot 2023-06-07 at 11 13 06 AM" src="https://github.com/prof-rossetti/intro-to-python/assets/1328807/edbbfe69-ea19-4cf6-8355-216d27aa457c">

### Playing Audio

We can use the `display` module to play audio files as well.

#### Playing Audio from File

To practice with an example audio file, first use this code to download the provided audio file into your notebook's filesystem:

```py
!wget "https://github.com/s2t2/ml-music-2023/raw/main/test/audio/pop.00032.wav"
```

Then we can play the audio:

```py
audio_filepath = "pop.00032.wav"
display(Audio(audio_filepath, autoplay=False)) # rate only necessary when passing custom audio data
```


