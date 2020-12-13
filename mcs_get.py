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
headers = {"Content-type": "application/json", "deviceKey_host": deviceKey_host}

now_time=int(time.strftime("%H"))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
light = 4
watering = 14
GPIO.setup(light,GPIO.OUT)
GPIO.setup(watering,GPIO.OUT)


def ldr():
    endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/mode/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("ldr_display")
    if value == True : #manual mode
        endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/man_ctl/datapoints"
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if value : GPIO.output(light,GPIO.HIGH)
        else :  GPIO.output(light,GPIO.HIGH)
    else : #auto mode 
        endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/ledswitch/datapoints"
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if(value==1):
            if (now_time >=17 or now_time <= 5):
                print("light will turn on ")
                GPIO.output(light,GPIO.HIGH)
            else :
                GPIO.output(light,GPIO.LOW)
        else :
            if (now_time <=17 and now_time>=5):
                GPIO.output(light,GPIO.LOW)
def soil():
    endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/mode/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    display("soil_display")
    if value==True :
        endpoint = "/mcs/v2/devices/" + deviceId_client + "/datachannels/man_ctl/datapoints"
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if value : GPIO.output(watering,GPIO.HIGH)
        else :  GPIO.output(watering,GPIO.HIGH)
    else :
        endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/soil_switch/datapoints"
        url = host + endpoint
        r = requests.get(url,headers=headers)
        value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
        if(value==1):
            print("Soil Need Water!")
            music.play()
            GPIO.output(watering,GPIO.HIGH)
        else :
            print("Water is Enough")
            GPIO.output(watering,GPIO.LOW)

def display(sensor):
    endpoint = "/mcs/v2/devices/" + deviceId_host + "/datachannels/"+sensor+"/datapoints"
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