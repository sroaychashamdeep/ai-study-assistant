from gtts import gTTS

def speak(text):

    tts = gTTS(text)

    tts.save("response.mp3")

    return "response.mp3"