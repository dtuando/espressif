from machine import Pin, SoftI2C
from time import sleep
from machine import UART

uart = UART(2, baudrate=9600, tx=17, rx=16)


while True:
    uart.write('Hello')
    print('Sent')
    sleep(5)



