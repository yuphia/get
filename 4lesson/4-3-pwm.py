import RPi.GPIO as gpio
import time

gpio.setmode (gpio.BCM)
pwm_out = 22
gpio.setup(pwm_out, gpio.OUT)
pwm = gpio.PWM(pwm_out, 1000)

duty = 0

try:
    while True:
        duty = int(input())
        pwm.start (duty)
        time.sleep (2)
        pwm.stop ()        
        
finally:
    gpio.cleanup()