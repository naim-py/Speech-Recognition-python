import speech_recognition as sr
r = sr.Recognizer() #allows computers to understand human language
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1) #background noise then have to enable
    print("Please say something ..")
    audio = r.listen(source)
    print("You have said : \n "+r.recognize_google(audio))
    # souce hisebe google speaker
    

''''
import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print(r.recognize_google(r.listen(source)))
'''