import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from textwrap import wrap
import matplotlib as mpl

with open('settings.txt', 'r') as f:
       vMin, tMin = f.readlines()
       vMin = np.float_(vMin)
       tMin = np.float_(tMin)

with open('data.txt', 'r') as f:
       data = np.int_(np.array(f.readlines())) * vMin


fig, ax = plt.subplots(figsize=(8, 6))
ax.annotate('Время разрядки = ' + str(round(np.argmax(data) * tMin, 4)) + ' с', [len(data) * tMin * 4 / 7, max(data) * 2 / 3])
ax.annotate('Время зарядки = ' + str(round((len(data) - np.argmax(data)) * tMin, 4)) + ' с', [len(data) * tMin * 4 / 7, max(data) * 2 / 3 - 0.5])
ax.plot(np.arange(len(data)) * tMin, data, label='V(t)', c='b', markevery=50, marker=mpl.markers.MarkerStyle("o"))
ax.grid()
ax.minorticks_on()
ax.grid(which='minor', ls='--')

ax.set_xlim([0, ceil(len(data) * tMin)])
ax.set_ylim([0, ceil(max(data) * 2)/2])

ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.set_title('\n'.join(wrap('Процесс заряда и разряда конденсатора в RC-цепочке', 60)), loc='center')
ax.legend()
plt.savefig("inj8.svg", bbox_inches='tight')

plt.show()
