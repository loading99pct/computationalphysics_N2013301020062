import numpy as np
array = np.array
import math
from dSolve_1 import *
import matplotlib.pyplot as plt
from dSolveAndPlot import dSolutionFastPlot as dfp
from dSolveAndPlot import detailedDSolutionPlotAndHoldOn as ddp
from dSolveAndPlot import easyPlotXYHoldON
from scipy.optimize import minimize
from scipy.optimize import bisect
from scipy.optimize import newton
'''
Ex. 2.9
'''
'''
def airDrugedTrajConstB2(B2OverM, g):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        return array([-B2OverM*v*vx, -g -B2OverM*v*vy, vx, vy])
    return foo
    
def airDrugedTrajVarB2(B2OverM0, g):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        uniRho = (1 - 6.5e-3 * y / 288.15) ** 2.5
        return array([-B2OverM0 * uniRho * v * vx, -g -B2OverM0 * uniRho * v * vy, vx, vy])
    return foo

def stopQ(state):
    return getT(state) != 0 and getX(state)[3] <= 0

def stopAltitudeQ(state, h):
    return 

#1.with or without Varied B2(h)#
ans1 = dSolveUntil(airDrugedTrajConstB2(4.0e-5, 9.8), array([700.,700.,0.,0.]), 0.05,stopQ)
ans1v = reduceStateList(ans1, [0,1])
ans1x = reduceStateList(ans1, [2,3])

ans2 = dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([700.,700.,0.,0.]), 0.5,stopQ, tMax = 200)
ans2v = reduceStateList(ans2, [0,1])
ans2x = reduceStateList(ans2, [2,3])

# V-T
ddp(ans1v,["vx Constant B2","vy Constant B2"])
ddp(ans2v,["vx Varied B2(h)","vy Varied B2(h)"],"t/s", "v/ m/s","V-T")
plt.show() 

# X-T
ddp(ans1x,["x Constant B2","y Constant B2"])
ddp(ans2x,["x Varied B2(h)","y Varied B2(h)"],"t/s", "x/m","X - T & Y - T")
plt.show() 

# Y-X
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Constant B2")
easyPlotXYHoldON(getXiList(ans2x,1),getXiList(ans2x,2), "Varied B2(h)","x/m","y/m", "Y - X")
plt.show() 
'''

'''
#2.different theta#
def solveTrajectoryByAngle(speed, angle):
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([vx,vy,0.,0.]), 0.05,stopQ)
    

for angle in range(10,90,10):
    ans1 = solveTrajectoryByAngle(700., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Theta = "+str(angle),"x/m","y/m", "Y - X")
plt.ylim(0,15000)
plt.show() 

for angle in range(10,90,3):
    ans1 = solveTrajectoryByAngle(700., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"","x/m","y/m", "Y - X")
plt.ylim(0,15000)
plt.show() 
'''
'''
#landing point, max l p #
def landingX(result):
    finalState = result[-1]
    return getX(finalState)[2]

def landingPointByAngle(speed, angle):
    return landingX(solveTrajectoryByAngle(speed, angle))

n = 100
thetaList = [(i * 90. / n) for i in range(n)]
landingList = map(lambda angle: landingPointByAngle(700., angle), thetaList)
easyPlotXYHoldON(thetaList, landingList, "","x/m","theta/degree", "X_landing - Theta")
plt.show()

landFarestTheta = - minimize(lambda angle: -landingPointByAngle(700., angle),- 40., method='Nelder-Mead', tol=1e-3).x

print landFarestTheta
print landingPointByAngle(700., 43.531)
'''
'''
#shoot a given point #

def solvediffByAngle(speed, angle,xTarget, yTarget):
    def stop2Q(state,xm):
        return getX(state)[2] >= xm 
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    ans = dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([vx,vy,0.,0.]), 0.5,lambda x:stop2Q(x,xTarget),tMax = 3000)
    finalState = ans[-1]
    diff =  getX(finalState)[3] - yTarget
    return diff

def solveTrajectoryByAngleQ2(speed, angle,xTarget, yTarget):
    def stop2Q(state,xTarget):
        return getX(state)[2] >= xTarget 
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([vx,vy,0.,0.]), 0.05,lambda s:stop2Q(s,xTarget))

vel = 500.
xTarget = 10000.
yTarget = 4000.

theta1 = bisect(lambda a: solvediffByAngle(vel, a, xTarget, yTarget),40.,50.)
theta2 = bisect(lambda a: solvediffByAngle(vel, a, xTarget, yTarget),60.,70.)

ans1 = solveTrajectoryByAngleQ2(vel, theta1, xTarget, yTarget)
ans1x = reduceStateList(ans1, [2,3])
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"theta = "+str(theta1),"x/m","y/m", "Y - X")

ans1 = solveTrajectoryByAngleQ2(vel, theta2, xTarget, yTarget)
ans1x = reduceStateList(ans1, [2,3])
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"theta = "+str(theta2),"x/m","y/m", "Y - X")
plt.ylim(0,9000)
plt.show()

'''
print theta1,theta2