import RPi.GPIO as gpio
import time

gpio.setmode (gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup (dac, gpio.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    sleep = int(input())
    currentValue = 0
    signedOne = 1
    while True:
        if (currentValue > 255 or currentValue < 0):
            signedOne *= -1
            currentValue += signedOne
            

        gpio.output (dac, dec2bin(currentValue))

        print (currentValue)
        currentValue += signedOne

        time.sleep(sleep/(255*2))

finally:
    gpio.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    gpio.cleanup()