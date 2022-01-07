# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime
# set inputs
sensor_pir = machine.Pin(28, machine.Pin.IN)
sensor_pir2 = machine.Pin(22, machine.Pin.IN)
# set outputs
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

# interrupt handler
def pir_hanlder(pin):
    if pin is sensor_pir:  # check for sensor 1
        print("ALARM! Motion detected in bedroom!")
    elif pin is sensor_pir2:  # check for sensor 2
        print("ALARM! Motion detected in living room!")
    for i in range(50):  # iterate
        # toggle led and buzzer for 100ms * 50 -> 5 seconds
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)


# attach IRQ handler as rising edge
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
sensor_pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()  # toggle led
    utime.sleep(5)  # 5 second delay
