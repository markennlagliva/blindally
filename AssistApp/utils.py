# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os

# language = 'en-us' Male || 'en-au' Female
# lang = 'tl' or English

class LanguageMode:
    def __init__(self, details, status) -> None:
        self.details = details
        self.status = status

    def english_speak(self):
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 170)
        engine.setProperty('voice', voices[1].id) 
        engine.say(self.details[0] + '. and' +self.details[1])
        engine.runAndWait()
        engine.stop()
    
    def tagalog_speak(self):
        from googletrans import Translator
        result = Translator().translate(self.details[0] + self.details[1], dest='tl')

        # This is for Filipino Language
        audio = gTTS(result.text, lang='tl', slow=False)
        audio.save('audio/playsound.mp3')
        playsound('audio/playsound.mp3')
        os.remove('audio/playsound.mp3')


# Status: True = English || False = Tagalog
def speak(response, details=None, status=False):
    # Home Page || Base
    
    if response == 'home':
        audio = gTTS('You are currently in Home page', lang='en')
        
        
    elif response == 'tap-detail-home':
        pass
        

    # More Page
    elif response == 'motivation':
        audio = gTTS('You are currently in Motivation Page', lang='en-au', slow=False, tld='us')
    
    elif response == 'tap-more-motivation':
        audio = gTTS(details[0] + '. So' +details[1], lang='en-au', slow=False, tld='us')

    elif response == 'technologies':
        audio = gTTS('You are currently in Motivation Page', lang='en-au', slow=False, tld='us') 
    
    elif response == 'tap-more-technologies':
        audio = gTTS(details[0], lang='en-au', slow=False, tld='us')
   

