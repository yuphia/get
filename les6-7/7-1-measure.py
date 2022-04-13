import RPi.GPIO as gpio
import time as t
import matplotlib.pyplot as plot

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

measurments = []

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
        t.sleep(0.001)
        voltage =  value / 255 * 3.3
        
        comparatorValue = gpio.input(comp)
        
        #gpio.output (leds, signal)

        if comparatorValue == 0:
            break

    
    print("ADC value = {:^3} -> {}, inputVoltage = {:.2f} compval = {}".format(value, signal, voltage, comparatorValue))

    return voltage

def troyka_voltage():
    return gpio.output(troyka)

try:
    #gpio.output(troyka, 0)
    #t.sleep(5)
    gpio.output (troyka, gpio.HIGH)
    time_start = t.time()
    while adc() < 3.3*99/100:
        voltage = adc()
        measurments.append(voltage)

    gpio.output (troyka, 0)
    while adc() > 3.3*2/100:
        voltage = adc()
        measurments.append(voltage)

    time_finish = t.time()

finally:
    plot.plot (measurments)
    plot.show()
    
    measurments_str = [str(item) for item in measurments]
    with open ("data.txt", "w") as outfile:
        outfile.write ("\n".join(measurments_str))
        
    exp_time = time_finish - time_start
    print(exp_time)


    gpio.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    gpio.output(troyka, 0)
    gpio.cleanup()