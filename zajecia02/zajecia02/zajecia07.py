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

n = int(input('Podaj cyferkę: '))
for i in EvenGeneratorv1(n):
    print(i, end=',')

#Powtórz powyższe zadanie, ale wyświetl liczby podzielna przez 5 i 7 i skorzystaj tym razem z pętli for


#napisz program, który akceptuje proste wyrażenie matematyczne i wyświetla wynik na stdout. Wsk: https://docs.python.org/2/library/functions.html#eval



#Wygeneruj listę 1000  randomowych liczb typu float w przedziale od 5 do 95 i zapisz do pliku rand.txt Wsk: https://docs.python.org/2/library/random.html




#http://brain.fuw.edu.pl/edu/index.php/TI/Matplotlib


''' Napisz program na znajdowanie najdłuższych linii względnie wyrazów w zawartości pliku.
'''

#http://brain.fuw.edu.pl/edu/index.php/TI/Operacje_na_macierzach: rozwiąż zadania z mnożeniem i transpozycją macierzy
