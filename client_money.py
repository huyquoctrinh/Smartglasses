from __future__ import print_function
import requests
import sys
import json
# import cv2
import os
# from trans import tranlate_text
from gtts import gTTS
# import cv2

num =0

def assistant_speaks(output): 
    global num 
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'money.mp3' 
    toSpeak.save(file)
    os.system("omxplayer money.mp3")
def run():
    os.system("fswebcam -r 1280x720 --no-banner test.jpg")
    addr = 'http://194.62.96.225:8080'
    test_url = addr + '/uploads'

    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    # img = cv2.imread('test.jpg')
    with io.open('test.jpg', 'rb') as image_file:
        content = image_file.read()
    response = requests.post(test_url, data=content, headers=headers)
    # decode response
    #print(json.loads(response.text))
    print(response.text)
    # out=tranlate_text(response.text)
    assistant_speaks(out)
    print('ket thuc')
