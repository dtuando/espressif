import network
from esp import espnow
from machine import Pin, SoftI2C, sleep
import htu21d

s = htu21d.HTU21D(22,21)
hum = s.humidity
temp = s.temperature * 1.8 + 32
print('Hum: ', + hum)
print("Temp: {}".format(temp) + " F")

degree = str(b'\xc2\xb0', 'utf8')

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'\x08\x3a\xf2\x52\x75\xc8'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    e.send('Temperature:')       # Send to all peers
    e.send("{}".format(temp))
    e.send('Humidity:')       # Send to all peers
    e.send("{}".format(hum))
    sleep(5)
