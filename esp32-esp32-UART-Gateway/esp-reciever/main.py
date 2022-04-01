from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from machine import UART

uart1 = UART(2, baudrate=9600, tx=17, rx=16)
# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Starting...', 0, 32)
        
oled.show()

while True:
    # write 5 bytes
    msg = str(uart1.read()).strip("b'\'")
    stop = "Bye"
    print(str(msg))
    sleep(5)
    oled.fill(0)
    oled.text(str(msg), 0, 20)
    oled.show()
    if str(stop) in str(msg):
        oled.fill(0)
        oled.text("Bye!")
        oled.show()

