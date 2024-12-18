from math import *


def cos(x):
    cosx = 0
    for j in range(100):
        cosx += (-1)**j*(x**(2*j)/factorial(2*j))
    return cosx


def ch(x):
    chx = 0
    for j in range(100):
        chx += (int(x)**(2*j)/factorial(2*j))
    return chx
