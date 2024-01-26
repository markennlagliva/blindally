# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os

# language = 'en-us' Male || 'en-au' Female
# lang = 'tl' or English

def speak(response, details=None):
    # Home Page || Base
    if response == 'home':
        audio = gTTS('You are currently in Home page', lang='en')

    elif response == 'tap-detail-home':
        audio = gTTS(details[0] + '. and' +details[1], lang='en', slow=False)

    # More Page
    elif response == 'motivation':
        audio = gTTS('You are currently in Motivation Page', lang='en-au', slow=False)
    
    elif response == 'tap-more-motivation':
        audio = gTTS(details[0] + '. So' +details[1], lang='en-au', slow=False)

    elif response == 'technologies':
        audio = gTTS('You are currently in Motivation Page', lang='en-au', slow=False)
    
    elif response == 'tap-more-technologies':
        audio = gTTS(details[0], lang='en-au', slow=False)
   

    
        
    audio.save('audio/playsound.mp3')
    playsound('audio/playsound.mp3')
    os.remove('audio/playsound.mp3')