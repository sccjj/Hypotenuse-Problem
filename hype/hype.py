def square(a):
    return a*a

def sum(a,b):
    return a+b

def squareroot(b):
    return b**(0.5)

def hypotenuse(a,b):
    c = squareroot(sum(square(a),square(b)))
    return c
