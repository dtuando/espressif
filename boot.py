#FOR ESP_NOW and WIFI
import network
from time import sleep

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)

sta_passw = 'CHANGEME'
sta_essid = 'CHANGEME'
ap_essid = 'CHANGEME'
#ap_channel =int(7) #channel number here

def ap_sta():
    if ap_if.active() == True:
        if sta_if.active() == True:
            sta_if.connect(sta_essid, sta_passw)
            print('Connecting Please Wait ...')
            sleep(5)

while True:
    if sta_if.isconnected():
        ap_if.config(essid=ap_essid)
        #ap.config(channel=ap_channel)
        print('AP SSID &  Channel Updated!')
        print('STA ifconfig:', sta_if.ifconfig())
        print('AP_ifconfig:', ap_if.ifconfig())
        break
    else:
        sleep(5)
        ap_sta()
        pass
