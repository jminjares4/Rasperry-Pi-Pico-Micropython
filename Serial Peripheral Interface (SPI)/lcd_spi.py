import machine

spi_sck = machine.Pin(2)
spi_tx = machine.Pin(3)
spi_rx = machine.Pin(4)

spi = machine.SPI(0,baudrate=100000, sck=spi_sck, mosi=spi_tx, miso=spi_rx)
spi.write('\x7C')
spi.write('\x2D')
spi.write("Hello world")
