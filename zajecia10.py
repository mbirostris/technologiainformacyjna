
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#Zad Uwórz macierz 10x2 losowych liczb. Niech macierz to reprezentuje zbior punktów w układzie kartezjańskim; przekonwertuj te punkty do układu biegunowego.

Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
#print(R)
#print(T)

#Zad. Dla macierzy z powyższego zadania znajdź odległości między punktami (w ukł. kartezjańskim).
#Wsk: http://docs.scipy.org/doc/numpy/reference/generated/numpy.atleast_2d.html
D = np.sqrt( (X-np.roll(X,1))**2 + (Y-np.roll(Y,1))**2)
#print(D)

#mazierz 10x10 z odleglosciamy dla kazdej kombnacji pk.
X,Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
#print(D)


#Wygeneruj 10x10 elementową macierz Gaussowską 2D z zakresie -1,1.  
#(wsk: http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html)
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
#print(G)

#Korzystając z pakietu matplotlib  narysuj punkty z poprzedniego zadania: 
#a) korzystając z funkcji contour
#b) korzystając z imshow
#c) korzystając z plot_surface


#Powtórz poprzednie zadanie dla większej liczby punktów, np. 10000. 

#Powtórz poprzednie zadanie dla funkcji sinus(X+Y) i tan(X+Y) (zamiast f.  gaussa)

from mpl_toolkits.mplot3d import Axes3D


# Dla wesji plot_surface()  podpisz osie, zmień kolor i styl punktów na siatce.

#------------------------------------

#Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a fill value when necessary)

#How to implement the Game of Life using numpy arrays ? 

#Given an arbitrary number of vectors, build the cartesian product (every combinations of every item)

