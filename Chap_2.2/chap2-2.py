import numpy as np
array = np.array
import math
from dSolve_2 import *
import matplotlib.pyplot as plt
from dSolveAndPlot import dSolutionFastPlot as dfp
from dSolveAndPlot import detailedDSolutionPlotAndHoldOn as ddp
from dSolveAndPlot import easyPlotXYHoldON
from scipy.optimize import minimize
from scipy.optimize import bisect
from scipy.optimize import newton
'''
Ex. 2.19
'''

def rpm(r):
    return r*2*math.pi/60.
def B2OverM(v):
    return 0.0039+0.0058/(1+math.exp(v-35.0/5.0))

def airDrugedSpinTraj(omega, s0OverM = 4.1e-4, g = 9.8):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        return array([-B2OverM(v)*v*vx - s0OverM*omega*vy, -g -B2OverM(v)*v*vy + s0OverM*omega*vx, vx, vy])
    return foo

def stopQ(state):
    return getT(state) != 0 and getX(state)[3] <= 0

'''
#1.with or without Spin#
vx0 = 50.
vy0 = 50.
omega = 2000.
ans1 = dSolveUntil(airDrugedSpinTraj(rpm(omega)), array([vx0,vy0,0.,0.]), 0.05,stopQ)
ans1v = reduceStateList(ans1, [0,1])
ans1x = reduceStateList(ans1, [2,3])

ans2 = dSolveUntil(airDrugedSpinTraj(0.), array([vx0,vy0,0.,0.]), 0.05,stopQ)
ans2v = reduceStateList(ans2, [0,1])
ans2x = reduceStateList(ans2, [2,3])

# V-T
ddp(ans1v,["vx with spin","vy with spin"])
ddp(ans2v,["vx without spin","vy without spin"],"t/s", "v/ m/s","V-T")
plt.show() 

# X-T
ddp(ans1x,["x with spin","y with spin"])
ddp(ans2x,["x without spin","y without spin"],"t/s", "x/m","X - T & Y - T")
plt.show() 

# Y-X
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "with spin")
easyPlotXYHoldON(getXiList(ans2x,1),getXiList(ans2x,2), "without spin","x/m","y/m", "Y - X")
plt.show() 

'''

#2.different theta#
def solveTrajectoryByAngle(speed, rpmval, angle):
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedSpinTraj(rpm(rpmval)), array([vx,vy,0.,0.]), 0.05,stopQ)
    
'''
for angle in range(10,90,10):
    ans1 = solveTrajectoryByAngle(70., 2000., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Theta = "+str(angle),"x/m","y/m", "Y - X")
plt.xlim(-20,260)
plt.ylim(0,150)
plt.show() 


for angle in range(0,90,2):
    ans1 = solveTrajectoryByAngle(70.,2000., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "","x/m","y/m", "Y - X")
plt.xlim(-50,260)
plt.ylim(0,150)
plt.show() 

for angle in range(0,90,2):
    ans1 = solveTrajectoryByAngle(70.,5000., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "","x/m","y/m", "Y - X")
plt.xlim(-100,320)
plt.ylim(0,150)
plt.show() 
'''
'''
# different omega
for omega in range(0,9000,1000):
    ans1 = solveTrajectoryByAngle(70., omega, 45.)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Omega = "+str(omega),"x/m","y/m", "Y - X")
plt.xlim(-20,260)
plt.ylim(0,150)
plt.show() 
'''
'''
# special
ans1 = solveTrajectoryByAngle(70., 15000., 45.)
ans1x = reduceStateList(ans1, [2,3])
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Omega = "+str(omega),"x/m","y/m", "Y - X")
plt.xlim(-50,360)
plt.ylim(0,150)
plt.show() 
'''
'''
#landing point, max l p #
def landingX(result):
    finalState = result[-1]
    return getX(finalState)[2]

def landingPointByAngle(speed, rpmval, angle):
    return landingX(solveTrajectoryByAngle(speed, rpmval, angle))

n = 100
thetaList = [(i * 90. / n) for i in range(n)]
landingList = map(lambda angle: landingPointByAngle(70., 2000., angle), thetaList)
easyPlotXYHoldON(thetaList, landingList, "","theta/degree","x/m", "X_landing - Theta")
plt.show()

n = 100
thetaList = [(i * 90. / n) for i in range(n)]
landingList = map(lambda angle: landingPointByAngle(70., 12000., angle), thetaList)
easyPlotXYHoldON(thetaList, landingList, "","theta/degree","x/m", "X_landing - Theta")
plt.show()
'''
'''
landFarestTheta = - minimize(lambda angle: -landingPointByAngle(700., angle),- 40., method='Nelder-Mead', tol=1e-3).x

print landFarestTheta
print landingPointByAngle(700., 43.531)
'''