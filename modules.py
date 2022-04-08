from time import sleep

# ser = serial.Serial("/dev/ttyUSB0", 9600)

import os
from time import sleep
# from script import get_audio, assistant_speaks
from google.cloud import vision
import speech_recognition as sr  
from google.cloud.vision import types
#import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from tien import detect_money
import subprocess
from subprocess import call
from weather import weather_kt
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="abc.json"
client = vision.ImageAnnotatorClient()
num = 0
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
    file = "/home/pi/kinh/assist.mp3" 
    toSpeak.save(file)
    os.system("omxplayer -o alsa {}".format(file))
     
    # os.remove(file)
  
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
    cam = cv2.VideoCapture(-1)
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('/home/pi/image.jpg',image)
    cam.release()

def obj_detect():
    takephoto() # First take a picture
    """Run a label request on a single image"""

    with open('/home/pi/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
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

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    # if texts==[]:
    #     assistant_speaks('không có chữ gì ở phía trước bạn')
    # else:
    k = 0
    for text in texts:
        k = 1
        sleep(3)
        print('\n"{}"'.format(text.description))
        assistant_speaks(text.description)
        break
    if (k==0):
        print("không có gì trước mắt bạn")
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
    takephoto()
    a = detect_labels('/home/pi/image.jpg')
    print(a)
    assistant_speaks(a)