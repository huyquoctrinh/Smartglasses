# import serial
# import pygame
from time import sleep

# ser = serial.Serial("/dev/ttyUSB0", 9600)

import cv2, os
from time import sleep
# from script import get_audio, assistant_speaks
from google.cloud import vision
import speech_recognition as sr  
#import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
# import wolframalpha # to calculate strings into formula 
# from selenium import webdriver # to control browser operations 
import subprocess
from subprocess import call
from weather import weather_kt
# from googletrans import Translator
# pygame.init()
# trans= Translator()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./json_file/abc.json"
client = vision.ImageAnnotatorClient()
num = 0
s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if (c in s1): s += s0[s1.index(c)]
        else: s += c
    return s

def detect_text(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    s = ""
    for text in texts:
        s += text.description.replace("\n", " ").replace("  ", " ") + " "
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    s = remove_accents(s).lower()
    if ("mot nghin" in s.lower()): return "một nghìn"
    if ("hai nghin" in s.lower()): return "hai nghìn"
    if ("nam nghin" in s.lower()): return "năm nghìn"
    if ("muoi nghin" in s.lower()): return "mười nghìn"
    if ("hai muoi nghin" in s.lower()): return "hai mươi nghìn"
    if ("nam muoi nghin" in s.lower()): return "năm mươi nghìn"
    if ("mot tram nghin" in s.lower()): return "một trăm nghìn"
    if ("hai tram nghin" in s.lower()): return "hai trăm nghìn"
    if ("nam tram nghin" in s.lower()): return "năm trăm nghìn"
    return("trong ảnh không có tiền 2")

def detect_labels(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    v = []
    p = []
    for label in labels:
        v.append(label.description)
        p.append(label.score)
    #for i in range(len(v)): print(v[i], p[i])
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    for i in range(len(v)):
        if ("money" in v[i].lower()):
            return(detect_text(path))
    return("trong ảnh không có tiền 1")
def process_text(input): 
    try: 
        if 'tìm' in input or 'kiếm' in input: 
            # a basic web crawler using selenium
            print('Chuc nang tim kiem')
            search_web(input) 
            return
  
        elif "bạn là ai" in input or "bạn tên gì" in input: 
            speak = '''Xin chào, mình tên là Google, mình là trợ lí của bạn nè, hihi'''
            assistant_speaks(speak) 
            return
  
        elif "ai tạo ra bạn" in input or "chủ của bạn" in input: 
            speak = "tôi được tạo bởi 2 ông chủ Huy và 1 ông Hào"
            assistant_speaks(speak) 
            return
  
        elif "mắt kính thông minh" in input:# just 
            speak = "Đây là sản phẩm hỗ trợ người khiếm thị."
            assistant_speaks(speak) 
            return
  
        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_speaks("The answer is " + answer) 
            return
        elif 'thời tiết' in input:
            weather_kt()        
        else:
            return 
            #assistant_speaks("tôi có thể tìm kiếm trang web cho bạn") 
            #ans = get_audio() 
            #if 'ok' in str(ans) or 'được' in str(ans): 
                #search_web(input) 
            #else: 
                #return
    except : 
        assistant_speaks("tôi không hiểu bạn nói gì ?") 
        ans = get_audio() 
        if 'có' in str(ans) or 'không' in str(ans): 
            search_web(input)   
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='vi-VN') 
        print("You : ", text) 
        return text 
  
    except: 
  
        #assistant_speaks("Bạn vui lòng nói lại!") 
        return ""

# def translate_cap(caption):
#     translator= Translator()
#     sent= translator.translate(caption, dest='vi',src ='en')
#     return sent.text
def assistant_speaks(output): 
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
    # saving the audio file given by google text to speech 
    file = "assist.mp3" 
    toSpeak.save(file)
    os.system("omxplayer {}".format(file))
     
    os.remove(file)
  
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='vi-VN') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return 0

def takephoto():
    
# initialize the camera
    # cam = cv2.VideoCapture(-1)
    # ret, image = cam.read()

    # if ret:
    # #cv2.imshow('SnapshotTest',image)
    # #cv2.waitKey(0)
    # #cv2.destroyWindow('SnapshotTest')
    #     cv2.imwrite('/home/pi/image.jpg',image)
    # cam.release()
    os.system("fswebcam -r 1280x720 --no-banner /home/pi/image.jpg")
# def webcam():
    
# # initialize the camera
# 	os.system(fswebcam -r 1280x720 --no-banner image3.jpg)
def obj_detect():
    # First take a picture
    """Run a label request on a single image"""
    takephoto()
    with open('/home/pi/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    tv=[]
    for label in labels:
        tv.append(label.description)
    return tv
# def khoangcach():
#     takephoto()
#     try:
#         while (1):
#             if (ser.in_waiting > 0):
#                 data = str(ser.readline())
#                 t = ""
#                 k = obj_detect()
#                 for i in range(len(k)):
#                     t += str(k[i])
#                     if (i != len(k) - 1):
#                         t += str(" và ")
#                 assistant_speaks("cách bạn " + str(6.5*int(float(data[2:len(data) - 5])) // 10) + " xang ti mét có " + t)
#                 break

#     except KeyboardInterrupt:
#         print("Xong")
#     finally:
#         ser.close()
def ocr():
    os.system("fswebcam -r 1280x720 --no-banner /home/pi/image.jpg")
    # cam = cv2.VideoCapture(-1)
    # ret, image = cam.read()

    # if ret:
    # #cv2.imshow('SnapshotTest',image)
    # #cv2.waitKey(0)
    # #cv2.destroyWindow('SnapshotTest')
    #     cv2.imwrite('/home/pi/image.jpg',image)
    # cam.release()
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open('/home/pi/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    if texts==[]:
        assistant_speaks('không có chữ gì ở phía trước bạn')
    else:
        for text in texts:
            sleep(3)
            print('\n"{}"'.format(text.description))
            assistant_speaks(text.description)
            break
#    os.remove('/home/pi/image.jpg')
def giongnoi():
    try:
            assistant_speaks("tôi có thể  giúp gì cho bạn ?")
            while True:
                try:
                    #assistant_speaks("tôi có thể  giúp gì cho bạn ?")
                    text = get_audio().lower() 
          
                    if text == "": 
                        continue
          
                    if "tạm biệt" in str(text) or "ngưng" in str(text) or "sleep" in str(text): 
                        assistant_speaks("tạm biệt ") 
                        break
          
                # calling process text to process the query 
                    process_text(text)
                    assistant_speaks("tôi có thể  giúp gì cho bạn ?") 
                except:
                    print("Chua ket noi mang 1")
                    #assistant_speaks('Bạn chưa kết nối mạng')
    except:
            print("Chua ket noi mang 2")
def tien():
    os.system("fswebcam -r 1280x720 --no-banner /home/pi/image.jpg")
    a = detect_labels('/home/pi/image.jpg')
    print(a)
    assistant_speaks(a)
