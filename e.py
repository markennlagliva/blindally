
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

import os
from dotenv import load_dotenv

# import elevenlabs
# load_dotenv()
# elevenlabs_api = elevenlabs.set_api_key(os.getenv('ELEVENLABS_API_KEY'))

# from elevenlabs import generate, play, voices
# # [print(voice) for voice in voices()]

# audio = generate(
#     text='Hello, This blindally.',
#     voice='Adam',
#     model='eleven_multilingual_v2',
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




