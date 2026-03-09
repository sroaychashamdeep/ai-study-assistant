import speech_recognition as sr
from pydub import AudioSegment
import tempfile


def speech_to_text(audio):

    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        audio.export(temp_audio.name, format="wav")

        with sr.AudioFile(temp_audio.name) as source:
            audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data)
                return text
            except:
                return "Could not understand audio"