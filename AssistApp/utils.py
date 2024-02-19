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
        engine.setProperty('rate', 165)
        engine.setProperty('voice', voices[1].id)
        try:
            print(self.details)
            # print('This is the length of details.', len([(self.details)]), type(self.details))
            engine.say(' '.join(self.details))
    
            engine.runAndWait()
            engine.stop()
        except:
            engine.stop()
    
    def tagalog_speak(self):
        from googletrans import Translator
     
        result = Translator().translate(' '.join(self.details), dest='tl')

        # print('This is inside tagalog.', result.text)
        # This is for Filipino Language
        # os.chmod('static/audio', 0o777)
        audio = gTTS(result.text, lang='tl', slow=False)
        audio.save('audio/playsound.mp3')
        playsound('audio/playsound.mp3')
        os.remove('audio/playsound.mp3')
        


# Status: True = English || False = Tagalog
def speak(response, details=None, status=True):
    # Home Page || Base
    print('This is the status server:', status)
    if status:
        if response == 'set-language':
            LanguageMode(details).english_speak()

        if response == 'assistant':
            LanguageMode([details]).english_speak()

        if response == 'home':
            LanguageMode(['Proceeding to Home page.']).english_speak() 
                    
        elif response == 'tap-detail-home':
            LanguageMode(details).english_speak()
            

        # More Page
        elif response == 'motivation':
            LanguageMode(['Going to motivation page.']).english_speak()
        
        elif response == 'tap-more-motivation':
            LanguageMode(details).english_speak()

        elif response == 'technology':
            LanguageMode(['Going to tehcnologies page.']).english_speak()
        
        elif response == 'tap-more-technologies':
            LanguageMode(details).english_speak()  
    else:
        if response == 'set-language':
            print(details)
            LanguageMode(details).tagalog_speak()

        if response == 'assistant':
            LanguageMode([details]).tagalog_speak()

        if response == 'home':
            LanguageMode(['Nasa Home page ka.']).tagalog_speak()

        elif response == 'tap-detail-home':
            LanguageMode(details).tagalog_speak()

        
        elif response == 'motivation':
            LanguageMode(['Nasa motivation page ka.']).tagalog_speak()
        
        elif response == 'tap-more-motivation':
            LanguageMode(details).tagalog_speak()

        elif response == 'technology':
            LanguageMode(['Nasa technologies page ka.']).tagalog_speak()
        
        elif response == 'tap-more-technologies':
            LanguageMode(details).tagalog_speak()  
        