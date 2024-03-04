def square(a):
    '''this is square function'''
    return a*a

def sum(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return a+b

def squareroot(b):
    if b>=0:
        return b**(0.5)
    else:
        return 'UNDEFINED'

def hypotenuse(a,b):
    c = squareroot(sum(square(a),square(b)))
    return c
