import requests
from pprint import pprint
from trans import translate_text
from gtts import gTTS 

import os 
num=0
def assistant_speaks(output): 
    global num 
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'weather.mp3' 
    toSpeak.save(file)
    os.system("omxplayer weather.mp3")
    #os.system('omxplayer file')  
    # playsound package is used to play the same file. 
    #pygame.mixer.music.load(file)
    #pygame.mixer.music.play()
    #os.remove(file)
def weather_kt():
	# translator = Translator()
	import datetime
	now=datetime.datetime.now()
	x= now.day 
	y= now.hour 
	z= now.minute
	t= now.month
	weatherData = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + "5f0736542e1606c9872f4f3e4703fdd7" + "&q=" + "Ho Chi Minh").json()
	result = translate_text(weatherData["weather"][0]["description"])
	result="Hiện tại là ngày "+str(x)+" tháng "+str(t)+" lúc "+str(y)+" giờ "+str(z)+" phút. "+"Thời tiết hiện tại ở Thành phố Hồ Chí Minh có " + result + " nhiệt độ là " + str(int(weatherData["main"]["temp"] // 10)) + " độ xê độ ẩm là " + str(int(weatherData["main"]["humidity"])) + " phần trăm"
	# speech.save("quochuy.mp3") 
	# os.system("quochuy.mp3")
	print(result)
	assistant_speaks(result)
# weather_kt()