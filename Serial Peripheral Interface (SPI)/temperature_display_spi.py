# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set pin 2 to clock
spi_sck = machine.Pin(2)
# set pin 3 as tx
spi_tx = machine.Pin(3)
# set pin 4 as rx
spi_rx = machine.Pin(4)
# initilize spi at 100kps
spi = machine.SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_tx, miso=spi_rx)

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = adc.read_u16() * conversion_factor  # read adc
    # convert adc to temperature
    temperature = 25 - (reading - 0.706)/(0.001721)
    # write to device
    # 114 -> memory address of the device
    # 0x7C -> put into setting mode
    # 0x2D -> clear device
    spi.write('\x7C')
    spi.write('\x2D')
    # write temperature to device
    out_string = "Temp: " + str(temperature)
    spi.write(out_string)
    utime.sleep(2)  # 2 second delay
