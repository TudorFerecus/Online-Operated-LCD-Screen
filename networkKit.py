'''
THIS IS THE CLASS THAT HANDELS PICO'S CONECTIVITY WITH THE WI-FI, 
THE SOCKET'S CREATION AND THE WEBSITE'S FRONTEND
THIS SHOULD NOT BE CHANGED
'''


import network
import socket
from time import sleep
from machine import Pin
import constants


class NetworkKit:
    def __init__(self, ssid, password, innerHTML):
        self.ssid = ssid
        self.password = password
        self.innerHTML = innerHTML
        self.wlan = None
        self.max_wait = 20
        self.ipAdress = None
        self.s = None
        self.status = None
        self.addr = None
        self.initConnection()
    
    def initConnection(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        print('Waiting for connection')
        while self.max_wait > 10:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            self.max_wait -= 1    
            sleep(1)
        self.status = None
        if self.wlan.status() != 3:
            raise RuntimeError('Connections failed')
        else:
            self.status = self.wlan.ifconfig()
            print('connection to', self.ssid,'succesfull established!', sep=' ')
            print('IP-adress: ' + self.status[0])
        self.initSocket()
    
    def initSocket(self):
        self.ipAddress = self.status[0]
        self.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen(1)
    
    def getSocket(self):
        return self.s
    
    def getInnerHTML(self):
        return self.innerHTML