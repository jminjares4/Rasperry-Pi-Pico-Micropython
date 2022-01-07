# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime
import urandom
# set led as output, pin 15
led = machine.Pin(15, machine.Pin.OUT)
# set button as input, pin 14
button = machine.Pin(14, machine.Pin.IN)

# button IRQ handler


def button_handler(pin):
    button.irq(handler=None)  # set handler to None
    # capture time difference
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    # display time difference
    print("Your reaction time was " + str(timer_reaction) + " milliseconds!")


led.value(1)  # turn on led
utime.sleep(urandom.uniform(5, 10))  # get random sleep
led.value(0)  # turn off led
timer_start = utime.ticks_ms()  # start timer
# attach button to IRQ handler as rising edge
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
