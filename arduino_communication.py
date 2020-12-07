import serial
import mcs_upload
mode= {
    'SOIL' : 0,
    'LDR' : 1 
    }
ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    for i in range(2):
        read_serial =int(ser.readline())
        if i == mode['SOIL'] :
            mcs_upload.get_data(read_serial,"soil_sensor")
            #print(read_serial)
        elif i == mode['LDR'] :
            mcs_upload.get_data(read_serial,"ldr_sensor1")
            #print(read_serial)
