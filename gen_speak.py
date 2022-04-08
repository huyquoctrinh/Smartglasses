from gtts import gTTS
import os
from playsound import playsound
def assistant_speaks(output): 
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
    # saving the audio file given by google text to speech 
    file = "start.mp3" 
    toSpeak.save(file)
    playsound(file)
    # os.system("omxplayer -o alsa {}".format(file))
assistant_speaks("đã khởi động xong")