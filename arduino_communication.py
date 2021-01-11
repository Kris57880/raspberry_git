import serial
import mcs_upload
import time
mode= {
    'AIR':0,
    'SOIL' :2,
    'LDR' :1
    }
ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    for i in range(3):
        read = ser.readline()
        if i== mode['AIR'] :
            read_serial =float(read[0:-2])
            mcs_upload.post_data(read_serial,"air")
            time.sleep(1)
        elif i == mode['SOIL'] :
            read_serial =int(read[0:-2])
            mcs_upload.post_data(read_serial,"soil_sensor")
            #print(read_serial)
        elif i == mode['LDR'] :
            read_serial =int(read[0:-2])
            mcs_upload.post_data(read_serial,"ldr_sensor1")
            #print(read_serial)
    