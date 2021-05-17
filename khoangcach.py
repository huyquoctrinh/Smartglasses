import serial
import pygame
from time import sleep

ser = serial.Serial("/dev/ttyUSB0", 9600)

import cv2, os
from time import sleep
# from script import get_audio, assistant_speaks
from google.cloud import vision
# import speech_recognition as sr  
#import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
# import wolframalpha # to calculate strings into formula 
# from selenium import webdriver # to control browser operations 
import subprocess
from subprocess import call
# from googletrans import Translator
pygame.init()
trans= Translator()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="thi.json"
client = vision.ImageAnnotatorClient()
num = 0
def translate_cap(caption):
    translator= Translator()
    sent= translator.translate(caption, dest='vi',src ='en')
    return sent.text


# def assistant_speaks(output): 
#     toSpeak = gTTS(text = output, lang ='vi', slow = False) 
#     # saving the audio file given by google text to speech 
#     file = "/home/pi/Desktop/MATKINHTHONGMINH/arduino.mp3" 
#     toSpeak.save(file)
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
     
#     os.remove(file) 

def assistant_speaks(output): 
    global num 
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'khoangcach.mp3' 
    toSpeak.save(file)
    os.system("mpg321 -q sound.mp3")  

def takephoto():
    
# initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('dis.jpg',image)
    cam.release()

def obj_detect():
    takephoto() # First take a picture
    """Run a label request on a single image"""

    with open('dis.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    tv=[]
    for label in labels:
        tv.append(translate_cap(label.description))
    return tv
def dis(kt):
    try:
        while (1):
            if (kt==1):
                break
            else:
                if (ser.in_waiting > 0):
                    data = str(ser.readline())
                    if data<=150:
                        t = ""
                        k = obj_detect()
                        for i in range(len(k)):
                            t += str(k[i])
                            if (i != len(k) - 1):
                                t += str(" và ")
                        assistant_speaks("cách bạn " + str(6.5*int(float(data[2:len(data) - 5])) // 10) + " xang ti mét có " + t)

    except KeyboardInterrupt:
        print("Xong")
    finally:
        ser.close()