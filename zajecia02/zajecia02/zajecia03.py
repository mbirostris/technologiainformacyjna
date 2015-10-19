import os

#import math
#from math import pi
import math as m

#Proszę napisać program do obliczania pola i obwodu koła. 

def wheelvolume(radius):
    return m.pi*int(radius)**2

def wheelcirkumference(radius):
    return 2*m.pi*radius;

#print('Pole kola: ', wheelvolume(2))
#print('Obwod kola: ', wheelcirkumference(4))

#Zadania z http://brain.fuw.edu.pl/edu/index.php/TI/P%C4%99tle

#Zadanie: sumator liczb dodatnich wersja 1
def zadanie1v1():
    suma = 0;
    while True:
        liczba = input('Podaj liczbe, ujemna konczy: ')
        a = float(liczba);
        if a < 0:
            break;
        suma += a;
        print('Suma liczb = ', suma)

#zadanie1v1();

def zadanie1v2():
    suma = 0; liczba_wprowadzen = 0;
    while True:
        liczba = input('Podaj liczbe, ujemna konczy: ')
        a = float(liczba);
        if a < 0:
            break;
        suma += a;
        liczba_wprowadzen+=1;
        print('Suma liczb = ', suma)
    print('Liczba wprowadzonych liczb: ', liczba_wprowadzen)

zadanie1v2();


#Zadania z http://www.ling.gu.se/~lager/python_exercises.html
