import Speech as sr
r=sr.Recognizer()
print("Please Talk")
with sr.Microphone as source:
    audio=r.record(source,duration=5)
    print("Recognizing...")
    text=r.Recognizer_google(audio)
    print(text)