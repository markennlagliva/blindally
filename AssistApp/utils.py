# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os

def speak(response):
    if response == 'tap-detail-home':
        audio = gTTS('This is the detail')
    elif response == 'home':
        audio = gTTS('You are currently in Home page')
    audio.save('audio/playsound.mp3')
    playsound('audio/playsound.mp3')
    os.remove('audio/playsound.mp3')