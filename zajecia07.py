# -*- coding: utf-8 -*-


#Zdefinij funkcję, która akceptuje dwa ciągi znaków i wyświetla ciąg o największej długości. Jeśli ciągi znaków są równe funkcja powinna wyświetlić oba.

def printValue(s1, s2):
    len1 = len(s1); len2 = len(s2);
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
#        print(s1,s2)
        print(s1)
        print(s2)

#printValue("mama","tata")

import re
#NApisz funkcję czytającą z stdin adres mailowy w formie 'username@companyname.com'. Niech funkcja wyświelna następnie nazwę użytkownika (username)
#Wsk: #https://docs.python.org/2/library/re.html

def readmail():
    pat1 = "(\w+)@((\w+\.)+(com))"
    pat2 = "(\w+)@((\w+\.)+\w+)"
    while True:
        emailAddress = input('Podaj nazwę email: ')
        if not emailAddress:
            break;
        r2 = re.match(pat1,emailAddress)
        if r2:
            print(r2.group(1))
            continue;
        r3 = re.match(pat2,emailAddress)
        if r3:
            print(r3.group(1))
            continue;
        print("Zły format!")


        
#readmail()

#Napisz to samo co wyżej, ale powinno zwracać nazwę maila (np: gmail.com)

def readmailv2():
    pat1 = "(\w+)@((\w+\.)+(com))"
    pat2 = "(\w+)@((\w+\.)+\w+)"
    while True:
        emailAddress = input('Podaj nazwę email: ')
        if not emailAddress:
            break;
        r2 = re.match(pat1,emailAddress)
        if r2:
            print(r2.group(2))
            continue;
        r3 = re.match(pat2,emailAddress)
        if r3:
            print(r3.group(2))
            continue;
        print("Zły format!")

#readmailv2();


#Wykorzystując słowo kluczowe yield napisz generator liczb parzystych od 0 do n, oddzielanych przecinkami dla liczby n czytanej z stdin. Wykorzystaj pętlę while. Np. Dla wpisanego 6 wyświetli "0,2,3,6". Wsk: https://docs.python.org/3/library/stdtypes.html#str.join

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

'''
#n = int(input('Podaj cyferkę: '))
lista = []
for i in EvenGenerator(n):
    lista.append(str(i))

#print(','.join(lista))
'''
'''
n = int(input('Podaj cyferkę: '))
for i in EvenGenerator(n):
    print(i, end=',')
'''
def EvenGeneratorv1(n):
    i=0
    while i<=n:
        yield i
        i+=2
'''
n = int(input('Podaj cyferkę: '))
for i in EvenGeneratorv1(n):
    print(i, end=',')
'''
#Powtórz powyższe zadanie, ale wyświetl liczby podzielna przez 5 i 7 i skorzystaj tym razem z pętli for

def EvenGeneratorv3(n):
    for i in range(0,n+1):
        if i%5==0 and i%7==0:
            yield i
'''
n = int(input('Podaj cyferkę: '))
for i in EvenGeneratorv3(n):
    print(i, end=',')
'''
def print5and7():
    n=int(input("Podaj cyfrę: "))
    values = []
    for i in EvenGeneratorv3(n):
        values.append(str(i))

    print(",".join(values))
#print5and7()
#napisz program, który akceptuje proste wyrażenie matematyczne i wyświetla wynik na stdout. Wsk: https://docs.python.org/2/library/functions.html#eval

#n = input("Podaj wyrazenie: "); print(eval(n))

#Wygeneruj listę 1000  randomowych liczb typu float w przedziale od 5 do 95 i zapisz do pliku rand.txt Wsk: https://docs.python.org/2/library/random.html

import random 
def napisdopliku():
    f = open('rand.txt', 'w')
    for i in xrange(0,1000):
        f.write(str(random.random()*90+5)+'\n' )
    f.close();

napisdopliku()
#http://brain.fuw.edu.pl/edu/index.php/TI/Matplotlib

'''
import pylab as pl
x = pl.arange(0.0, 2.0, 0.01)
y = pl.sin(2.0*pl.pi*x)
pl.plot(x,y)
pl.show()
'''

''' Napisz program na znajdowanie najdłuższych linii względnie wyrazów w zawartości pliku.
'''

'''Znajdowanie najdłuższych linii względnie wyrazów w zawartości pliku.
Uwaga: wyrazy tutaj liczą się razem z "przyklejonymi" znakami przestankowymi.
'''

def najdluzsze_linie(plik):
  '''Zwraca listę linii o maksymalnej długości wśród linii
  pliku.
  '''
  f = open(plik)
  maxdl = 0
  najdluzsze = []
  for linia in f:
    linia = linia.strip()
    if len(linia) == maxdl:
      najdluzsze.append(linia)
    elif len(linia) > maxdl:
      maxdl = len(linia)
      najdluzsze = [linia]
  f.close()
  return najdluzsze
  
def najdluzsze_wyrazy0(plik):
  '''Zwraca listę wyrazów o maksymalnej długości wśród wyrazów
  w treści pliku. Metoda linia po linii.
  '''
  f = open(plik)
  maxdl = 0
  najdluzsze = []
  for linia in f:
    for wyraz in linia.strip().split():
      if len(wyraz) == maxdl:
        najdluzsze.append(wyraz)
      elif len(wyraz) > maxdl:
        maxdl = len(wyraz)
        najdluzsze = [wyraz]  
  f.close()
  return najdluzsze
  
def najdluzsze_wyrazy1(plik):
  '''Zwraca listę wyrazów o maksymalnej długości wśród wyrazów
  w treści pliku. Metoda cały plik na raz.
  '''
  f = open(plik)
  tresc = f.read()
  f.close()
  wyrazy = tresc.split()
  maxdl = 0
  najdluzsze = []
  for w in wyrazy:
    if len(w) == maxdl:
      najdluzsze.append(w)
    elif len(w) > maxdl:
      maxdl = len(w)
      najdluzsze = [w]
  return najdluzsze
  
def najdluzsze_wyrazy(plik):
  '''Zwraca listę wyrazów o maksymalnej długości wśród wyrazów
  w treści pliku. Metoda zwięzła, ale ciut wolniejsza.
  '''
  f = open(plik)
  wyrazy = f.read().split()
  f.close()
  maxdl = max(len(w) for w in wyrazy)
  najdluzsze = [w for w in wyrazy if len(w)==maxdl]
  return najdluzsze

if __name__ == '__main__':
  from sys import argv
  plik = argv[1]
  for linia in najdluzsze_wyrazy(plik):
    print(linia)


#http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach: rozwiąż zadania z mnożeniem i transpozycją macierzy
