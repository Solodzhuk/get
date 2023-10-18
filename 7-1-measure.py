import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 1)

def dec2bin(a):
    # перевод в двоичную систему
    return [int(element) for element in bin(a)[2:].zfill(8)]

def adc():
    # функция измерения напряжения на конденсаторе с помощью АЦП
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
    initialTime = time.time()
    previousTime = initialTime # меряем начальное время

    valueList = []
    timeList = []

    midtime = 0
    adcValue = adc()
    while(1):
        newAdcValue = adc()
        if newAdcValue == adcValue:
            if time.time() - previousTime > 3: # значения не меняются 3 секунды начинаем вторую часть эксперимента
                GPIO.output(troyka, 0)
                if midtime == 0:
                    midtime = time.time() # меряем время конца 1 части эксперимента
                else:
                    break # заканчиваем измерения
        else:
            adcValue = newAdcValue
            previousTime = time.time()
        print(adcValue)
        valueList.append(adcValue * 3.3 / 255) # запись измерений в списки
        timeList.append(round(previousTime - initialTime, 5))

        
finally:
    GPIO.output(dac + [troyka], 0) # гасим плату
    GPIO.cleanup()

    finalTime = time.time() # измерение времени конца эксперимента

    plt.plot(timeList, valueList) # строим график
    with open("data.txt", "w") as f: # запись точек в файл
        for i in range(len(valueList)):
            f.write(str(valueList[i]) + " " + str(timeList[i]) + "\n")
    
    with open("settings.txt", "w") as f: # запись параметров АЦП в файл
        f.write(str(len(timeList) / timeList[len(timeList - 1)]) + "\n" + str(round(3.3 / 255, 5)))
    
    # вывод характеристик эксперимента в терминал
    print("Время эксперимента " + str(round(finalTime - initialTime, 5)) + "\n" + "T1 " + str(round(midtime - initialTime, 5)) + " T2 " + str(round(finalTime - midtime, 5)))
    print("Ср. частота дискретизации " + str(round(len(timeList) / timeList[len(timeList - 1)], 5)) + "\n" + "Шаг квантования АЦП " + str(round(3.3 / 255, 5)))

    plt.show() #показываем график