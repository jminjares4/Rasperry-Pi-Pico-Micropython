# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set external led as output, pin 15
led_external = machine.Pin(15, machine.Pin.OUT)

while True:
    led_external.toggle()  # toggle led
    utime.sleep(5)  # 5 second delay
