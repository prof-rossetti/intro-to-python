# The `SpeechRecognition` Package

The `SpeechRecognition` package provides a high-level interface to record and process audio inputs in Python.

Reference:

  + https://github.com/Uberi/speech_recognition
  + https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
  + https://github.com/s2t2/learning-new-sounds
  + https://github.com/prof-rossetti/voice-interface-demo-py

## Prerequisites

This package depends on another Python package called ["pyaudio"](http://people.csail.mit.edu/hubert/pyaudio/#downloads), which itself depends on a lower-level library caled "portaudio" (not a Python package). To install "portaudio": 

  + On a Mac, use homebrew (`brew install portaudio`). 
  + On Windows, use pipwin within an active virtual environment (see installation steps below).


## Installation

Do these installation steps after activating a virtual environment.

Windows:

```sh
pip install pipwin
pipwin install pyaudio # will install along with lower level binaries
pip install SpeechRecognition # depends on the "pyaudio" Python package
```

Mac:

```sh
pip install pyaudio 
pip install SpeechRecognition
```

## Usage

### Recording Audio

Record audio using your computer's built-in microphone, and save that to a file:

```py
import speech_recognition as sr

client = sr.Recognizer()

with sr.Microphone() as mic:
    print("Say something!")
    audio = client.listen(mic)

with open("my-recording.flac", "wb") as f:
    f.write(audio.get_flac_data())
```

### Recognizing Speech

Record audio using your computer's built-in microphone, and recognize the spoken words:

```py
import speech_recognition as sr

client = sr.Recognizer()

with sr.Microphone() as mic:
    print("Say something!")
    audio = client.listen(mic)

# returns the transcript with the highest confidence:
transcript = client.recognize_google(audio)
#> 'how old is the Brooklyn Bridge'

# returns all transcripts:
response = client.recognize_google(audio, show_all=True)
#> {
#>   'alternative': [
#>     {
#>       'transcript': 'how old is the Brooklyn Bridge',
#>       'confidence': 0.987629
#>     }
#>   ],
#>   'final': True
#> }
```
