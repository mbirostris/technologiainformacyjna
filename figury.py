#! /usr/bin/python3

''' Proste klasy opisujące figury geometryczne.'''

import math

class Kwadrat(object):

    def __init__(self, bok):
        self.bok = bok 
        
    def pole(self):
        return self.bok ** 2
        
    def obwod(self):
        return self.bok * 4
        

class Kolo(object):

    def __init__(self, promien):
        self.promien = promien
        
    def pole(self):
        return math.pi * self.promien ** 2
        
    def obwod(self):
        return 2 * math.pi * promien
        


