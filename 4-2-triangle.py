import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT) 


def dec2bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

try:
    count = 0
    period = int(input())
    while(1):      
        if count % 256 == count % (2 * 256):
            voltage = count % 256
        else:
            voltage = 255 - count % 256
        for i in range(8):
            GPIO.output(dac[i], dec2bin(voltage)[i])
        print(voltage)
        count += 1
        time.sleep(period / 2 / 256)

finally:
    GPIO.cleanup()