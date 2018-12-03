#!/usr/bin/python

import math

wejscie = [float(x) for x in raw_input().split()]

r = wejscie[0]
d = wejscie[1]

pi = 3.141592654

pole = ((r*r)-((d*d)/4))*pi
pole = round(pole,2)

print pole
