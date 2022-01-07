# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set led as ouptut, pin 15
led_external = machine.Pin(15, machine.Pin.OUT)
# set button as input, pin 14
button = machine.Pin(14, machine.Pin.IN)

while True:
    if button.value() == 1:  # check if button has been pressed
        led_external.value(1)  # turn led on
        utime.sleep(2)  # 2 second delay
    led_external.value(0)  # turn off led
