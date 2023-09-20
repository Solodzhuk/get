import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

outs = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(outs, GPIO.OUT)
for j in range(9):
    for i in range(8):
        GPIO.output(outs[i], 1)
        GPIO.output(outs[i-1], 0)
        time.sleep(0.1)

GPIO.output(outs, 0)
GPIO.cleanup()