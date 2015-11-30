# -*- coding: utf-8 -*-


#Napisz funkcję, która przyjmuje jako argument ciąg znaków i czym wyświetla co drugi z nich.

def zad01(s):
    print(s[::2])

#zad01(input('Podaj ciąg znaków: '))

import numpy as np

#The NumPy array is in general homogeneous (there is a special array type that is
#heterogeneous)—the items in the array have to be of the same type.
a = np.arange(5)
print(a.dtype)

#Many functions have a data type argument, which is often optional:
a = np.arange(5, dtype=np.uint8)

#Numpy na swoją listę typów: http://docs.scipy.org/doc/numpy-1.10.1/user/basics.types.html
#Konwersji typów można dokonać rzutując (dla liczb) lub używając funkcji (dla macierzy): http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.ndarray.astype.html
print(np.int8(42.0))
print(a.astype(np.bool))

#The record data type is a heterogeneous data type—think of it as representing a row in a
#spreadsheet or a database.
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
#Inne przykłady na stronie: http://docs.scipy.org/doc/numpy-1.10.0/reference/arrays.dtypes.html
#Można oglądać typy
print(t['name'])
#Przykład użycia:
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
print(itemz[1])


#Kształt (czyli wymiar) macierzy podawany jast za pomocą atrybutu (nie metody) zwracającej tuple:
print(a.shape)

#Wygodny sposób ma tworzenie wektorów wielkowymiarowych:
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)

#Podobnie działa funkcja np.zeros,http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.zeros.html
s = (2,2)
n = np.zeros(s)
print(n)

#Do tworzenie wielowymiarowych macierzy lub zmieniania ich wymiarów służy funkcja np.reshape(), http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.reshape.html.
b = np.arange(24).reshape(2,3,4)
print(b, b.shape)

#Aby zmienić wymiar (krztałt) macierzy można posłużyć się funkcjami:
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html
print(b.ravel())
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.ndarray.flatten.html
print(b.flatten())
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.ndarray.shape.html
b.shape = (6,4)
print(b)
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.resize.html
b.resize((2,12))
print(b)
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.transpose.html
print(b.transpose())

#Arrays can be stacked horizontally, depth-wise, or vertically. We can use, for that purpose,the np.vstack , np.dstack , np.hstack , np.column_stack , np.row_stack , and np.concatenate functions.

a = np.arange(9).reshape(3,3)
b = 2*a
print(a, '\n', b )
print(np.hstack((a,b)))
print(np.concatenate((a, b), axis=1)) #zauważmy, że tak samo działa jak powyżej
print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=0)) #zauważmy, że tak samo działa jak powyżej
#Pozostałe na stronach:
#http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.dstack.html
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html
#http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.ma.row_stack.html

#Arrays can be split vertically, horizontally, or depth wise. The functions involved are np.hsplit ,np.vsplit , np.dsplit , and np.split.

#Cwiczenie: Sprawdź działanie i spróbuj zrozumieć powyższych funkcji dla macieży 'a' i 'b'.

#Aby przemienić macierz numpy w zwykłą listę pythona możemy posłużyć się metodą tolist():
'''
a = np.arange(9).reshape(3,3)
print(a, a.shape)
a = a.tolist();
print(a); print(a.shape)
'''

#Do wgrywania zawartości pliku (odpowiednik open()) w numpy służy metoda np.loadtext(), http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
#Do zapisu (odpowiednik write()) służy metoda np.savetxt(), http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html

#Bardzo przydatną funkcją w praktyce okazje się np.linspace(), http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html.
#Dzięki niej można utworzyć listę liczb odzielonych a jakąć stałą wartość, np:
a = np.linspace(2.0, 3.0, num=5) #początek przedziału, koniec przedziału, 5 liczb w zadanym przedziale
print(a)

#Inne przydatne metody:
#np.eye(n) - tworzy macierz jednostkową o wymiarze n
#np.minimum(), np.maximum() minimalne i maxymoalne wartości macierzy, patrz.: dokumentacja


#Rozwiąż zadanie na mnożenie i wyznacznik macierzy ze strony http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach


#mnozeniemaciezy(np.array([[1,2,3],[1,2,4]]),np.array([[6,2],[1,2],[4,5]]))
#print(np.dot(np.array([[1,2,3],[1,2,4]]), np.array([[6,2],[1,2],[4,5]]))) #array  działa, lub
#print(np.array([[1,2,3],[1,2,4]]).dot(np.array([[6,2],[1,2],[4,5]])))
#print(np.matrix([[1,2,3],[1,2,4]]) * np.matrix([[6,2],[1,2],[4,5]])) #array nie działa

#print(wyznacznik(a)[0][0], np.linalg.det(a))

#Zadania dodatkowe:

#Utwórz macierz jednostkową 3x3.
#Wygeneruj macierz 10x10x10 liczb losowych. Uzyj metody rand() z bib. numpy


