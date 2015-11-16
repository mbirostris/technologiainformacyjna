#! /usr/bin/python3
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
