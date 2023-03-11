import pyttsx3
text_speech = pyttsx3.init()
print("write that is speech : ")
text = input()
text_speech.say(text)
text_speech.runAndWait()