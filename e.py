# import threading

# def speak(message):
#     # Simulate speaking the message
#     print("Speaking:", message)

# def index(request):
#     # Call the asynchronous function to get the data
#     data = get_data()
#     # Return JSON response
#     response = 'response'

#     # Start a separate thread to speak the message
#     threading.Thread(target=speak, args=("Hello, World!",)).start()

#     print(response)

a = ['a', 'b', 'c', 'd']

print(a[-2:])



# import elevenlabs
# elevenlabs.set_api_key("e0c96d185e2e75e056f2b3d21e4f2652")


# voice = elevenlabs.Voice(
#     voice_id="EXAVITQu4vr4xnSDxMaL",
#     settings = elevenlabs.VoiceSettings(
#         stability=0,
#         similarity_boost=0.75
#     )
# )

# audio = elevenlabs.generate(
#         text="Hello this is blindally, and currently you are in home page.",
#         voice = voice
#     )
# elevenlabs.play(audio)

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# from googletrans import Translator
# details = ['Hello', 'Whats up']
# print(len(details))
# if len([details]) >= 2: 
#     print('Here 1')
#     result = Translator().translate(details, dest='tl')
# else:
#     print('Here 2')
#     result = Translator().translate(' '.join(details), dest='tl')

# print('This is inside tagalog.', result.text)

# print(str(['Hello']))

# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()

# from googletrans import Translator

# translator = Translator()


# result = Translator().translate('Our team then decided to make a sample website that contains the technologies that will help website become accessible and help blind people in interacting with the website easily by removing technological barrier.', dest='tl')
# print(result.text)


# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

# # Example usage
# text_to_translate = "Hello, how are you?"
# translated_text = translate_text(text_to_translate, target_language='es')
# print(f"Original text: {text_to_translate}")
# print(f"Translated text: {translated_text}")

# class Hello:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def func_name(self):
#         print('It went here')
#         print('This is the none', self.name)

#     def func_age(self):
#         print('This is the self.age', self.age)


# Hello('marvelous', 19).func_age()




# import os
# from dotenv import load_dotenv

# import elevenlabs
# load_dotenv()
# elevenlabs_api = elevenlabs.set_api_key(os.getenv('ELEVENLABS_API_KEY'))

# from elevenlabs import generate, play, voices, Voice, VoiceSettings
# # [print(voice) for voice in voices()]


# audio = generate(
#     text='Hello, What are you doing today?',
#     voice=Voice(
#         voice_id='EXAVITQu4vr4xnSDxMaL',
#         settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0)
#     )
# )
# play(audio)




# from playsound import playsound
"""
import gtts
from gtts import gTTS
from playsound import playsound
text = 'Kamusta kayo lahat? Ako nga pala si blind ally ang inyong tagapaglingkod.'
audio = gTTS(text, lang='tl') # 1. com.mx, 2. pt
audio.save('audio/ex.mp3')
playsound('audio/ex.mp3')
"""
# import os
# from dotenv import load_dotenv

# load_dotenv()
# print(os.getenv('SECRET_KEY'))

# print(help(gtts.lang))

"""from gtts.lang import tts_langs
# print(tts_langs())

for k, v in tts_langs().items():
    print(k, v)"""

'''
    >>> from gtts import gTTS
>>> from io import BytesIO
>>>
>>> mp3_fp = BytesIO()
>>> tts = gTTS('hello', lang='en')
>>> tts.write_to_fp(mp3_fp)
>>>
>>> # Load `mp3_fp` as an mp3 file in
>>> # the audio library of your choice
'''




