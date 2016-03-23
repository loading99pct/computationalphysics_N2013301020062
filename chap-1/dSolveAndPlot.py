# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:38:48 2016

@author: Wang Ziang
"""
import numpy as np
array = np.array
import math
from dSolve_1 import *
import matplotlib.pyplot as plt

def dSolveAndPlot(func, x0, tMax, stepSize, method = "RK4"):
    a = dSolve(func, x0, tMax, stepSize, method)
    x = a[0][1]
    if type(x) != np.ndarray:
        n = 1
    else:
        n = len(x.tolist())
    T=getTList(a)
    Xi=[getXiList(a,i) for i in range(1,n+1)]

    for i in range(1,n+1): 
        plt.plot(T,Xi[i-1],label="X_"+str(i))
    plt.legend(loc='upper right', frameon=False)
    plt.show()    

def dSolveAndHoldOn(func, x0, tMax, stepSize, method = "RK4"):
    a = dSolve(func, x0, tMax, stepSize, method)
    x = a[0][1]
    if type(x) != np.ndarray:
        n = 1
    else:
        n = len(x.tolist())
    T=getTList(a)
    Xi=[getXiList(a,i) for i in range(1,n+1)]

    for i in range(1,n+1): 
        plt.plot(T,Xi[i-1],label="X_"+str(i))
   
