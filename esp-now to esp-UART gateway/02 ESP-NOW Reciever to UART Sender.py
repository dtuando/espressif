from machine import Pin, SoftI2C
from time import sleep
from machine import UART
import network
import ubinascii
from esp import espnow

w0 = network.WLAN(network.STA_IF)
w0.active(True)
uart = UART(2, baudrate=9600, tx=17, rx=16)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print("MAC: " + mac)

e = espnow.ESPNow()
e.init()
peer = b'\xe0\xe2\xe6\xd0\x1b\xf4'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        note = msg.decode()
        print(note)
        uart.write(note)
        print('Sent')
        sleep(5)




