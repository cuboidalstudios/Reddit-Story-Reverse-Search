import speech_recognition as sr

import common
import redditSearch

def transcribe_audio(audio_data, language) -> str:
    r = sr.Recognizer()
    text = r.recognize_google(audio_data, language=language)
    return text


def voiceToText(file):
    with sr.AudioFile(file) as source:
        audio_data = sr.Recognizer().record(source)
        text = transcribe_audio(audio_data, "english")
    print(text)
    common.changeLog(text)
    with open("transcript", "w") as f:
        f.write(text)
    redditSearch.redditSearch(text)
