import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)

def dec2bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue != 0:
            return i
    return 255

try:
    while(1):
        print(round(adc() / 256 * maxVoltage, 2), "B")
finally:
    GPIO.output(dac + [troyka], 0)
    GPIO.cleanup()