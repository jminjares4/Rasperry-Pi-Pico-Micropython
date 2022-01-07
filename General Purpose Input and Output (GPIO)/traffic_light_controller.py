# Author: Jesus Minjares
# Master of Science in Computer Engineering
# Date 01-07-22

import machine
import utime
import _thread

# set leds as output, pin 13-15
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
# set button as input, pin 16
button = machine.Pin(16, machine.Pin.IN)
# set buzzer as output, pin 12
buzzer = machine.Pin(12, machine.Pin.OUT)

# create global variable
global button_pressed
button_pressed = False  # set to false

# button function
def button_reader_thread():
    global button_pressed  # recall global variable
    while True:  # loop
        if button.value() == 1:  # check if button has been pressed
            button_pressed = True  # update global variable


# create a thread for the button
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:  # check if the button has been pressed
        led_red.value(1)  # turn red led
        for i in range(10):  # iterate
            buzzer.value(1)  # turn on buzzer
            utime.sleep(0.2)  # 0.2 second
            buzzer.value(0)  # turn off buzzer
            utime.sleep(0.2)  # 0.2 second
        global button_pressed  # recall global variable
        button_pressed = False  # update global variable
    # turn traffic light sequence
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)
