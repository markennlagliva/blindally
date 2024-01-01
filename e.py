
import elevenlabs
elevenlabs.set_api_key("e0c96d185e2e75e056f2b3d21e4f2652")



voice = elevenlabs.Voice(
    voice_id="EXAVITQu4vr4xnSDxMaL",
    settings = elevenlabs.VoiceSettings(
        stability=0,
        similarity_boost=0.75
    )
)

audio = elevenlabs.generate(
        text="Hello this is blindally, and currently you are in home page.",
        voice = voice
    )
elevenlabs.play(audio)