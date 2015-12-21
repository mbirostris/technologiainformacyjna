# -*- coding: utf-8 -*-


#Uzupełnij klasę kwadrat/koło o metodę rysującą kwadrat/koło
import math
import numpy as np
import matplotlib.pyplot as plt

'''
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
'''


'''
import matplotlib.patches as patches
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D




'''
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('kometa.pdf')
#http://matplotlib.org/users/image_tutorial.html
import matplotlib.image as mpimg

#Wyjątki
