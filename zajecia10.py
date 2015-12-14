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

h = plt.contourf(X,Y,G)
#plt.show()

plt.imshow(G)
#plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, G, rstride=1, cstride=1, color='0.8', alpha=0.85, linewidth=1)  
#plt.show()

#Powtórz poprzednie zadanie dla większej liczby punktów, np. 10000. 

#Powtórz poprzednie zadanie dla funkcji sinus(X+Y) i tan(X+Y) (zamiast f.  gaussa)

X, Y = np.meshgrid(np.linspace(-1.5,1.5,100), np.linspace(-1.5,1.5,100))
D = np.sqrt(X*X+Y*Y)
#G = np.sin(X+Y)
G = np.tan(X+Y)
#print(G)


h = plt.contourf(X,Y,G)
#plt.show()

#plt.imshow(G)
#plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line = ax.plot_surface(X, Y, G, rstride=1, cstride=1, color='r', alpha=0.15, linewidth=1, label='saaa')
ax.set_xlabel(r'$\beta$')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
#plt.show()


# Dla wesji plot_surface()  podpisz osie, zmień kolor i styl punktów na siatce.

#------------------------------------
'''
#Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a fill value when necessary)
Z = np.random.randint(0,10,(10,10))
print(Z)
shape = (2,5)
fill  = 0
position = (2,6)

R = np.ones(shape, dtype=Z.dtype)*fill
P  = np.array(list(position)).astype(int)
Rs = np.array(list(R.shape)).astype(int)
Zs = np.array(list(Z.shape)).astype(int)
print(P, Rs, Zs, Rs)

R_start = np.zeros((len(shape),)).astype(int)
R_stop  = np.array(list(shape)).astype(int)
Z_start = (P-Rs//2)
Z_stop  = (P+Rs//2)+Rs%2
print(R_start, R_stop, Z_start, Z_stop)

R_start = (R_start - np.minimum(Z_start,0)).tolist()
Z_start = (np.maximum(Z_start,0)).tolist()
R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()
Z_stop = (np.minimum(Z_stop,Zs)).tolist()

r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]
R[r] = Z[z]
#print(Z)
#print(R)

####################
R = Z
Zy = list(range(0, position[0] - int(shape[0]/2)))+ list(range( position[0] + int(shape[0]/2) + shape[0]%2, Z.shape[0] ))
Zx = list(range(0, position[1] - int(shape[1]/2)))+ list(range( position[1] + int(shape[1]/2) + shape[1]%2, Z.shape[1] ))
R = np.delete(R, Zx, axis=1); R = np.delete(R, Zy, axis=0)
#print(R)
'''

#How to implement the Game of Life using numpy arrays ? 
def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
    print('\n', "AA\n", N)
    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    print('\n\n',Z[1:-1,1:-1])
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0 # to samo co Z[:,:] = 0, lub = Z = np.zeros(Z.shape[0], Z.shape[1]) czyli, że wszystko ma być zero: '...' = wszystko.
    print('\n', "BB\n", Z, "\n birth", birth, '\n\n\n' ,survive)
    Z[1:-1,1:-1][birth | survive] = 1
    return Z

Z = np.random.randint(0,2,(25,25))
for i in range(1):
    print(Z)
    Z = iterate(Z)

'''
#Given an arbitrary number of vectors, build the cartesian product (every combinations of every item)
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.asarray.html
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.indices.html
def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)
    print(arrays)
    print((shape))
    ix = np.indices(shape, dtype=int)
    print(ix)
    ix = ix.reshape(len(arrays), -1).T
    print(ix)
    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]
    return ix
print ([1, 2, 3], [4, 5], [6, 7],cartesian(([1, 2, 3], [4, 5], [6, 7])))
print(np.indices((3,2), dtype=int))
'''
