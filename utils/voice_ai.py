from audiorecorder import audiorecorder

def record_voice():

    audio = audiorecorder("Start Recording", "Stop Recording")

    return audio