import time
import RPi.GPIO as GPIO
relay = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
try :
    while True:
        GPIO.output(relay,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relay,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt :
    print("close")