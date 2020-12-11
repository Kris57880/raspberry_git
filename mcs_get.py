import time
import http.client, urllib
import json
import RPi.GPIO as GPIO
import requests
import socket
import serial
import music
import i2c_lcd


#deviceId = "DweNqI3l" #109550172
#deviceKey = "aNyIGaL6GdsJZxco"
deviceId = "DfgskicX" 
deviceKey = "0WXK7SwuDx2Vp9Qc"

host = "http://api.mediatek.com"
headers = {"Content-type": "application/json", "deviceKey": deviceKey}

now_time =time.strftime(“%H”)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
light = 4
soil_indicator = 14
GPIO.setup(light,GPIO.OUT)
GPIO.setup(soil_indicator,GPIO.OUT)

def ldr():
    
    endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/ledswitch/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("ldr_display")
    if(value==1):
        if (now_time <=21 or now_time >= 5):
            print("light will turn on ")
            GPIO.output(light,GPIO.HIGH)

    else :
        print("light will not turn on")
        GPIO.output(light,GPIO.LOW)
def soil():
    endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/soil_switch/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("soil_display")
    if(value==1):
        print("Soil Need Water!")
        music.play()
        GPIO.output(soil_indicator,GPIO.HIGH)
    else :
        print("Water is Enough")
        GPIO.output(soil_indicator,GPIO.LOW)

def display(sensor):
    endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/"+sensor+"/datapoints"
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