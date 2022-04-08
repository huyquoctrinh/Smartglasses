import os
import RPi.GPIO as GPIO
import time
import subprocess
from modules import ocr,giongnoi
from client_money import run
from cap import caption
from weather import weather_kt
# from khoangcach import dis
from tien import detect_money
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# file1="arduino.py"
# file2="ocr.py"

def do_script():
    check = 0
    command = 0
    # 0 IDLE
    # 1 CALL VOICE
    # 2 OCR
    # 3 MONEY
    # 4 ENVI DES
    kt=0
    os.system("omxplayer -o alsa /home/pi/kinh/start.mp3")
    while True:
        inSta1 = GPIO.input(23)
        inSta2 = GPIO.input(24)
        inSta3 = GPIO.input(25)
        inSta4 = GPIO.input(26)
        # inSta5 = GPIO.input(27)
        # inSta6 = GPIO.input(28)
        if inSta1 == 0 and check == 0:
            check = 1
            kt=1
            command = 1
            os.system("omxplayer -o alsa /home/pi/kinh/money.mp3")
            # subprocess.run("python3 {}".format(file1),shell=True)
            detect_money()
            check =0
            # khoangcach()
        elif inSta2 == 0 and check == 0:
            check = 1
            kt=1
            command = 2
            os.system("omxplayer -o alsa /home/pi/kinh/bao.mp3")
            # subprocess.run("python3 {}".format(file2),shell=True)
            ocr()
            check =0
        elif inSta3 == 0 and check == 0:
            check = 1
            kt=1
            command = 3
            # subprocess.run("python3 {}".format(file3),shell=True)
            os.system("omxplayer -o alsa /home/pi/kinh/cap.mp3")
            caption()
            check =0
        elif inSta4 == 0 and check == 0:
            check = 1
            kt=1
            command = 4
            os.system("omxplayer -o alsa /home/pi/kinh/troliao.mp3")
            # ubprocess.run("python3 {}".format(file4),shell=True)
            weather_kt()
            check =0
        elif inSta1 == 1 and inSta2 == 1 and inSta3 == 1 and inSta4 == 1:
            check = 0
            command = 0
            kt=0
    #     # dis(kt)
        print(command, check)
