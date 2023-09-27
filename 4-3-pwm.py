import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) 

p = GPIO.PWM(24, 1000)
p.start(0)
try:
    while(1):
        n0 = input("0-255 ")

        if n0 == 'q':
            raise KeyboardInterrupt()

        if 1 - isinstance(float(n0), (int, float)):
            print("Not a number")
        elif 1 - isinstance(int(n0), int):
            print("Not an integer")        
        else:
            n = int(n0)
            if n < 0:
                print("Negative number")
            elif n  > 100:
                print("Input value out of range")

            else:
                p.ChangeDutyCycle(n)
                print('{:.2f}'.format(0.033 * n, "B"))
finally:
    p.stop
    GPIO.cleanup()
