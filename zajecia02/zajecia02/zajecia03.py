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

#zadanie1v2();

#lista.append(a);
def zadanie1v3():
    lista = []
    suma = 0;
    while True:
        liczba = input('Podaj liczbe, ujemna konczy: ')
        a = float(liczba);
        if a < 0:
            break;
        lista.append(a);
        suma += a;
    dlugosc = len(lista)
    srednia = suma/dlugosc;
    print('Liczba wprowadzonych liczb: ', dlugosc, '; Srednia liczb: ' ,srednia)

#Napisz dwa programy, które obliczają sumę liczb całkowitych od 1 do 10. W pierwszym wykorzystaj pętlę while, a w drugim pętlę for. 
def sumaliczb010(n):
    suma = 0;
    for i in range(1,n+1):
        suma += i;
    print(suma)

#sumaliczb010(3000);

#Napisz program który pyta użytkownika o liczbę, a następnie oblicza silnię tej liczby. Wykorzystaj pętlę for.
def liczysilnie(n):
    suma = 1;
    for i in range(1,n+1):
        suma *= i;
    print(suma)

liczysilnie(4)


#Zadania z http://www.ling.gu.se/~lager/python_exercises.html