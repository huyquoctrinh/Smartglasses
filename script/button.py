import os
import RPi.GPIO as GPIO
import subprocess
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file1="ocr.py"
file2= "danduong.py"
file3= "money.py"
while True: 
    if GPIO.input(10) == GPIO.HIGH:
    		subprocess.run("python3 {}".format(file1),shell=True)
    if GPIO.input(11) == GPIO.HIGH:
    		subprocess.run("python3 {}".format(file2),shell=True)
    if GPIO.input(12) == GPIO.HIGH:
    		subprocess.run("python3 {}".format(file3),shell=True)
