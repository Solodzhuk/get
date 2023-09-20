import RPi.GPIO as GPIO
import time
try:
    GPIO.setmode(GPIO.BCM)

    outs = [2, 3, 4, 17, 27, 22, 10, 9]
    GPIO.setup(outs, GPIO.OUT)
    ins = [21, 20, 26, 16, 19, 25, 23, 24]
    GPIO.setup(ins, GPIO.IN)

    while(True):
        for i in range(8):
            GPIO.output(outs[i], GPIO.input(ins[i]))
        time.sleep(0.1)
finally:
    GPIO.cleanup()