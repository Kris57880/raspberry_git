import time
import http.client, urllib
import json
import requests
import socket
import serial
import i2c_lcd
import mcs_get
#import mcs_ldr

#deviceId = "DxO0kY2u"
#deviceKey = "87oBeIFDtfZUuo2R"
#deviceId = "DmNwrsf9"
#deviceKey = "1y2bYSE70msD2nDL"
deviceId = "DweNqI3l" #109550172
deviceKey = "aNyIGaL6GdsJZxco"
# Set MediaTek Cloud Sand box (MCS) Connection
def post_to_mcs(payload):
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = http.client.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (http.client.HTTPException, socket.error) as ex:
            print ("Error: %s" % ex)
        time.sleep(1) # sleep 10 seconds
        conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
        response = conn.getresponse()
        print( response.status, response.reason,# json.dumps(payload),
        time.strftime("%c"))
        data = response.read()
        conn.close()
def get_data (data,mode):
    print(mode ,"=",data)
    #i2c_lcd.message(mode +":",0,0,True)
    #i2c_lcd.message(""+str(data),1,0,False)
    time.sleep(2)
    payload= {"datapoints":[{"dataChnId":mode,"values":{"value":str(data)}}]}
    post_to_mcs(payload)

    if mode == 'ldr':
        mcs_get.ldr()
    elif mode == 'soil_humidity':
        mcs_get.soil()
    time.sleep(1)
    