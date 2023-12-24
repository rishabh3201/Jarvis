#Hindi to English
#library 
#pip install googletrans==3.1.0a0
#pip install speechrecognition


import speech_recognition as sr
from googletrans import Translator


# 1. Listen function
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
    except:
        return ""
    query = str(query).lower()
    return query

# 2. English Translation
def TranslationHinditoEnglish(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You: {data}.")
    return data

# 3. connect 
def MicExecution():
    query = Listen()
    data = TranslationHinditoEnglish(query)
    return data

MicExecution()