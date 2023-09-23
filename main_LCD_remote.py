#The main file of the project, this is the one you should run in Thonny


from networkKit import NetworkKit
import network
import socket
from time import sleep
from machine import Pin
import constants
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime


ssid = constants.ssid
password = constants.wlan_password
innerHTML = constants.network_html
screenString = None
string_row_one = ''
string_row_two = ''

network = NetworkKit(ssid, password, innerHTML)
i2c = I2C(0, sda=machine.Pin(constants.I2C_SDA_PIN), scl=machine.Pin(constants.I2C_SCL_PIN), freq=400000)
lcd = I2cLcd(i2c, constants.I2C_ADDR, constants.I2C_NUM_ROWS, constants.I2C_NUM_COLS)
utime.sleep(2)
lcd.clear()


def put_to_screen(lcd, text_row_one, text_row_two):
        lcd.clear() 
        lcd.putstr(text_row_one)
        lcd.move_to(0, 1)
        lcd.putstr(text_row_two)

def parse_result(request):
    strCopy = ""
    result = request.find('_') + 1
    chrLen = request[11]
    screenString1= ""
    screenString2= ""
    if request[12] != '_':
        chrLen += request[12]
    for i in range(result, result+int(chrLen)):
        if request[i] == '_':
            strCopy += ' '
        else:
            strCopy += request[i]
    if len(strCopy) > 15:
        screenString1 = strCopy[0:16]
        screenString2 = strCopy[16:]
        print(screenString1)
    else:
        screenString1 = strCopy
        
    return screenString1, screenString2

while True:
    try:
        s = network.getSocket()
        cl, addr = s.accept()
        print('Connection from ', addr, "accepted!")
        request = cl.recv(1024)
        request = str(request)
        
        if request.find('/lcd') == 6:
            string_row_one, string_row_two = parse_result(request)
            

        put_to_screen(lcd,string_row_one, string_row_two)
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(network.getInnerHTML())
        cl.close()
    except OSError as e:
        cl.close()
        print('connection closed')
        
    
    
