# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# Use pin 26 for ADC
potentiometer = machine.ADC(26)

while True:
    # Display analog reading
    print(potentiometer.read_u16())
    utime.sleep(2)  # 2 second delay
