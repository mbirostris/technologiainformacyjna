# -*- coding: utf-8 -*-

#Rozwiązania kolokwium

#################################################
#                 Zadanie 1
#################################################
#Zadanie 1 - 1 sposob
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns
numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)

################################################
#Zadanie 1 - 2 sposob
def liczbakrolikow(glowy, nogi):
    return int((nogi-2*glowy)/2)

def liczbakur(glowy, nogi):
    return int(glowy-liczbakrolikow(glowy, nogi));

print(liczbakur(35, 94), liczbakrolikow(35, 94))

#################################################
#                 Zadanie 2
#################################################
a = [  
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ']*7,
        [' ']*7,
        [' ']*7,
        [' ']*7,
        [' ']*7,
        ['-','-','-','-','-','-','-'],
        ['1','2','3','4','5','6','7'],
]

def printav1(a):
    for row in a:
        for cell in row:
            print(cell, end='')
        print()


def wypelnija(b, xo):
    for i in range(5,-1,-1):
        if a[i][b] != ' ':
            continue;
        else:
            a[i][b] = xo
            return True
    return False;

xx = 'x'; oo = 'o'
while True:
    printav1(a);
    b = int(input('Podaj kolumne: '))
    if b >0 and b < 8:
        if wypelnija(b-1, xx):
            printav1(a);
        else:
            break;
        xx, oo = oo, xx
    else:
        print('Zły zakres wartości, podaj liczbę od 1 do 7!')
print("Koniec")
#################################################
#                 Zadanie 3
#################################################
i = 0;
output = open('plik.xml', 'w')
for text in open('pacPat_t0sc0sg0.xml', 'r'):
    if  "code" in text:
        output.write(text.replace(">", " bx=\"%d\">" % (i)))
        i+=1;
    else:
        output.write(text)
output.close()
