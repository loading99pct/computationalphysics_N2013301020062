import numpy as np
array = np.array
import math
from dSolve_1 import *
import matplotlib.pyplot as plt
from dSolveAndPlot import dSolveAndFastPlot as dfp
from dSolveAndPlot import dSolveAndDetailedPlotAndHoldOn as ddp

def decayFunc0(tau):
    return lambda t,x: -tau*x



    
def decayFunc4(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA, 0],[1./tauA,-1./tauB]]),nab)
    
def decayFunc5(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA,1./tauB],[1./tauA,-1./tauB]]),nab)

def populationGrowth(a,b):
    return lambda t,n: a*n - b*n*n
    

"""

def freeFallingFunc1():
    return lambda t,x: -9.8
#dfp(freeFallingFunc1(), 0, 10.,0.05,"ForwardEuler")
"""
#'''
def airDragedFallingFunc3(a,b):
    return lambda t,v: a - b * v
'''    
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.5,"ForwardEuler",\
    ["step size = 0.5"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.1,"ForwardEuler",\
    ["step size = 0.05"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.005,"ForwardEuler",\
    ["step size = 0.005"],"t/s", "v/m.s-1","air Draged Falling")
fig.savefig("a.png")
plt.show()
'''
stpsz = 0.8

ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"ForwardEuler",\
    ["ForwardEuler"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"ExplicitTrapezoidal",\
    ["ExplicitTrapezoidal"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"Midpoint",\
    ["Midpoint"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"RK4",\
    ["RK4"])

xx = np.linspace(0., 8., 256, endpoint=True)
print xx
vv =9.8 -9.8*np.exp(-xx)
print vv
plt.plot(xx,vv,label = "real solution")
plt.legend(loc='upper right', frameon=False)
plt.show()

#'''
'''
def decayFunc4(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA, 0],[1./tauA,-1./tauB]]),nab)
dfp(decayFunc4(1.,1.), array([1.5,0.]), 10.,0.05,"RK4")
'''
def decayFunc5(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA,1./tauB],[1./tauA,-1./tauB]]),nab)
ddp(decayFunc5(1.,1.5), array([2.0,0.5]), 5.,0.05,"RK4",["N_A","N_B"],"t/s","N/1")
"""
dSolveAndHoldOn(decayFunc0(1.), 1, 5.,0.05,"ForwardEuler")

dSolveAndHoldOn(decayFunc0(0.5), 1, 5.,0.05,"ForwardEuler")
plt.show()
dSolveAndPlot(decayFunc5(1.,1.), array([1.5,1]), 5.,0.05)
dSolveAndHoldOn(decayFunc5(1.,1.), array([1.5,1]), 5.,0.05, "RK4")
plt.show()
dSolveAndPlotWithLabelAndHoldOn(decayFunc5(1.,1.), array([1.5,1]), 5.,0.05, "RK4",\
    ["c","s"], "x", "y", "tt")
"""
'''
print dSolve(populationGrowth(10.,1.2), 1, 5., 0.05, "ForwardEuler")
dSolveAndPlot(populationGrowth(5.,0.5), 1., 2., 0.05,"ForwardEuler")
# print populationGrowth(10.,1.)(0,12)
'''