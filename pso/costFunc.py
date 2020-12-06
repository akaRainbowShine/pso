import numpy as np
from math import pi, e
from numpy import exp, sqrt, sin, cos
import math
def costFunc(num_func,x,dims):
    #print(count)
    if num_func == 1:
        return rastrigin(x,dims)
    if num_func == 2:
        return rosenbrock(x,dims)
    if num_func == 3:
        return eggholder(x,dims)
    #print(num_func)
    #exit()
    return ackley(x,dims)
def sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
def rastrigin(x,dims):
    A=10
    return A*dims + np.sum(np.square(x) - A * np.cos(2*math.pi * x), axis=0) 
def rosenbrock(x,dims):
    A=100
    x_0 = x[:-1]
    x_1 = x[1:]
    return np.sum(A*np.square(x_1 - np.square(x_0)) + np.square(1 - x_0), axis=0)
def eggholder(x,dims):
    assert x.shape[0] == 2
    x, y = x
    return -(y + 47) * sin(sqrt(abs(x/2 + (y+47)))) - x * sin(sqrt(abs(x - (y+47))))
def ackley(x,dims):
    assert x.shape[0] == 2, "This function supports only 2-dimensional variables."
    x, y = x
    return -20 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) \
            - exp(0.5 * (cos(2*pi * x) + cos(2*pi * y))) + e + 20
                    