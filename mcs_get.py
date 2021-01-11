import time
import http.client, urllib
import json
import RPi.GPIO as GPIO
import requests
import socket
import serial
import music
import i2c_lcd
import Line_notifier as line


#deviceId_host = "DweNqI3l" #109550172
#deviceKey_host = "aNyIGaL6GdsJZxco"
deviceId_host = "DfgskicX" 
deviceKey_host = "0WXK7SwuDx2Vp9Qc"

deviceId_client = "D5Wu3e3g"
deviceKey_client = "DQ4P5W3mkcHIepq8"

host = "http://api.mediatek.com"

now_time=int(time.strftime("%H"))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
light = 4
watering = 14
GPIO.setup(light,GPIO.OUT)
GPIO.setup(watering,GPIO.OUT)


def ldr():
    endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/mode/datapoints"
    headers = {"Content-type": "application/json", "deviceKey": deviceKey_client}
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("ldr_display")
    
    if value == "1": #manual mode
        endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/man_ctl/datapoints"
        headers = {"Content-type": "application/json", "deviceKey": deviceKey_client}
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if value == '1' : GPIO.output(light,GPIO.HIGH)
        else :  GPIO.output(light,GPIO.LOW)
    else : #auto mode 
        endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/ledswitch/datapoints"
        headers = {"Content-type": "application/json", "deviceKey": deviceKey_host}
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if(value==1):
            if (now_time >= 18 or now_time <= 3): #plant need sleep, so the light will turn at particular  time
                print("light will turn on ")
                GPIO.output(light,GPIO.HIGH)
            else :
               GPIO.output(light,GPIO.LOW)
        else :
            GPIO.output(light,GPIO.LOW)

def soil():
    display("soil_display")
    endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/soil_switch/datapoints"
    headers = {"Content-type": "application/json", "deviceKey": deviceKey_host}
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    if(value==1):
        print("Soil Need Water!")
#        music.play()
        GPIO.output(watering,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(watering,GPIO.LOW)
        time.sleep(25)
    else :
        print("Water is Enough")
        GPIO.output(watering,GPIO.LOW)

def display(sensor):
    endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/"+sensor+"/datapoints"
    headers = {"Content-type": "application/json", "deviceKey": deviceKey_host}
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    if sensor == 'soil_display':
        print("soil(%) : "+str(value))
        if value<=1:
            i2c_lcd.message("                ",0,0,False)
        i2c_lcd.message("soil(%) : "+str(value),  0, 0, False )
    else :
        i2c_lcd.message("ldr(%)  : "+str(value),  1, 0, False )
        print("ldr(%)  : "+str(value))

while True:
    ldr()
    time.sleep(1)
    soil()
    time.sleep(1)
