#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2.0, 0.01)
y1 = np.sin(2.0*np.pi*x)
y2 = np.cos(2.0*np.pi*x)
y = y1 * y2
#l1 = plt.plot(x, y, 'b')
l1, l2, l3 = plt.plot(x, y, 'b', x, y1, 'r--', x, y2, 'g')
plt.legend((l2, l3, l1), ('y1', 'y2', 'y1*y2'))
plt.xlabel('czas')
plt.ylabel('pozycja')
plt.title('wykres paru funkcji trygonometrycznych')
plt.grid(True)
plt.xticks(np.arange(0.0, 2.0, 0.2))
#plt.show()
plt.savefig('trygo.png')
