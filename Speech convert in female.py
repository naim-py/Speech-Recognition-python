from gtts import gTTS
import os
speech = gTTS("welcome to my channel ig tech team")
speech.save('welcome.mp3')
os.system('start welcome.mp3')
