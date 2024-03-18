import os
import tempfile
from google.cloud import texttospeech
import pydub
from pydub.playback import play
from config import config

def synthesize_speech(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config["google_cloud_credentials_path"]
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=config["tts_language_code"],
        name=config["tts_voice_name"]
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(response.audio_content)
        audio_file = pydub.AudioSegment.from_mp3(f.name)
        play(audio_file)
