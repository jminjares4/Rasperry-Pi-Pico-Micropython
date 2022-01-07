# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# set input
sensor_pir = machine.Pin(28, machine.Pin.IN)
# set output
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

# IRQ handler
def pir_handler(pin):
    print("ALARM! Motion detected!")  # display message
    for i in range(50):  # iterate
        buzzer.toggle()  # toggle buzzer
        utime.sleep_ms(3)  # 3 ms delay

# attach IRQ handler as rising edge
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()  # toggle led
    utime.sleep(5)  # 5 second delay
