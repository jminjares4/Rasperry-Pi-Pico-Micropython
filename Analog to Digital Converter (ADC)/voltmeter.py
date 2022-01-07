# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# Use pin 28 for ADC
potentiometer = machine.ADC(28)
# conversion factor for analog to digital
conversion_factor = 3.3 / (65535)

while True:
    # convert reading to voltage
    voltage = potentiometer.read_u16() * conversion_factor
    print(voltage)  # diplay voltage
    utime.sleep(2)  # 2 second delay
