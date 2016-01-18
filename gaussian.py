#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import normpdf

mi, sigma = 100, 15
x = mi + sigma * np.random.randn(1000)

n, bins, patches = plt.hist(x, 50, normed=True, facecolor='g', alpha=0.75)

bincenters = 0.5 * (bins[1:] + bins[:-1])

y = normpdf(bincenters, mi, sigma)

l = plt.plot(bincenters, y, 'r--')

plt.show()

