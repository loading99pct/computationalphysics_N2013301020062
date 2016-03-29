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

def dSolveAndFastPlot(func, x0, tMax, stepSize, method = "RK4"):
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
    plt.grid(True)
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()
    plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))
    
    
    plt.show()    
'''
def dSolveAndHoldOnDetailWithSelection(func, x0, tMax, stepSize, method , toPlotList, labelList):
    a = dSolve(func, x0, tMax, stepSize, method)
    x = a[0][1]
    if type(x) != np.ndarray:
        n = 1
    else:
        n = len(x.tolist())
    T=getTList(a)
    Xi=[getXiList(a,i) for i in range(1,n+1)]
    j = 0
    for i in range(1,n+1): 
        if i in toPlotList:
            #plt.plot(T,Xi[i-1],label="X_"+str(i))
            plt.plot(T,Xi[i-1], label=labelList[j])
            j = j+1
    plt.legend(loc='upper right', frameon=False)
'''

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
    plt.legend(loc='upper right', frameon=False)
    
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()
    plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))

    plt.grid(True)

def dSolveAndDetailedPlotAndHoldOn(func, x0, tMax, stepSize, method,\
 labelList, xLabel = "", yLabel = "", titleLabel = ""):
    a = dSolve(func, x0, tMax, stepSize, method)
    x = a[0][1]
    if type(x) != np.ndarray:
        n = 1
    else:
        n = len(x.tolist())
    T=getTList(a)
    Xi=[getXiList(a,i) for i in range(1,n+1)]
    for i in range(1,n+1): 
        plt.plot(T,Xi[i-1],label=labelList[i-1])
    plt.legend(loc='upper right', frameon=False)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(titleLabel)
    
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()
    plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))
    
    plt.grid(True)
