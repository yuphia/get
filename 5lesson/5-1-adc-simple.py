import RPi.GPIO as gpio
import time as t

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode (gpio.BCM)

gpio.setup (dac, gpio.OUT, initial = gpio.LOW)
gpio.setup (troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup (comp, gpio.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]



def adc():
    for value in range (256):
        signal = decimal2binary(value)
        gpio.output (dac, signal)
        t.sleep(0.001
        )
        voltage =  value / 255 * 3.3
        
        comparatorValue = gpio.input(comp)

        if comparatorValue == 0:
            break

    
    print("ADC value = {:^3} -> {}, inputVoltage = {:.2f} compval = {}".format(value, signal, voltage, comparatorValue))

    return gpio.input(comp)

try:
    while True:
        comparatorValue = adc()        

finally:
    gpio.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    gpio.output(troyka, 0)
    gpio.cleanup()