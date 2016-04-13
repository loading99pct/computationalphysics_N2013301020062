# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:12:47 2016
@author: Wang Ziang
"""

"""
This function solves a system of first-order differential equations
(or A first-order differential equation, of course) of the form:

-----------------------------------------------

                X'[t] = F[t,X]
                
-----------------------------------------------
                
    where  X = (x1,x2,...,xn)T
    F:  X -> Y
        (x1,x2,...,xn)T -> (y1,y2,...,yn)T
        where:
        y1 = f1(t,x1,x2,...,xn),
        y1 = f1(t,x1,x2,...,xn),
        .
        .
        yn = f1(t,x1,x2,...,xn) 
"""


'''
in the following method:
xi could be a scalar, or a vector
    if xi is a vector, 
    it should be given by the data structure "array" defined in numpy package
    e.g. numpy.array([x1,x2,x3])
the f is the RHS-function in X'[t] == f(X,t)
    f: ti,xi -> xii
    f should be defined in the form 
        define f(ti, Xi):  
            return a vector with the same size as Xi
        or given by a equivalent lambda expression
with fixed step size h, and a given f,
the followingMethod is a iterative function 
    followingMethod: state ->state
                     (ti,xi) -> (tii,xii)
'''
import numpy as np
array = np.array
from nest import nestList
from nest import nestUntilList
import math


"""
the constructor and selector of a State:(t,X) 
"""
def makeState(t, x): return [t,x]
def getX(state): return state[1]
def getT(state): return state[0]

"""
four methed in Runge-Kutta's family
"""


def forwardEulerMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    tii = ti + h  # tii = Subscibe[t,i+1]
    xii = xi + h * f(ti,xi)  # xii = Subscibe[x,i+1]
    return makeState(tii,xii)

def explicitTrapezoidalMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    tii = ti + h  
    xii = xi + h/2.0 *(f(ti,xi) + f(ti+h, xi+h*f(ti,xi)))
    return makeState(tii,xii)

def midPointMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    h = float(h)
    tii = ti + h
    xii = xi + h * f(ti+h/2, xi+h/2*f(ti,xi))
    return makeState(tii,xii)

def rk4Method(state, f, h):
    '''
    Classic fourth-order Runge-Kutta method
    '''
    ti = getT(state)
    xi = getX(state)
    h = float(h)
    tii = ti + h 
    s1 = f(ti,xi)
    s2 = f(ti+h/2, xi+h/2*s1)
    s3 = f(ti+h/2, xi+h/2*s2)
    s4 = f(ti+h, xi+h*s3)
    xii = xi + h/6 * (s1 + 2*s2 + 2*s3 +s4)
    return makeState(tii,xii)


__methodDictionary={\
    "ForwardEuler":forwardEulerMethod,\
    "ExplicitTrapezoidal":explicitTrapezoidalMethod,\
    "Midpoint":midPointMethod,\
    "RK4":rk4Method\
}



'''-------------------------------------------------------------------------------'''



def normalize(initX):
    """
    normalize X, 
    if array([X__]) ,-> array([X])
    if X_Number ,-> array([X])
    used in dSolve
    
    """
    if type(initX) == np.ndarray:
        return initX      
    else:
        return array([initX])   

def dSolve(func, x0, tMax, stepSize, method = "RK4"):
    """
    dSolve solves a system of first-order differential equations
    (or A first-order differential equation, of course) of the form:
    
    -----------------------------------------------
    
                    X'[t] = F[t,X]
                    
    -----------------------------------------------
    (
                    
        where  X = (x1,x2,...,xn)T
        F:  X -> Y
            (x1,x2,...,xn)T -> (y1,y2,...,yn)T
            where:
            y1 = f1(t,x1,x2,...,xn),
            y1 = f1(t,x1,x2,...,xn),
            .
            .
            yn = f1(t,x1,x2,...,xn) 
    )
    
    with initial value X[0] =x0,
    (
        !!! if xi is a vector, 
        it should be given by the data structure "array" defined in numpy package
        e.g. numpy.array([x1,x2,x3])
    )
    
    from t = 0 to t = tMax,
    
    with fixed step size = stepSize,
    
    using method selected from __methodDictionary
    
    
    Output: [state0, state1,... ]
        where statei has the form [ti, xi] for a ODE, 
            or [ti, array([x1i,x2i...])] for s system of ODEs
                    
    """         

    x0 = normalize(x0)
    times = int(math.ceil(float(tMax) / stepSize))
    methodFunc = __methodDictionary[method]
    toNext = lambda state: methodFunc(state, func, stepSize)
    return nestList(toNext, makeState(0, x0), times)


def dSolveUntil(func, x0, stepSize, stopQ, method = "RK4", tMax = 1000):
    '''
    stopQ is about a state
    '''
    x0 = normalize(x0)
    maxStep = int(math.ceil(float(tMax) / stepSize))
    methodFunc = __methodDictionary[method]
    toNext = lambda state: methodFunc(state, func, stepSize)
    return nestUntilList(toNext, makeState(0, x0), stopQ, maxStep)


'''-------------------------------------------------------------------------------'''


def getColumn(table,i):
    "get the ith column of the table\
    without security "
    return [elem[i] for elem in table]
    
    

def getTList(result):
    "get the time list T of the result given by function dSolve\
    without security "
    return getColumn(result, 0)

def getXiList(result, i = 1):
    "get the list of i-th component Xi of the result given by function dSolve\
    without security "
    
    return getColumn( getColumn(result,1), i-1)   
    '''
    if type(result[0][1]) == np.ndarray:
        return getColumn( getColumn(result,2), i-1)      
        #return [elem[1][i-1] for elem in result]
    else:
        return getColumn(result,2)         
        #return [elem[1] for elem in result]
    '''
def reduceStateList(result, includeList):
    def reduceState(state):
       return makeState(getT(state), array([getX(state)[i] for i in includeList]))
    return map(reduceState, result)

'''-------------------------------------------------------------------------------'''

