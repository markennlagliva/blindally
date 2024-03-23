# Speech Synthesis
from gtts import gTTS
from playsound import playsound

import os
import json
import keyboard


# language = 'en-us' Male || 'en-au' Female
# lang = 'tl' or English
import multiprocessing

from django.conf import settings


class LanguageMode:
    def __init__(self, details) -> None:
        self.details = details

    def english_speak(self):

        import pyttsx3
    
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 170)
        engine.setProperty('voice', voices[1].id)
        engine.say(' '.join(self.details))
        engine.runAndWait()
        # try:
        #     if __name__ == "__main__":
        # # print('This is the length of details.', len([(self.details)]), type(self.details))
        #         p = multiprocessing.Process(target=engine.say, args=(' '.join(self.details)))
        #         p2 = multiprocessing.Process(target=engine.runAndWait)
        #         p.start()
        #         p2.start()
        #         while p.is_alive() and p2.is_alive():
        #             if keyboard.is_pressed('q'):
        #                 p.terminate()
        #                 p2.terminate()
        #             else:
        #                 continue
        #             p.join()
        # except Exception as e:
        #     print(str(e))
        engine.stop()
            
    def tagalog_speak(self):
        from googletrans import Translator
     
        result = Translator().translate(' '.join(self.details), dest='tl')

        # print('This is inside tagalog.', result.text)
        # This is for Filipino Language
        # os.chmod('static/audio', 0o777)
        audio = gTTS(result.text, lang='tl', slow=False)

        print(settings.MEDIA_ROOT, type(settings.MEDIA_ROOT))
        print('playing sound...')
        playsound(f'{settings.MEDIA_ROOT}/notif.mp3')


        print('saving file...')
        audio.save(f'{settings.MEDIA_ROOT}/playsound.mp3')
        print('saved file...')

        print('playing sound...')
        playsound(f'{settings.MEDIA_ROOT}/playsound.mp3')
        print('played sound...')

        print('removing sound...')
        os.remove(f'{settings.MEDIA_ROOT}/playsound.mp3')
        print('removed sound...')


# Status: True = English || False = Tagalog
def speak(details=None, status=True):
    # Home Page || Base
    print('This is the status server:', status)
    print(type(details), details)
    if type(details) != list:
        details = [details]

    if status:
        LanguageMode(details).english_speak() 
    else:
        LanguageMode(details).tagalog_speak()




# AUDIO APPS
from dotenv import load_dotenv
import requests
from requests import post, get
import base64

load_dotenv()
class AudioApps:
    def __init__(self) -> None:  
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

    def get_token(self):
        auth_string = self.client_id + ":" + self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"

        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(self, token):
        return {"Authorization": "Bearer " + token}
    
    '''
        Spotify Audio Book - Logic
    '''
    def search_for_audiobook(self, token, book):
        pass


    '''
        Spotify Music - Logic
    '''

    def search_for_artist(self, token, artist_name):
        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": "Bearer " + token}
        query = f"?q={artist_name}&type=artist&limit=1"

        query_url = url + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["artists"]["items"]

        if len(json_result) == 0:
            print('No artist with this name exists...')
            return None
        
        return json_result[0]
        
    def get_songs_artist(self, token, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
        headers = {"Authorization": "Bearer " + token}
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["tracks"]
        return json_result

