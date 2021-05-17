import RPi.GPIO as GPIO 
import subprocess
file1="label.py"
file2="ocr.py"
file3= "assist.py"
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True: 
	try:
		if GPIO.input(10) == GPIO.HIGH:
			subprocess.run("python3 {}".format(file2),shell=True)
			break
		if GPIO.input(11) == GPIO.HIGH:
			subprocess.run("python3 {}".format(file2),shell=True)
			break
		if GPIO.input(12) == GPIO.HIGH:
			subprocess.run("python3 {}".format(file3),shell=True)
			break
	except:
		print("Error")