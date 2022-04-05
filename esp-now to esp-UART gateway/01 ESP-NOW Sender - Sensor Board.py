import network
from esp import espnow
from machine import Pin, SoftI2C
from time import sleep
import htu21d

s = htu21d.HTU21D(22,21)
hum = s.humidity
temp = s.temperature * 1.8 + 32     #Converted to Fahrenheit
print('Hum: {:.2f}'.format(hum))
print('Temp: {:.2f}'.format(temp))

degree = str(b'\xc2\xb0', 'utf8')

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

#Initiate ESP-NOW
e = espnow.ESPNow()
e.init()
#Connect to Peer (Reciever)
peer = b'\xff\xff\xff\xff\xff\xff'   # MAC address of Reciever's wifi interface
e.add_peer(peer)

while True:
    e.send('Temperature:')       # Send to all peers
    e.send('Temp: {:.2f}'.format(temp))     #Send Temp
    e.send('Temp: {:.2f}'.format(hum))      #Send Humidity
    print('Message Sent...')                #Print Sent
    sleep(5)
