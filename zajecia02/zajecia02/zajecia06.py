
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

slowv2()
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

slowv6()


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
        li.append(i**2)
    return li

print(listav1())
print(listav2())
#Korzystaj?c z poprzedniego rozwi?zania napisz funkcj?, która zwraca pierwszych 5 elementów listy z powy?szego zadania.


#Powtórz powy?sze zadanie dla ostatnich 5 warto?ci:



#Zdefiniuj funkcj? generuj?c? tuple której warto?ciami s? liczy od 1 do 20:


#Napiz program generuj?cu i wy?witlaj?cy tupl?, której warto?ciami s? liczby parzyste od 1 do 20



#Napisz funkcj?, która filtruje liczby parzyste z listy. Skorzystaj z funkcji wbudowanej filter() i funkcji lambda.
#https://docs.python.org/2/library/functions.html#filter
#http://www.secnetix.de/olli/Python/lambda_functions.hawk
#https://docs.python.org/3.0/whatsnew/3.0.html
#http://www.secnetix.de/olli/Python/list_comprehensions.hawk



#Napisz funkcj? korzystaj?c? z funkji budowanej map() i zrwacjaca list? elementów b?d?cych kwadratami liczb od 1 do 99:



#http://brain.fuw.edu.pl/edu/index.php/TI/Numpy
#http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach

#Napisz funkcj? obliczaj?c? ?lad macierzy. 


#Napisz funkcj? transponuj?c? macierz kwadratow? w miejscu, czyli bez tworzenia nowej macierzy, poprzez zamian? elementów parami. 


#Napisz funkcj? która zwróci transponowan? macierz, niekoniecznie kwadratow?.
#U?yj funkcji numpy.empty do stworzenia macierzy wynikowej, a nast?pnie wype?nij ja w p?tli. 




