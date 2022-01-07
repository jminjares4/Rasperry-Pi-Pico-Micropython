# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# Use onboard temperature sensor at pin 4
sensor_temp = machine.ADC(4)
# convert 3.3v to analog
conversion_factor = 3.3 / (65535)

while True:
    # store reading of temperature sensor * conversion factor
    reading = sensor_temp.read_u16() * conversion_factor
    # convert analog reading to temperature
    temperature = 27 - (reading - 0.706)/(0.001721)
    print(temperature) # display temperature
    utime.sleep(2) # 2 second delay