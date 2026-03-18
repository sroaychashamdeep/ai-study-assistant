import speech_recognition as sr
from pydub import AudioSegment
import tempfile


def speech_to_text(audio_bytes):

    recognizer = sr.Recognizer()

    # save webm audio
    webm_file = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
    webm_file.write(audio_bytes)
    webm_file.close()

    # convert webm → wav
    sound = AudioSegment.from_file(webm_file.name, format="webm")

    wav_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sound.export(wav_file.name, format="wav")

    # speech recognition
    with sr.AudioFile(wav_file.name) as source:

        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except:
        return "❌ Could not understand audio"