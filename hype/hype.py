import numpy as np

def square(a):
    return a*a

def sum(a,b):
    return a+b

def squareroot(b):
    if b>=0:
        return b**(0.5)
    else:
        return 'UNDEFINED'

def hypotenuse(a,b):
    c = squareroot(sum(square(a),square(b)))
    return c
