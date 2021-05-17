import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
check = 0
command = 0
kt=0
while  True:
	inSta1 = GPIO.input(23)
	GPIO.output(18,0)
	GPIO.output(13,0)
	if inSta1 == 0 and check == 0:
		check = 1
		kt=1
		command = 1
		os.system("omxplayer demoFPTAISound.mp3")
		check =0



# import RPi.GPIO as GPIO
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.output(18,0)
# GPIO.output(13,0)