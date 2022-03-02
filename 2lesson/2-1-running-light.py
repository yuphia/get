import RPi.GPIO as gpio
import time 

leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.setmode (gpio.BCM)
gpio.setup (leds, gpio.OUT)

j = 0

while j < 3:
    j = j+1
    for i in range (8):
        gpio.output (leds[i], 1)
        time.sleep (0.2)
        gpio.output (leds[i], 0)

gpio.output (leds, 0)

gpio.cleanup()