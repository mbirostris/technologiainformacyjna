import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import genfromtxt


my_data = genfromtxt('plik.csv', delimiter=',')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')

ax.plot(my_data[:,0], my_data[:,1], my_data[:,2], c='g')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()

