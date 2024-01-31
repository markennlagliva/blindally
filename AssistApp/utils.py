# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os

# language = 'en-us' Male || 'en-au' Female
# lang = 'tl' or English

class LanguageMode:
    def __init__(self, details) -> None:
        self.details = details

    def english_speak(self):
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 170)
        engine.setProperty('voice', voices[1].id)

        print('This is the length of details.', len([(self.details)]), type(self.details))
        if len([self.details]) >= 2:
            engine.say(self.details[0] + '. and' +self.details[1])
        engine.say(self.details)
        engine.runAndWait()
        engine.stop()
    
    def tagalog_speak(self):
        from googletrans import Translator
        if len([self.details]) >= 2:
            result = Translator().translate(self.details[0] + self.details[1], dest='tl')
        result = Translator().translate(str(self.details), dest='tl')
        print('This is inside tagalog.', result.text)
        # This is for Filipino Language
        audio = gTTS(result.text, lang='tl', slow=False)
        audio.save('audio/playsound.mp3')
        playsound('audio/playsound.mp3')
        os.remove('audio/playsound.mp3')


# Status: True = English || False = Tagalog
def speak(response, details=None, status=True):
    # Home Page || Base
    print('This is the status server:', status)
    if status:
        if response == 'home':
            details = 'Proceeding to home page.'
            LanguageMode(details).english_speak() 
                    
        elif response == 'tap-detail-home':
            LanguageMode(details).english_speak()
            

        # More Page
        elif response == 'motivation':
            LanguageMode(details).english_speak()
        
        elif response == 'tap-more-motivation':
            LanguageMode(details).english_speak()

        elif response == 'technologies':
            LanguageMode(details).english_speak()
        
        elif response == 'tap-more-technologies':
            LanguageMode(details).english_speak()  
    else:
        if response == 'home':
            details = 'Nasa Home Page na tayo.'
            LanguageMode(details).tagalog_speak()
        elif response == 'tap-detail-home':
            LanguageMode(details).tagalog_speak()
        