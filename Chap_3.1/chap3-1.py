# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:39:31 2016

@author: Wang Ziang
"""
import numpy as np
array = np.array
import math
from dSolve_2 import *
import matplotlib.pyplot as plt
from dSolveAndPlot import dSolutionFastPlot as dfp
from dSolveAndPlot import detailedDSolutionPlotAndHoldOn as ddp
from dSolveAndPlot import *
from scipy.optimize import minimize
from scipy.optimize import bisect
from scipy.optimize import newton



'''
fd = drivingForceAmplitude
omgd = drivingForceFrequency
gOverL
q = dampingParameter
'''
deg = math.pi / 180.

def forcedDampedLinearPendulum(omgd, fd, q, gOverL):
    def foo(t,X):
        [omega, theta] = X
        return array([- gOverL*theta - q*omega + fd*math.sin(omgd*t), omega])
    return foo
'''    
def simpleLinearPendulum(gOverL):
    return forcedDampedLinearPendulum(0, 0, gOverL, 0)
'''
def simpleLinearPendulum(gOverL = 9.8):
    def foo(t,X):
        [omega, theta] = X
        return array([-gOverL*theta, omega])
    return foo

def oneDimNewtonPhaseSpaceSolutionPrintAndHoldOn(ans1, \
    legendC = "", xLabel = "theta/1", yLabel = "omaga/ 1/s", titleLabel = "Phase Diagram"):
    easyPlotXYHoldON(getXiList(ans1,2),getXiList(ans1,1),legendC, xLabel,yLabel, titleLabel)

'''
#different mathod
stepSize = 0.01
tMax = 10.

ans1 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "RK4")
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "ForwardEuler")
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])

# Omega
ddp(ans2Omega,["ForwardEuler"], xLabel = "t/s", yLabel = "Omega/ 1/s")
ddp(ans1Omega,["RK4"], xLabel = "t/s", yLabel = "Omega/ 1/s")
done()

# Theta
ddp(ans2Theta,["ForwardEuler"], xLabel = "t/s", yLabel = "Theta/ 1")
ddp(ans1Theta,["RK4"], xLabel = "t/s", yLabel = "Theta/ 1")
done()

# phase diag
easyPlotXYHoldON(getXiList(ans2,2),getXiList(ans2,1), "ForwardEuler","Theta/ 1","Omega/ 1/s", "Phase Diagram")
easyPlotXYHoldON(getXiList(ans1,2),getXiList(ans1,1), "RK4","Theta/ 1","Omega/ 1/s", "Phase Diagram")
done()

#evenmore
stepSize = 0.01
tMax = 20.

ans1 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "RK4")
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])
# Omega
ans2 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "ForwardEuler")
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])
# Theta
ddp(ans2Theta,["ForwardEuler"], xLabel = "t/s", yLabel = "Theta/ 1")
ddp(ans1Theta,["RK4"], xLabel = "t/s", yLabel = "Theta/ 1")
done()
'''


'''
# dumping
fd = 0.0
omgd = 2.
gOverL = 9.8
q = 0.5

stepSize = 0.01
tMax = 30.

ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")
oneDimNewtonPhaseSpaceSolutionPrintAndHoldOn(ans1)
done()
ans1Theta = reduceStateList(ans1, [1])
ddp(ans1Theta,[""], xLabel = "t/s", yLabel = "Theta/ 1")
done()

q = 9.
tMax = 8.
ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")
oneDimNewtonPhaseSpaceSolutionPrintAndHoldOn(ans1)
plt.xlim(-0.1,0.1)
plt.ylim(-0.3,0.3)
done()
ans1Theta = reduceStateList(ans1, [1])
ddp(ans1Theta,[""],xLabel = "t/s", yLabel = "Theta/ 1")
done()
'''

# without periodic check
def amplitude(ans1, omegd, stepSize):
    takeLength =int(round(2 * (2*math.pi/omgd)/stepSize))
    ans1 = ans1[- takeLength :-1]
    xList = getXiList(ans1, 2)
    return (max(xList)-min(xList))/2.


'''
# forced
fd = 1.
omgd = 2.
gOverL = 9.8
q = 1.

stepSize = 0.01
tMax = 30.

    
ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")
# amplitude(ans1, omgd, stepSize)
oneDimNewtonPhaseSpaceSolutionPrintAndHoldOn(ans1)
done()
ans1Theta = reduceStateList(ans1, [1])
ddp(ans1Theta,[""],xLabel = "t/s", yLabel = "Theta/ 1")
done()
'''


'''
omgList = (np.linspace(0.5, 10., 100)).tolist()
ampList = []
fd = 1.
# omgd = 1.
gOverL = 9.8
q = 1.

stepSize = 0.01
tMax = 30.

for omgd in omgList:
    ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")
    ampList.append(amplitude(ans1, omgd, stepSize))

easyPlotXYHoldON(omgList, ampList, legendC = "", xLabel = "OmegaF / 1/s", yLabel = "Amplitude / 1", titleLabel = "Amplitude with different OmegaF")

'''

