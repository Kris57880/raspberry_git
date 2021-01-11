import RPi.GPIO  as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setwarnings(False) 
GPIO.output(7,True)