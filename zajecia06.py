
# -*- coding: utf-8 -*-

# Zdefiniuj funkcj? która wy?wietla s?ownik, w którym kluczami s? liczby od 1 do 3 w??cznie a warto?ciami s? pierwiastki tych liczb
from math import sqrt, sin, pi

def slowv1():
    d = dict()
    d[1] = sqrt(1)
    d[2] = sqrt(2)
    d[3] = sqrt(3)
    print(d)

#slowv1()

#Zdeniuj funkcj? która wy?wietla s?ownik, gdzie kluczam s? pliczby od 1 do 20, a warto?ci sinusy tych liczb
def slowv2():
    d = dict()
    for i in range(1,21):
        d[i] = sin(i)
    return d;

#slowv2()
#Zrób co wy?ej, ale niech funkcja wy?wietla tylko warto?ci (bez kluczy). Wsk: u?yj keys() lub items()

def slowv3():
    for i in slowv2().keys():
        print(slowv2()[i])
    print(slowv2().keys())
    print(slowv2().items())

def slowv4():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():	
        print(v)
#slowv4()

#Zrób co wy?ej, ale niech funkcja wy?wietla tylko klucze. Wsk: u?yj keys() lub item()

def slowv5():
    for i in slowv2().keys():
        print(i)

def slowv6():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():	
        print(k)

#slowv6()


#Zdefiniuj funkcj? generuj?c? list? warto?ci b?d?cych kwadratami liczb od 1 do 20 (w??cznie)

def listav1():
    li = []; i = 1;
    while i <= 20:
        li.append(i*i)
        i+=1;
    return li

def listav2():
    li=list()
    for i in range(1,21):
        li.append(i)
    return li

#print(listav1())
#print(listav2())
#Korzystaj?c z poprzedniego rozwi?zania napisz funkcj?, która zwraca pierwszych 5 elementów listy z powy?szego zadania.

def printlistav1(a):
    print(a[:5])

#printlistav1(listav2())

#Powtórz powy?sze zadanie dla ostatnich 5 warto?ci:

def printlistav2(a):
    print(a[-5:])

#printlistav2(listav2())


#Zdefiniuj funkcj? generuj?c? tuple której warto?ciami s? liczy od 1 do 20:

def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    return tuple(li)

#print(printTuple())

#Napiz program generuj?cu i wy?witlaj?cy tupl?, której warto?ciami s? liczby parzyste od 1 do 20

def printTupleeven():
    li=list()
    for i in range(1,21):
        if i%2 == 0:
            li.append(i)
    return tuple(li)

def printTupleevenv2():
    li=list()
    for i in range(2,21,2):
        li.append(i)
    return tuple(li)

#print(printTupleeven())


#Napisz funkcj?, która filtruje liczby parzyste z listy. Skorzystaj z funkcji wbudowanej filter() i funkcji lambda.
#https://docs.python.org/2/library/functions.html#filter
#http://www.secnetix.de/olli/Python/lambda_functions.hawk
#https://docs.python.org/3.0/whatsnew/3.0.html
#http://www.secnetix.de/olli/Python/list_comprehensions.hawk

def flparzv3():
    li = listav2()
    return filter(lambda x : x%2==0, li )

def flparzv1():
    li = [1,2,3,4,5,6,7,8,9,10]
    evenNumbers = filter(lambda x: x%2==0, li)
    return evenNumbers;
#lub
def flparzv2():
    return filter(lambda x: x%2==0, range(1,21))

#print(flparzv1()) #python3 zwraca iteratory
#print(flparzv2()) #python3 zwraca iteratory
#print(list(flparzv1())) 
#print([i for i in flparzv2()])

#Napisz funkcj? korzystaj?c? z funkji budowanej map() i zrwacjaca list? elementów b?d?cych kwadratami parzystych liczb od 1 do 99:
def lll(x):
    return x**2

def lfmapkwv1():
    return map(lll, filter(lambda x: x%2==0, range(1,100)))

def lfmapkwv2():
    return map(lambda x : x**2, filter(lambda x: x%2==0, range(1,100)))

#print((lfmapkwv1()))

#http://brain.fuw.edu.pl/edu/index.php/TI/Numpy
#http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach
import numpy as np


#Napisz funkcj? obliczaj?c? ?lad macierzy. 

A = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

#print(np.matrix(A))
#print(A)

def sladmacierzy(A):
    a,b = np.shape(A)
    tr = 0;
    for i in range(0,a):
        tr += A[i][i]
    return tr;

#print(sladmacierzy(A))
#print(np.trace(A))


#Napisz funkcj? transponuj?c? macierz kwadratow? w miejscu, czyli bez tworzenia nowej macierzy, poprzez zamian? elementów parami. 


def macierzodwrotna(A):
    print(A)
    a,b = np.shape(A)
    i = 0;
    while i < int(a/2 + 1):
        for j in range(0,b):
            A[i][j], A[j][i] = A[j][i], A[i][j]
        i+=1;
    print(A)
#macierzodwrotna(A)


#Napisz funkcj? która zwróci transponowan? macierz, niekoniecznie kwadratow?.
#U?yj funkcji numpy.empty do stworzenia macierzy wynikowej, a nast?pnie wype?nij ja w p?tli. 

def macierzodwrotnav2(A):
    print(A)
    a,b = np.shape(A)
    B = np.empty([a, b])
    for i in range(0,a):
        for j in range(0,b):
            B[i][j] = A[j][i]
    print(B)


macierzodwrotnav2(A)
#print(np.transpose(A))




