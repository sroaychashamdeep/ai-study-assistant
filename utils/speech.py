from gtts import gTTS
import tempfile


def speak(text):

    tts = gTTS(text)

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

    tts.save(temp.name)

    return temp.name