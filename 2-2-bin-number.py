import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

outs = [8, 11, 7, 1, 0, 5, 12, 6]
num = 256
if num > 255:
    print("число вне области значений")
    number = '0'*8
else:
    number = (8 - len(bin(num)[2:])) * '0' + bin(num)[2:]
GPIO.setup(outs, GPIO.OUT)

for i in range(8):
    GPIO.output(outs[i], int(number[i]))

time.sleep(10)
GPIO.cleanup()
