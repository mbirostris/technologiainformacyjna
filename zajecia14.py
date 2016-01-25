import numpy as np;
import matplotlib.pyplot as plt


#Zad1
class lis(object):
    def __init__(self, l):
        self.l = l
        self.cs = 'b-'

    def draw(self,a , b):
        t = np.linspace(-np.pi, np.pi, self.l);
        x = np.sin(a * t + np.pi/2)
        y = np.cos(b * t)
        plt.plot(x,y, self.cs)
        plt.show();

    def drawandsave(self,a , b):
        t = np.linspace(-np.pi, np.pi, self.l);
        x = np.sin(a * t + np.pi/2)
        y = np.cos(b * t)
        plt.plot(x,y)
        plt.title("Zadanie 1: a = 9, b = 8.")
        plt.savefig('zad1.png')

    def csc(self, c, s):
        self.cs = c+s


plot = lis(1000)
plot.csc('r', '_')
plot.drawandsave(9,8)
plt.close()

#Zad2
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import genfromtxt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax._axis3don = False
u = np.linspace(-10, 10, 100)
x, y = np.meshgrid(u, u)
nu, l = 6,1/24
z = np.sqrt(x ** 2  + y ** 2)
Z = -nu*z**2 +l*z**4
ax.plot_surface(x, y, Z, rstride=2, cstride=2, cmap=cm.coolwarm)
ax.set_title("Zadanie 2")
plt.savefig("zad2.png")



#Zad3
from sys import argv

data = np.genfromtxt(argv[1])
f, ax = plt.subplots(2, sharex=False)
ax[0].hist(data[:,2], 50, normed = True, facecolor='red', linewidth=3 )
ax[0].set_title('Zadanie 3')
ax[0].set_ylabel('Liczba przypadków')
ax[0].set_xlabel('Eta')
#plt.subplot(2, 1, 2)
styg = np.genfromtxt(argv[2])
#plt.plot(styg[:,0], styg[:,1])
ax[1].fill_between(styg[:,0], styg[:,1], np.min(styg[:,1]), facecolor='g')
ax[1].set_ylim([np.min(styg[:,1]), np.max(styg[:,1])])
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
ax[1].yaxis.set_ticks_position('left')
ax[1].xaxis.set_ticks_position('bottom')
ax[1].set_xlabel('Czas (s)')
ax[1].set_ylabel(r'Temeratura ($^o$C)')
plt.savefig("zad3.png")

