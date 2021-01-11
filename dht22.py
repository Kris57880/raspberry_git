import time
import board
import adafruit_dht
import time
import datetime
import http.client, urllib
import json
import requests
import socket
import mcs_upload
import pymysql
import os

dht_device = adafruit_dht.DHT22(board.D20, use_pulseio = False)

try:
    print('press ctrl c to end the program')
    while True:
        aa=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            t = dht_device.temperature
            h = dht_device.humidity
            if h is not None and t is not None:
                print('temperature={0:0.1f} C humidity={1:0.1f}%'.format(t, h))
                #i2c_lcd.message("tempture "+str(t)+"c",0,0)
                #i2c_lcd.message("humidity "+str(h)+"%",1,0,False)
                mcs_upload.post_data(t,"celsius")
                conn= pymysql.connect(
                host='localhost',
                port = 3306,
                user='root',
                passwd='12345',
                db ='sensor_database',
                )
                cur = conn.cursor()
                # cur.execute("creat table if not exists temp(time int,temperature int,humidity int)")
                cur.execute("insert into temp_and_humid values('%s','%f','%f')"%(aa,t,h))
                conn.commit()
                
        except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
            print("no detected!")
        # print(error.args[0])
        time.sleep(60)
except KeyboardInterrupt:
    cur.close()
    conn.close()
    print('close')
    #i2c_lcd.display_time()
