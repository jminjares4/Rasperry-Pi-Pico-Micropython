# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set sda to pin 0
sda = machine.Pin(0)
# set scl to pin 1
scl = machine.Pin(1)
# initialize i2c at 400Khz
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

# use pin 4 as ADC
adc = machine.ADC(4)
# use conversion factor to convert analog to digital
conversion_factor = 3.3 / (65535)

while True:
    reading = adc.read_u16() * conversion_factor  # read adc
    # convert adc to temperature
    temperatur = 25 - (reading - 0.706)/(0.001721)
    # write to device
    # 114 -> memory address of the device
    # 0x7C -> put into setting mode
    # 0x2D -> clear device
    i2c.writeto('\x7C')
    i2c.writeto('\x2D')
    # write temperature to device
    out_string = "Temp: " + str(temperature)
    i2c.writeto(114, out_string)
    utime.sleep(2)  # 2 second delay
