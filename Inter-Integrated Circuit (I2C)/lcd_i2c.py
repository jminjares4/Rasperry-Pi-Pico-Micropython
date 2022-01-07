# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
# set sda to pin 0
sda = machine.Pin(0)
# set scl to pin 1
scl = machine.Pin(1)
# initialize i2c at 400Khz
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

# write to device
# 114 -> memory address of the device
# 0x7C -> put into setting mode
# 0x2D -> clear device
i2c.writeto(114, '\x7C')
i2c.writeto(114, '\x2D')
# write string to device
i2c.writeto(114, "hello world")
