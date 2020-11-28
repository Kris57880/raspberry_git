import time
import http.client, urllib
import json
import RPi.GPIO as GPIO
import requests
import socket
import serial
import music
import i2c_lcd

#deviceId = "DxO0kY2u"
#deviceKey = "87oBeIFDtfZUuo2R"
#deviceId = "DmNwrsf9"
#deviceKey = "1y2bYSE70msD2nDL"
deviceId = "DweNqI3l" #109550172
deviceKey = "aNyIGaL6GdsJZxco"

host = "http://api.mediatek.com"
headers = {"Content-type": "application/json", "deviceKey": deviceKey}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ldr_indicator = 14
soil_indicator = 4
GPIO.setup(ldr_indicator,GPIO.OUT)
GPIO.setup(soil_indicator,GPIO.OUT)

def ldr():
    
    endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/ledswitch/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("ldr_display")
    if(value==1):
        print("It's so Dark, Light will turn on.")
        GPIO.output(ldr_indicator,GPIO.HIGH)
    else :
        print("It's Bright Enough.")
        GPIO.output(ldr_indicator,GPIO.LOW)
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
        i2c_lcd.message("soil(%) : "+str(value),  0, 0, False )
    else :
        i2c_lcd.message("ldr(%)  : "+str(value),  1, 0, False )