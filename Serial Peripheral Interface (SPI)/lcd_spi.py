# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine

# set pin 2 to clock
spi_sck = machine.Pin(2)
# set pin 3 as tx
spi_tx = machine.Pin(3)
# set pin 4 as rx
spi_rx = machine.Pin(4)
# initilize spi at 100kps
spi = machine.SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_tx, miso=spi_rx)

# write to device
# 114 -> memory address of the device
# 0x7C -> put into setting mode
# 0x2D -> clear device
spi.write('\x7C')
spi.write('\x2D')
# write string to device
spi.write("Hello world")
