# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os


# lang = 'tl' or English

def speak(response, details=None):
    if response == 'home':
        audio = gTTS('You are currently in Home page', lang='en')

    elif response == 'tap-detail-home':
        audio = gTTS(details[0] + '. and' +details[1], lang='en', slow=False)

        
    audio.save('audio/playsound.mp3')
    playsound('audio/playsound.mp3')
    os.remove('audio/playsound.mp3')