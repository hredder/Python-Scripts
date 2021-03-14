import math

#Made by Henry Redder
#A couple differentiation functions

def func(x):

    #Arbitrary Function
    return math.cos(x)

def polynomial_derivative(polylist):
    
    #Returns the derivative of the polynomial via the power rule
    #Polynomials are represented with coefficients in a list. Index 0 has the coefficient for x^0 and so on
    newlist = []
    for i in range(len(polylist)-1):
        newlist.append(polylist[i+1]*(i+1))
    
    return newlist
    
    
def numerical_derivative(func, x):

    #Numerical Derivative on func at x
    diff = .00001
    return (func(x+diff) - func(x))/diff


def newton_method(func, x, n):
    
    #Newton-Raphson method on func at x with n iterations
    #Returns None if numerical_derivative = 0 (Newton's method fails)
    
    for i in range(n):
        if (numerical_derivative(func, x) != 0):
            x = x - (func(x)/numerical_derivative(func, x))
        else:
            return None
    return x
        

    