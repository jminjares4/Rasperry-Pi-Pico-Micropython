# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set onboard led as output
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.value(1)  # turn on led
    utime.sleep(5)  # 5 second delay
    led_onboard.value(0)  # turon off led
    utime.sleep(5)  # 5 second delay
