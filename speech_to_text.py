import os
from google.cloud import speech
from google.oauth2 import service_account
from config import GOOGLE_CLOUD_SPEECH_CREDENTIALS

def transcribe_audio(audio_file_path):
    credentials = service_account.Credentials.from_service_account_file(GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    client = speech.SpeechClient(credentials=credentials)

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="zh-CN",
        audio_channel_count=1,
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript
