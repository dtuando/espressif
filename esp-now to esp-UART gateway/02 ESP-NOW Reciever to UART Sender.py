from machine import Pin, SoftI2C
from time import sleep
from machine import UART
import network
import ubinascii
from esp import espnow


w0 = network.WLAN(network.STA_IF)
w0.active(True)

#UART 
uart = UART(2, baudrate=9600, tx=17, rx=16)

#Get Mac Address
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print("MAC: " + mac)

#Initiate ESP-NOW
e = espnow.ESPNow()
e.init()
#Connecting to Peer (Sender)
peer = b'\xff\xff\xff\xff\xff\xff'   # MAC address of Senders wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        note = msg.decode()
        print(note)
        uart.write(note)
        print('Sent')
        sleep(1)
