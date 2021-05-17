# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
# import wolframalpha # to calculate strings into formula 
# from selenium import webdriver # to control browser operations 
import subprocess
from playsound import playsound
stt=1
time=2

file1="/home/pi/Desktop/MATKINHTHONGMINH/label.py"
 
num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
    # saving the audio file given by google text to speech 
    file =  str(num)+"assist.mp3 " 
    toSpeak.save(file) 
    # os.system("mpg321 -q assist.mp3")
    # playsound package is used to play the same file. 
    playsound(file) 
    os.remove(file) 
  
  
def process_text(input): 
    try: 
        if 'tìm' in input or 'kiếm' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
        elif "bạn là ai" in input or "bạn tên gì" in input: 
            speak = '''Xin chào, mình tên là Google, mình là trợ lí của bạn nè, hihi'''
            assistant_speaks(speak) 
            return
  
        elif "ai tạo ra bạn" in input or "chủ của bạn" in input: 
            speak = "tôi được tạo bởi 2 ông chủ Huy và Nhật"
            assistant_speaks(speak) 
            return
  
        elif "mắt kính thông minh" in input:# just 
            speak = """Đây là sản phẩm hỗ trợ người khiếm thị."""
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
  
        elif 'chức năng' in input: 
            subprocess.run("python3 {}".format(file1),shell=True)
            # another function to open  
            # different application availaible 
              
            return
  
        else: 
  
            assistant_speaks("tôi có thể tìm kiếm trang web cho bạn") 
            ans = get_audio() 
            if 'ok' in str(ans) or 'được' in str(ans): 
                search_web(input) 
            else: 
                return
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
  
        assistant_speaks("Bạn vui lòng nói lại!") 
        return 0
  
  
# Driver Code 
if __name__ == "__main__": 
    assistant_speaks("bạn tên gì, Human?") 
    name ='Human'
    name = get_audio() 
    assistant_speaks("Hello, " + str(name) + '.') 
      
    while(1): 
  
        assistant_speaks("tôi có thể  giúp gì cho bạn ?") 
        text = get_audio().lower() 
  
        if text == 0: 
            continue
  
        if "tạm biệt" in str(text) or "ngưng" in str(text) or "sleep" in str(text): 
            assistant_speaks("tạm biệt "+ name+'.') 
            break
  
        # calling process text to process the query 
        process_text(text) 
