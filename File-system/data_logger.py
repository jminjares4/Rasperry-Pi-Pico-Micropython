# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# use sensor temperature at the core
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

# conversion factor for analog to digital
conversion_factor = 3.3 / (65535)

# open file
file = open("temps.txt", "w")

while True:
    # store reading of temperature sensor * conversion factor
    reading = sensor_temp.read_u16() * conversion_factor
    # convert analog reading to temperature
    temperature = 27 - (reading - 0.706)/(0.001721)
    # write to file
    file.write(str(temperature) + "\n")
    file.flush()
    utime.sleep(10)  # 10 second delay
