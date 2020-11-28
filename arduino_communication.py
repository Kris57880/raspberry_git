import serial
import mcs_upload
mode= {
    'SOIL' : 1,
    'LDR' : 0 
    }
ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    for i in range(2):
        read_serial =int(ser.readline())
        if i == mode['SOIL'] :
            mcs_upload.get_data(read_serial,"soil_humidity")
            #print(read_serial)
        elif i == mode['LDR'] :
            mcs_upload.get_data(read_serial,"ldr")
            #print(read_serial)
