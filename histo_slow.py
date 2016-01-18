#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from sys import argv

f = open(argv[1])
l = []
for line in f:
  l.append(len(line.strip('\n')))
f.close()
dl = np.array(l, dtype=np.int)
print(dl)
print('statystyki pliku {}:'.format(argv[1]))
print('liczba linii: {}'.format(len(dl)))
print('maksymalna: {}, minimalna: {}, średnia: {}, mediana: {}'.
      format(dl.max(), dl.min(), dl.mean(), np.median(dl))
      )
plt.hist(dl, bins=(dl.max()-dl.min()+1), color='green')
plt.title('rozkład długosci linii w pliku {}'.format(argv[1]))
plt.xlabel('długosc słowa')
plt.ylabel('czestosc')
plt.show()

