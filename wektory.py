#! /usr/bin/python3

'''Prosta klasa opisująca wektory na płaszczyźnie.'''

class Wektor2(object):

    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def dlugosc(self):
        return (self.x * self.x + self.y * self.y) ** 0.5
        
    def __str__(self):
        return 'Wektor2({}, {})'.format(self.x, self.y)
        
    __repr__ = __str__
    
    def __mul__(self, number):
        return Wektor2(number * self.x, number * self.y)
        
    __rmul__ = __mul__
    
    def __add__(self, other):
        return Wektor2(self.x + other.x, self.y + other.y)
        
    def __neg__(self):
        return Wektor2(-self.x, -self.y)
        
    def __sub__(self, other):
        return Wektor2(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    __abs__ = dlugosc
    
    def __len__(self):
        return 2
    
 

x = Wektor2(3,4)
print(x);   
