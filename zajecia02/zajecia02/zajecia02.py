# -*- coding: utf-8 -*-

import os
import numpy


'''
#rzutowanie na typy zmiennych: strin(), int(), float(), long()
a=3; b=4; print(a+b) #a, b to liczby typu integer
c='3'; d ="4"; print(c+d) #a,b to ciagi znakow

print(str(a)+str(b))
print(int(c)+int(d))
'''
##############################################################

#funkcje wbudowane: https://docs.python.org/3.3/library/functions.html
##############################################################
'''
#funkcja input()
liczba = input('Wpisz liczbe: ')
print(liczba)
'''

##############################################################
'''
#if...elif...else
right_number = 7
liczba = input('Zgadnij liczbe od 0 do 10: ')
liczba = int(liczba)
if liczba == right_number:
    print('Zgadłes!');
elif (liczba < right_number):
    print('Za malo')
else:
    print('Za duzo')
'''
##############################################################
'''
print(__name__)
if __name__ == '__main__':
    #if...elif...else
    right_number = 7
    liczba = input('Zgadnij liczbe od 0 do 10: ')
    liczba = int(liczba)
    if liczba == right_number:
        print('Zgadłes!');
    elif (liczba < right_number):
        print('Za malo')
    else:
        print('Za duzo')
'''

##############################################################a
#petla while
'''
i = 10;
while i>0:
    print(i);
    i=i-1;
'''
##############################################################a
#poprawiona wersja zgadywanki z petla while
'''
right_number = 7
while True:
    liczba = input('Zgadnij liczbe od 0 do 10: ')
    liczba = int(liczba)
    if liczba == right_number:
        print('OK!');
        break;
    elif (liczba < right_number):
        print('Za malo')
    else:
        print('Za duzo')
'''

##############################################################a
#rozwiazanie równania kwadratowego
a = input('Podaj a')
b = input('Podaj b')
c = input('Podaj c')




