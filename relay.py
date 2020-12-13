import time
import RPi.GPIO as GPIO
relay = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
try :
    while True:
        GPIO.output(relay,GPIO.HIGH)
        
except KeyboardInterrupt :
    GPIO.output(relay,GPIO.LOW)
    print("close")
