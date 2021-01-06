import speech_recognition as sr
from gtts import gTTS
import os
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        wake="For English say English...............malayalathin Malayalam yennu parayukaa"
        language='ml'
        output=gTTS(text=wake,lang=language,slow=False)
        output.save("output.mp3")
        os.system("start output.mp3") 
        language='ml' 
        audio = r.listen(source) 
        print("You have said \n" + r.recognize_google(audio))   
        num=(r.recognize_google(audio)) 
        if(num=="Malayalam"):
            print("Please say the PNR Number")        
            audio = r.listen(source)
            print("Recognizing Now ... ")
            # recognize speech using google
            try:
                language='ml'
                print("You have said \n" + r.recognize_google(audio))
                xxx=r.recognize_google(audio)                             
                if xxx==12345:
                    xx="Rajadhani Express"
                    language='ml'
                    output=gTTS(text=xx,lang=language,slow=False)
                    output.save("output.mp3")
                    os.system("start output.mp3")                
                else:
                    oo="ദയവായി വീണ്ടും ശ്രമിക്കുക"
                    language='ml'
                    output=gTTS(text=oo,lang=language,slow=False)             
                    output.save("output.mp3")
                    print(output)
                    os.system("start output.mp3")          
                                                                                           
            except Exception as e:
                print("Error :  " + str(e)) 
                        
        if(num=="English"):
            print("Please say the PNR Number")        
            audio = r.listen(source)
            print("Recognizing Now ... ")
            # recognize speech using google
            try:
                print("You have said \n" + r.recognize_google(audio))
                xxx=int(r.recognize_google(audio))                              
                if xxx==12345:
                    xx1="Rajadhani Express"
                    language='en'
                    output=gTTS(text=xx1,lang=language,slow=False)
                    output.save("output.mp3")
                    os.system("start output.mp3")                
                else:
                    oo="Try again"
                    language='en'
                    output=gTTS(text=oo,lang=language,slow=False)             
                    output.save("output.mp3")
                    print(output)
                    os.system("start output.mp3")          
                                                                                           
            except Exception as e:
                print("Error :  " + str(e)) 
if __name__ == "__main__":
    main()