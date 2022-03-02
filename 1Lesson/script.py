import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

while True:
    GPIO.output(2, GPIO.input(3))
    
    
