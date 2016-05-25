# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:38:48 2016

@author: Wang Ziang
"""
import numpy as np
array = np.array
import math
from dSolve_2 import *
import matplotlib.pyplot as plt


def easyPlotXYHoldON(X, Y, legendC = "", xLabel = "", yLabel = "", titleLabel = ""):
    plt.plot(X,Y,label=legendC)
    plt.legend(loc='upper right', frameon=False)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(titleLabel)
    
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()
    plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))

    plt.grid(True)

def easyScatterPlotXYHoldON(X, Y, legendC = "", xLabel = "", yLabel = "", titleLabel = ""):
    plt.plot(X,Y, 'o',markersize = 1.1 , label=legendC)
    plt.legend(loc='upper right', frameon=False)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(titleLabel)
    
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()
    plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))

    plt.grid(True)

def detailedDSolutionPlotAndHoldOn(solution, labelList, xLabel = "", yLabel = "", titleLabel = ""):
    x = solution[0][1]
    n = len(x.tolist())
    T=getTList(solution)
    Xi=[getXiList(solution,i) for i in range(1,n+1)]
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

def dSolutionPlotAndHoldOn(solution):
    x = solution[0][1]
    n = len(x.tolist())
    labelList = [""] * n
    detailedDSolutionPlotAndHoldOn(solution, labelList)

def dSolutionFastPlot(solution):
    dSolutionPlotAndHoldOn(solution)
    plt.show() 

def done():
    plt.show()
