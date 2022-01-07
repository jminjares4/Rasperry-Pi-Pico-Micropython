# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime

# use pin 28 to read ADC
potentiometer = machine.ADC(28)
# attach pin 15 to PWM
led = machine.PWM(machine.Pin(15))
# set pwm to 1Khz
led.freq(1000)

while True:
    # update led based on adc reading
    led.duty_u16(potentiometer.read_u16())
