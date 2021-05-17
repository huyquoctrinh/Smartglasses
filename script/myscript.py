# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
# from gtts import gTTS # google text to speech 
import os # to save/open files 
# import wolframalpha # to calculate strings into formula 
# from selenium import webdriver # to control browser operations 
import subprocess
# import pygame
import requests
import playsound
import wget
import time
# pygame.init()
stt=0
# time=2

file1="home/pi/Desktop/MATKINHTHONGMINH/label.py"
file2="home/pi/Desktop/MATKINHTHONGMINH/ocr.py"
file3="home/pi/Desktop/MATKINHTHONGMINH/emo.py"
file4="home/pi/Desktop/MATKINHTHONGMINH/client.py" 
file5="home/pi/Desktop/MATKINHTHONGMINH/client.py"
file6="home/pi/Desktop/MATKINHTHONGMINH/canh.py"
file7="home/pi/Desktop/MATKINHTHONGMINH/logo.py" 
file8= "home/pi/Desktop/MATKINHTHONGMINH/weather.py"
num = 5
def assistant_vn(output):
    global num
    url = 'https://api.fpt.ai/hmi/tts/v5'

    payload = output
    headers = {
    'api-key': '7AtxeVHCYn4cY4xy7wuhMBOaIw57qey3',
    'speed': '',
    'voice': 'linhsan'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    a= response.json()
    num+=1
    file =str(num)+"huyq.mp3"
    print("đang download")
    time.sleep(3)
    wget.download(a["async"], file)
    playsound.playsound(file)
    print('xong')

def search_web(input): 
  
    driver = webdriver.Chrome() 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'youtube' in input.lower(): 
  
        assistant_vn("mở youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
  
    elif 'wikipedia' in input.lower(): 
  
        assistant_vn("mở Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
  
    else: 
  
        if 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
  
        return print('xong')
# def assistant_vn(output): 
#     global num 
  
#     # num to rename every audio file  
#     # with different name to remove ambiguity 
#     num += 1
#     print("PerSon : ", output) 
  
#     toSpeak = gTTS(text = output, lang ='vi', slow = False) 
#     # saving the audio file given by google text to speech 
#     file = str(num)+ ".mp3"
#     toSpeak.save(file) 
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
      
#     # playsound package is used to play the same file. 
      
#     os.remove(file) 
  
  
def process_text(input): 
    try: 
        if 'tìm' in input or 'kiếm' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
        elif "bạn là ai" in input or "bạn tên gì" in input: 
            speak = '''Xin chào, mình tên là Google, mình là trợ lí của bạn nè, hihi'''
            assistant_vn(speak) 
            return
        # elif "bồ" in input or "bạn gái " in input: 
        #     speak = '''bồ Quốc Huy là Đông Phương'''
        #     assistant_vn(speak) 
        #     return
  
        elif "ai tạo ra bạn" in input or "chủ của bạn" in input: 
            speak = "tôi được tạo bởi 2 ông chủ Huy và Nhật"
            assistant_vn(speak) 
            return
  
        elif "mắt kính thông minh" in input:# just 
            speak = """Đây là sản phẩm hỗ trợ người khiếm thị."""
            assistant_vn(speak) 
            return
  
        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_vn("The answer is " + answer) 
            return
        
        elif 'ghi nhớ khuôn mặt' or 'nhớ' or 'lưu trữ' in input: 
            subprocess.run("python3 {}".format(file5),shell=True)
        elif 'tìm kiếm vật thể' or 'kiếm' or 'vật thể' in input: 
            subprocess.run("python3 {}".format(file1),shell=True)
            # another function to open  
            # different application availaible 
        elif 'đọc sách báo' or 'đọc sách' or 'học  bài' or 'đọc báo' or 'chữ' in input: 
            subprocess.run("python3 {}".format(file2),shell=True)
        elif 'mô' or 'tả' or 'mô tả không gian xung quanh' or 'môi trường' or 'xung quanh' in input: 
            subprocess.run("python3 {}".format(file4),shell=True)
        elif 'biểu cảm khuôn mặt' or 'cảm xúc' or 'cảm giác' in input:
            subprocess.run("python3 {}".format(file3),shell=True)
        elif 'logo' or 'nhãn hiệu' or 'thương hiệu' in input:
            subprocess.run("python3 {}".format(file7),shell=True)
        elif 'khung cảnh' or 'danh lam' in input:
            subprocess.run("python3 {}".format(file6),shell=True)
        elif 'thời tiết' in input:
            subprocess.run("python3 {}".format(file8),shell=True)

            # another function to open  
            # different application availaible 
              
            return
  
        else: 
  
            assistant_vn("tôi có thể tìm kiếm trang web cho bạn") 
            ans = get_audio() 
            if 'ok' in str(ans) or 'được' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
  
        assistant_vn("tôi không hiểu bạn nói gì ?") 
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
  
        assistant_vn("Bạn vui lòng nói lại!") 
        return 0
  
  
# Driver Code 
if __name__ == "__main__": 
    assistant_vn("bạn tên gì, Human?") 
    name ='Human'
    name = get_audio() 
    assistant_vn("Hello, " + name + '.') 
      
    while(1): 
  
        assistant_vn("tôi có thể  giúp gì cho bạn ?") 
        text = get_audio().lower() 
  
        if text == 0: 
            continue
  
        if "tạm biệt" in str(text) or "ngưng" in str(text) or "sleep" in str(text): 
            assistant_vn("tạm biệt "+ name+'.') 
            break
  
        # calling process text to process the query 
        process_text(text) 
