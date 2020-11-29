import time
import board
import adafruit_dht
import time
import http.client, urllib
import json
import requests
import socket
import mcs_upload 
dht_device = adafruit_dht.DHT22(board.D20, use_pulseio = False)

try:
    print('press ctrl c to end the program')
    while True:
        try:
            t = dht_device.temperature
            h = dht_device.humidity
            if h is not None and t is not None:
                print('tempture={0:0.1f} C humidity={1:0.1f}%'.format(t, h))
                #i2c_lcd.message("tempture "+str(t)+"c",0,0)
                #i2c_lcd.message("humidity "+str(h)+"%",1,0,False)
                mcs_upload.get_data(t,"celsius")
        except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
            print("no detected!")
        # print(error.args[0])
        time.sleep(30)
except KeyboardInterrupt:
    print('close')
    #i2c_lcd.display_time()
