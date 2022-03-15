import RPi.GPIO as gpio
import time

gpio.setmode (gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup (dac, gpio.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    print ("input a number in range 0-255")
    setupString = input()
    
    if (setupString == "q"):
        print("exiting")
        exit(0)
    
    setupNumbers = int (setupString)

    if (setupNumbers < 0 or setupNumbers > 255):
        print ("Value not in accepted range")
        exit(0)

    print (f"expected voltage: {(setupNumbers/255)*3.3}")
    gpio.output (dac, setupNumbers)
    time.sleep(1)

except ValueError:
    print ("Not an integer number in the input")

finally:
    gpio.output (dac, [0, 0, 0, 0, 0, 0, 0, 0])
    gpio.cleanup()