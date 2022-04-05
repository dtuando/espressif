from machine import Pin 
from time import sleep
from machine import UART

import gc
gc.collect()

try:
  import usocket as socket
except:
  import socket

uart = UART(2, baudrate=9600, tx=17, rx=16)
msg = str(uart.read()).strip("b'\'")
# ESP32 Pin assignment 

t =""
h =""
########################################
def web_page():
  html = """<!DOCTYPE HTML><html><head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style> html { font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }
    h2 { font-size: 3.0rem; } p { font-size: 3.0rem; } .units { font-size: 1.2rem; } 
    .ds-labels{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
  </style></head><body><h2>ESP-Now --> UART Gateway to HTTP</h2>
    <p><i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="ds-labels">Temperature</span>
    <span id="temperature">""" + str(t) + """</span>
    <sup class="units">&deg;F</sup>
  </p>
    <p><i class="fa fa-percent"" style="color:#059e8a;"></i> 
    <span class="ds-labels">Humidty</span>
    <span id="humidity">""" + str(h) + """</span>
    <sup class="units">&#37;rH</sup>
  </p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def req():
    try:
        if gc.mem_free() < 102000:
              gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
##########################################

temp = "Temp"
hum = "Hum"              
while True:
    msg = str(uart.read()).strip("b'\'")
    if msg == "None":
        pass
    else:
        if temp in msg:
            t = str(msg).strip("Temp")
            print(str(msg))
        if hum in msg:
            h = str(msg).strip("Hum")
            print(str(msg))
        req()
        

