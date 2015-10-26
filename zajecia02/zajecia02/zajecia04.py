# -*- coding: utf-8 -*-
#Enter konczy wywolanie funkcji
def zadanie1v3():
    lista = []
    suma = 0;
    while True:
        liczba = input('Podaj liczb?, enter konczy: ')
        if not liczba:
            break;
        a = float(liczba);
        lista.append(a);
        suma += a;
    dlugosc = len(lista)
    srednia = suma/dlugosc;
    print('Liczba wprowadzonych liczb: ', dlugosc, '; Srednia liczb: ' ,srednia)

#zadanie1v3()
 

#Prosz? napisa? funkcj?, kt?ra:
#1. Kt?ra wypisuje sum? dw?ch argument?w.`
#2. Kt?ra zwraca sum? dw?ch argument?w.
#3. Wypisuj?c? wynik dzielenia zmiennoprzecinkowego dla dw?ch dowolnych argument?w b?d?cych liczbami.
def wynikdzielenia(a,b):
    return float(a)/b;

#print(wynikdzielenia(1,2))
from math import pow
#4. Obliczaj?c? i zwracaj?c? pierwiastek zadanego stopnia ? w li?cie parametr?w podajemy liczb? podpierwiastkow? i stopie? pierwiastka, domy?lnie niech wynosi on dwa.
def pierwiastekstopnian(a,r=2):
    return pow(a,1/r)

#print(pierwiastekstopnian(16))

#5. Wypisuj?c? r?wnanie prostej przechodz?cej przez wsp??rz?dne dw?ch zadanych punkt?w.

def strlineeq(x1,y1,x2,y2):
    print('y = ', (y1-y2)/(x1-x2), 'x + ', y1-x1*((y1-y2)/(x1-x2)) )

#strlineeq(2,2,0,0)

#6. Wypisuj?c? jedno lub dwa rozwi?zania r?wnania kwadratowego a x^2+b x +c = 0, lub informuj?c?, ?e nie ma rozwi?za? rzeczywistych. Parametrami funkcji niech b?d? a, b, c ? wsp??czynniki r?wnania kwadratowego.
#7. Zwracaj?c? silni? argumentu. Zadanie prosz? rozwi?za? na dwa sposoby ? raz z u?yciem p?tli, a drugi raz rekurencyjnie.

def liczysilniev2(n):
    if n > 0:
        return n*liczysilniev2(n-1);
    else:
        return 1;
#print(liczysilniev2(4))

#8. Wypisuj?c? ??dan? liczb? wyraz?w ci?gu Fibbonacciego. (F_0=0, F_1=1, F_n=F_{n-1}+F_{n-2})
def fibonnacci(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonnacci(n-1)+fibonnacci(n-2) 

#print(fibonnacci(24))

#9. S?u??c? do obliczania n-tego elementu ci?gu arytmetycznego o zadanym wyrazie pocz?tkowym i r??nicy. Funkcja powinna dawa? mo?liwo?? wypisywania wynik?w po?rednich (element?w ci?gu od pierwszego do przedostatniego obliczonego).

def elementarytmy(n, n0, d):
     ele = n0;
     for i in range(n):
         ele += d
     return ele

#10. S?u??c? do obliczania n-tego elementu ci?gu geometrycznego o zadanym wyrazie pocz?tkowym i ilorazie. Funkcja powinna dawa? mo?liwo?? wypisywania wynik?w po?rednich (element?w ci?gu od pierwszego do przedostatniego obliczonego).
#11. S?u??c? do obliczania n-tej sumy cz??ciowej ci?gu arytmetycznego o zadanym wyrazie pocz?tkowym i r??nicy. Funkcja powinna dawa? mo?liwo?? wypisywania wynik?w po?rednich (kolejno obliczanych element?w ci?gu i sum).

def sumaarytm(n, n0, d, p = False):
    result = 0;
    for i in range(n):
        result += elementarytmy(i, n0, d)
        if p:
            print(result)
    return result;
#print(sumaarytm(10,0,1, True))

#12. S?u??c? do obliczania n-tej sumy cz??ciowej ci?gu geometrycznego o zadanym wyrazie pocz?tkowym i ilorazie. Funkcja powinna dawa? mo?liwo?? wypisywania wynik?w po?rednich (kolejno obliczanych element?w ci?gu i sum).
#13. S?u??c? do obliczania n-tej sumy cz??ciowej ci?gu 1/n^m, gdzie n i m s? parametrami. Funkcja powinna dawa? mo?liwo?? wypisywania wynik?w po?rednich (kolejno obliczanych element?w ci?gu i sum).
#14. Funkcj? obliczaj?c? d?ugo?? wektora jedno-, dwu- lub tr?jwymiarowego.
from math import sqrt

def vlen(a, b=0, c=0):
    return sqrt(a**2 + b**2 + c**2)

#print(vlen(4,3, 1))

# opt. 15. Funkcj?, kt?ra zwr?ci napis b?d?cy reprezentacj? podanej liczby ca?kowitej. T? ?konwersj? na napis? wykonaj cyfra po cyfrze.
print('zajecia04', __name__)
import module1
module1.mojafunkcja()



#sito Eratostenesa