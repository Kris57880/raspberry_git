#!/usr/local/bin/python
import time
import RPi.GPIO as GPIO
def sound(key):
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT)
    p = GPIO.PWM(15, 50)
    p.start(50)
    if key == 'Do' :
        time.sleep(0.1)
        p.ChangeFrequency(523)
        time.sleep(1)
    elif  key == 'Re':
        time.sleep(0.1)
        p.ChangeFrequency(587)
        time.sleep(1)    
    elif  key == 'Mi':
        time.sleep(0.1)
        p.ChangeFrequency(659)
        time.sleep(1)    
    elif  key == 'Fa':
        time.sleep(0.1)
        p.ChangeFrequency(698)
        time.sleep(1)    
    elif  key == 'So':
        time.sleep(0.1)
        p.ChangeFrequency(784)
        time.sleep(1)    
    elif  key == 'La':
        time.sleep(0.1)
        p.ChangeFrequency(880)
        time.sleep(1)    
    elif  key == 'Si':
        time.sleep(0.1)
        p.ChangeFrequency(988)
        time.sleep(1)    
def play():
    music=["Do","Do","So","So","La","La","So","Fa","Fa","Mi","Mi","Re","Re","Do"]
    for i in range(14):
        sound(music[i])

