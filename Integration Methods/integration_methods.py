from matplotlib import pyplot as plt
import numpy as np
import random, math

def func(x):
    return math.sin(2*x)*x

def rightside_integration(func, n, a, b):
    
    #Right endpoint Riemann sum on func over a to b with n intervals
    sum = 0
    for i in range(1,n+1):
        sum += func(a + i*(b-a)/n)
    return sum*(b-a)/n
        

def leftside_integration(func, n, a, b):

    #Left endpoint Riemann sum on func over a to b with n intervals
    sum = 0
    for i in range(0, n):
        sum += func(a + i*(b-a)/n)
    return sum*(b-a)/n
    

def midpoint_integration(func, n, a, b):

    #Midpoint Riemann sum on func over a to b with n intervals (does not work)
    sum = 0
    for i in range(0, n):
        sum += func(a + (i+.5)*(b-a)/n)
    return sum*(b-a)/n

def trapezoidal_integration(func, n, a, b):

    #Trapezoidal Riemann sum on func over a to b with n intervals
    sum = 0
    for i in range(0, n):
        sum += func(a + ((b-a)/n)*i) + func(a + ((b-a)/n)*(i+1))
    
    return sum * (b-a)/(2*n)

def montecarlo_integration(func, n, minmax_sample, a, b):
    
    #Monte Carlo Integral estimate on func over a to b with n random sampled points
    funcmax = 0
    funcmin = 0
    suminbounds = 0
    
    for i in range(0, minmax_sample+1):
    
        #Iterative approach to find max and min of function
        val = func(a + i*(b-a)/minmax_sample)
        if (val > funcmax):
            funcmax = val
        if (val < funcmin):
            funcmin = val
    
    for i in range(n):  
    
        #if a point is bounded between the function value and the x axis it is added to the suminbounds
        
        randx = a + random.random()*(b-a)
        randy = funcmin + random.random()*(funcmax-funcmin)
        funcy = func(randx)
        
        if (funcy > randy and funcy > 0 and randy > 0):
            suminbounds += 1
            
        elif (funcy < randy and funcy < 0 and randy < 0):
            suminbounds -= 1
            
    return (b-a)*(funcmax-funcmin)*(suminbounds/n)


