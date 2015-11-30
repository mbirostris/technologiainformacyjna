# -*- coding: utf-8 -*-


#Napisz funkcję, która przyjmuje jako argument ciąg znaków i czym wyświetla co drugi z nich.

def zad01(s):
    print(s[::2])

#zad01(input('Podaj ciąg znaków: '))


#Rozwiąż zadanie na mnożenie i wyznacznik macierzy ze strony http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach

import numpy as np

def mnozeniemaciezy(a,b):
    print(a,b)
    c = np.zeros((a.shape[0], b.shape[1]));
    for i in range(0, c.shape[0]):
        for j in  range(0, c.shape[1]):
            for k in range(0, a.shape[1]):
                c[i][j] += a[i][k]*b[k][j]
    print(c)

#mnozeniemaciezy(np.array([[1,2,3],[1,2,4]]),np.array([[6,2],[1,2],[4,5]]))


