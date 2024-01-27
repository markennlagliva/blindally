# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os

# language = 'en-us' Male || 'en-au' Female
# lang = 'tl' or English

def english_speak(details):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 165)
    engine.setProperty('voice', voices[1].id) 
    engine.say(details[0] + '. and' +details[1])
    engine.runAndWait()

def speak(response, details=None):
    # Home Page || Base
    if response == 'home':
        audio = gTTS('You are currently in Home page', lang='en')
        
    elif response == 'tap-detail-home':
        english_speak(details)
        

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