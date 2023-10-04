import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + led, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)

def dec2bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

def adc():
    arr = [0]*8
    for i in range(8):
        arr[i] += 1
        GPIO.output(dac, arr)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue:
            arr[i] -= 1
    ret = 0
    for i in range (8):
        ret += arr[7-i] * 2 ** i
    return ret

try:
    while(1):
        signal = adc()
        print(signal)
        for i in range(8):
            if (i + 1) / 8  > (signal + 1) / 256:
                GPIO.output(led[i], 1)
            else:
                GPIO.output(led[i], 0)

finally:
    GPIO.output(dac + led + [troyka], 0)
    GPIO.cleanup()