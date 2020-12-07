import time
import RPi.GPIO as GPIO
#import mcs_upload 
import Line_notifier as notifier
status = 0
RAIN = 1 
SUN = 0
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin ,GPIO.IN)
try :
	while True :
		if GPIO.input(pin)==GPIO.LOW:
			print("raining")
			if status == SUN :
				notifier.line_message("it's raining")
				status = RAIN 
		else :
			print("sunny")
			if status == RAIN :
				notifier.line_message("it's sunny again ")
				status = SUN
		time.sleep(20)
except KeyboardInterrupt:
	print("close")  	 
