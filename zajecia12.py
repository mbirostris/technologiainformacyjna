# -*- coding: utf-8 -*-


#Uzupełnij klasę kwadrat/koło o metodę rysującą kwadrat/koło
import math
import numpy as np
import matplotlib.pyplot as plt

#http://matplotlib.org/api/patches_api.html
#http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.gca

import matplotlib.patches as patches
class Kwadrat(object):

    def __init__(self, bok):
        self.bok = bok 
        
    def pole(self):
        return self.bok ** 2
        
    def obwod(self):
        return self.bok * 4

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        ax.set_xlim([0, self.bok + 0.1*self.bok])
        ax.set_ylim([0, self.bok + 0.1*self.bok])
        ax.add_patch(
            patches.Rectangle(
                (0, 0),   # (x,y)
                self.bok,          # width
                self.bok,          # height
            )
        )
        return fig;
        

class Kolo(object):

    def __init__(self, promien):
        self.promien = promien
        
    def pole(self):
        return math.pi * self.promien ** 2
        
    def obwod(self):
        return 2 * math.pi * promien
 
    def draw(self):
        circle2=plt.Circle((.5,.5),self.promien,color='b')
        fig = plt.gcf()
        fig.gca().add_artist(circle2)
        plt.xlim([-self.promien - 0.1*self.promien, self.promien + 0.1*self.promien])
        plt.ylim([-self.promien - 0.1*self.promien, self.promien + 0.1*self.promien])
        return fig


a = Kolo(30);
fig = a.draw();
plt.show()
b = Kwadrat(2)
fig1 = b.draw();
plt.show()




'''
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# Calculate spiral coordinates for the Xmas tree
theta = np.linspace(-8 * np.pi, 8 * np.pi, 200) 
z = np.linspace(-3, 0, 200)
r = 5
x = r * np.sin(theta)*z
y = r * np.cos(theta)*z
print(z)

# Use matplotib and its OOP interface to draw it 
fig = plt.figure() # Create figure
ax = fig.gca(projection='3d') # It's a 3D Xmas tree!
#ax.view_init(15, 0) # Set a nice view angle
#ax._axis3don = False # Hide the 3d axes

# Plot the Xmas tree as a line
ax.plot(x, y, z,c='green', linewidth=2.5)

# Every Xmas tree needs a star
#http://matplotlib.org/api/axes_api.html + do scatter
#ax.scatter(0, 0, 0.2, c='red', s=251, marker='*')

# Type here your best whishes
#ax.set_title("Merry Christmas")
plt.show()
'''


'''
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('kometa.pdf')
#http://matplotlib.org/users/image_tutorial.html
import matplotlib.image as mpimg
img=mpimg.imread('comet.png')

plt.imshow(img)


#invert colors
img = img[:,:,0]
#zmień naświtlenie
imgfig = plt.imshow(img, cmap="hot")
#to samo ale po zdefiniowaniu obrazka
imgfig.set_cmap('spectral')
#dodanie skali
plt.colorbar()

#zapis do pliku - jak rysujemy to wykomentowujemy albo przenosimy na koniec 'plt.show()'
plt.draw()
pp.savefig()
pp.close()
plt.show()
'''


#Wyjątki
