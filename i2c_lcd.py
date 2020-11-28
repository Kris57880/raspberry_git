
import sys
import time
import smbus
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574',address=0x27,port=1,backlight_enabled=True)
def message(msg,line=0,column=0,clearEnable=True):
        if clearEnable : 
            lcd.clear()
        lcd.cursor_pos=(line,column)
        lcd.write_string(msg)
        return 0        
def display_time():
    lcd.clear()
    try:
        while True:
            lcd.cursor_pos=(0,0)
            
            lcd.cursor_pos=(0,0)
            lcd.write_string("Date:{}".format(time.strftime("%y/%m/%d")))
            lcd.cursor_pos=(1,0)
            lcd.write_string("Time:{}".format(time.strftime("%H:%M:%S")))
            time.sleep(0.01)
    except KeyboardInterrupt:
        lcd.clear()
        lcd.cursor_pos=(0,0)
        lcd.write_string("BYE")
        time.sleep(3)
    finally:
        lcd.backlight_enabled=False
        lcd.clear()
    return 0
#lcd.write_string("HELLO!!")
#time.sleep(5)
#display_time()
