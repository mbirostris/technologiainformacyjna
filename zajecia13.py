
#Zadanie1 Napisz funkcję rysującą funkcje sin(t), cos(t) i sin(t)*cos(t) w przedziale 0<t<2. Podpisz osie, narysuj legendę, zmień kolory i styl linii. Ustaw interwał podpisów osi 't' na 0.2. Zapisz rysunek do pliku .png

import numpy as np
import matplotlib.pyplot as plt

def trygo():
    x = np.arange(0.0, 2.0, 0.01)
    y1 = np.sin(2.0*np.pi*x)
    y2 = np.cos(2.0*np.pi*x)
    y = y1 * y2
    #l1 = plt.plot(x, y, 'b')
    l1, l2, l3 = plt.plot(x, y, 'b', x, y1, 'r--', x, y2, 'g')
    plt.legend((l2, l3, l1), ('y1', 'y2', 'y1*y2'))
    plt.xlabel('czas')
    plt.ylabel('pozycja')
    plt.title('wykres paru funkcji trygonometrycznych')
    plt.grid(True)
    plt.xticks(np.arange(0.0, 2.0, 0.2))
    #plt.show()
    plt.savefig('trygo.png')

#trygo();

#Zadanie2 Narysuj rozkłąd gaussa: a) jako histogram (wygeneruj listę wartości losowych funkcją np.random.randn()) b) jako funkcję ciągłą metoda mlab.normpdf()

from matplotlib.mlab import normpdf

def gauss():
    mi, sigma = 100, 15
    x = mi + sigma * np.random.randn(1000)

    n, bins, patches = plt.hist(x, 50, normed=True, facecolor='g', alpha=0.75)

    bincenters = 0.5 * (bins[1:] + bins[:-1])

    y = normpdf(bincenters, mi, sigma)

    l = plt.plot(bincenters, y, 'r--')

    plt.show()

gauss()


#Zadanie3 Napisz program tworzący statystykę pliku wczytywanego jako argument skryptu. Niech program wypisuje na stdout nazwę pliku, liczbę lini w pliku oraz maksymalną, minimalną, średnią oraz medianę liczby znaków w liniach pliku. Ponadto niech program tworzy histogram długości lini. Użyj np. pliku  pacPat_t0sc0sg0.xml do przetestowanie działania programu. 

from sys import argv
'''
f = open(argv[1])
l = []
for line in f:
  l.append(len(line.strip('\n')))
f.close()
dl = np.array(l, dtype=np.int)
print(dl)
print('statystyki pliku {}:'.format(argv[1]))
print('liczba linii: {}'.format(len(dl)))
print('maksymalna: {}, minimalna: {}, średnia: {}, mediana: {}'.
      format(dl.max(), dl.min(), dl.mean(), np.median(dl))
      )
plt.hist(dl, bins=(dl.max()-dl.min()+1), color='green')
plt.title('rozkład długosci linii w pliku {}'.format(argv[1]))
plt.xlabel('długosc słowa')
plt.ylabel('czestosc')
plt.show()
'''

#Zadanie4 napisz funkcję rysującą funkcję sin(x)*exp(-x) w przedziale 0<x<5. Korzystając z metody plt.fill() zamaluj obszar pod funkcją.

def zamaluj():
    x = np.linspace(0, 5)
    y = np.sin( np.pi * x) * np.exp(- x)

    plt.fill(x, y, 'r')
    plt.grid(True)
    plt.show()

def zamalujv2():
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.sin(3 * x)
    plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
    plt.show()

#zamaluj()

####Spines##################################################
def spines():
    x = np.linspace(0, 2*np.pi, 50)
    y = np.sin(x)
    y2 = y + 0.1 * np.random.normal(size=x.shape)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'k--')
    ax.plot(x, y2, 'ro')

    # set ticks and tick labels
    ax.set_xlim((0, 2*np.pi))
    ax.set_xticks([0, np.pi, 2*np.pi])
    ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
    ax.set_ylim((-1.5, 1.5))
    ax.set_yticks([-1, 0, 1])

    # Only draw spine between the y-ticks
    ax.spines['left'].set_bounds(-1, 1)
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    plt.savefig('spines.png')
    #plt.show()


spines();

#http://matplotlib.org/users/gridspec.html
#http://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()


