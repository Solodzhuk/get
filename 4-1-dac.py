import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]
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
            elif n  > 255:
                print("Input value out of range")

            else:
                print("V = {:.4f}".format(3.3 / 256 * n), 'B')
                for i in range(8):
                    GPIO.output(dac[i], dec2bin(n)[i])

finally:
    GPIO.cleanup()