"""
    this is a calculator app
"""

def add(x,y):
    """
    this function is used to add two numbers
    """
    return x+y

def sub(x,y):
    """
    this function is used to subtract two numbers
    """
    if(x>y):
        return x-y
    else:
        return "first number can't be small"

def mul(x,y):
    """
    this function is used to multiply two numbers
    """
    return x*y

def div(x,y):
    """
    this function is used to divide two numbers
    """
    if(y==0):
        return "number can't be divided by 0"
    else:
        return x/y

def mod(x,y):
    """
    this function is used to modulo two numbers
    """
    return (x/100)*y