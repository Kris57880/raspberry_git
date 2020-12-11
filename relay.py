import time
import RPi.GPIO as GPIO
relay = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
try :
    while True:
        GPIO.output(relay,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(relay,GPIO.LOW)
        time.sleep(5)
except KeyboardInterrupt :
    print("close")
