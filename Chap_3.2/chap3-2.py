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

def forcedDampedNonlinearPendulum(omgd, fd = 1.2, q = 0.5 , gOverL = 1.):
    def foo(t,X):
        [omega, theta] = X
        return array([- gOverL*math.sin(theta) - q*omega + fd*math.sin(omgd*t), omega])
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


def modSolution(solution):
	"""
	mod the solution to interval (-pi, pi)
	pre: solution = [ [ti, array([omegai, thetai])], ...  ]
	post: return ...
	"""
	sol = solution[:];
	xi = getXiList(sol, 2);
	mxi = np.remainder( (array(xi) + math.pi).tolist(), 2 * math.pi) - math.pi
	for i in range(len(sol)):
		sol[i][1][1] = mxi[i]
	return sol

def specialPlotForm(solution, nanForm = [np.nan, array([np.nan, np.nan])] ):
	sol = solution[:];
	xi = getXiList(sol, 2);
	# print xi
	pos = np.where(np.abs(np.diff(xi))>6.)[0]+1
	# print pos
	# print nanForm
	# print sol[0]
	for i in pos[::-1]:
		sol.insert(i, nanForm)
	return sol

'''
#different initial
stepSize = 0.01
tMax = 80.

ans1 = dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.20]), tMax, stepSize, method = "RK4")
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.21]), tMax, stepSize, method = "RK4")
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])

# Omega
ddp(ans2Omega,[ "init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Omega/ 1/s")
ddp(ans1Omega,[ "init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Omega/ 1/s")
done()

# Theta
ddp(ans2Theta,["init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Theta/ 1")
ddp(ans1Theta,["init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Theta/ 1")
done()

# mod-theta
stepSize = 0.01
tMax = 80.

ans1 = modSolution( dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.20]), tMax, stepSize, method = "RK4") )
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = modSolution( dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.21]), tMax, stepSize, method = "RK4") )
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])

ddp(ans2Theta,["init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Theta/ 1")
ddp(ans1Theta,["init = (omaga=0.0, theta=0.20)"], xLabel = "t/s", yLabel = "Theta/ 1")
done()
'''

def fEqQ(floot1, floot2):
	return abs(floot2 - floot1) < 1e-2
def poincareSection(solution, omgd, phase = 0., tmin = 50):
	def mulOfTQ(t, omgd):
		n = (t - phase/omgd)/ (2*math.pi/omgd)
		return fEqQ(round(n), n)
	n = len(solution)
	sol = solution#[int(round(0.2*n)):-1]
	sectionPoints = filter(lambda state: mulOfTQ(getT(state), omgd) and getT(state) > tmin, sol)
	print phase
	return sectionPoints




'''
# Omega
ddp(ans2Omega,["ForwardEuler"], xLabel = "t/s", yLabel = "Omega/ 1/s")
ddp(ans1Omega,["RK4"], xLabel = "t/s", yLabel = "Omega/ 1/s")
done()

# Theta
ddp(ans2Theta,["ForwardEuler"], xLabel = "t/s", yLabel = "Theta/ 1")
ddp(ans1Theta,["RK4"], xLabel = "t/s", yLabel = "Theta/ 1")
done()

stepSize = 0.01
tMax = 180.


ans1 = modSolution( dSolve(forcedDampedNonlinearPendulum(2./3.), array([0, 0.2]), tMax, stepSize, method = "RK4") )
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = modSolution( dSolve(forcedDampedNonlinearPendulum(2./3.), array([0, 0.21]), tMax, stepSize, method = "RK4") )
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])
# phase diag

ans1 = specialPlotForm(ans1)
ans2 = specialPlotForm(ans2)

easyPlotXYHoldON(getXiList(ans2,2),getXiList(ans2,1), "init = (omaga=0.0, theta=0.20)","Theta/ 1","Omega/ 1/s", "Phase Diagram")
easyPlotXYHoldON(getXiList(ans1,2),getXiList(ans1,1), "init = (omaga=0.0, theta=0.21)","Theta/ 1","Omega/ 1/s", "Phase Diagram")
done()
'''

'''
omgd = 2./3.
ppp = 50.
stepSize = 2* math.pi/omgd/ ppp
tMax = 100000.

frameN = 400

i = 2.001
ans = dSolve(forcedDampedNonlinearPendulum(omgd, fd = 1.2), array([0., 0.20]), tMax, stepSize, method = "RK4")
ans = modSolution(ans)
pSec = poincareSection(modSolution(ans), omgd,i * math.pi / 4.)
easyScatterPlotXYHoldON(getXiList(pSec,2),getXiList(pSec,1), "phase = "+ str(2)+" *Pi/4","Theta/ 1","Omega/ 1/s", "Phase Diagram")
done()

### i = 2.0 wrong!!!!! 
# for i in range(5):
# 	pSec = poincareSection(modSolution(ans), omgd,i * math.pi / 4.)
# 	easyScatterPlotXYHoldON(getXiList(pSec,2),getXiList(pSec,1), "phase = "+ str(i)+" *Pi/4","Theta/ 1","Omega/ 1/s", "Phase Diagram")
# 	done()
'''




# p section
# stepSize = 0.05
# tMax = 80.
omgd = 2./3.
ppp = 50.
stepSize = 2* math.pi/omgd/ ppp
tMax = 10000.

frameN = 400


ans = dSolve(forcedDampedNonlinearPendulum(omgd, fd = 1.2), array([0., 0.20]), tMax, stepSize, method = "RK4")
ans = modSolution(ans)
phaseL = np.linspace(0, 2*math.pi, frameN, endpoint = 1).tolist()
dataL = [poincareSection(ans, omgd, phase) for phase in phaseL]

phaseLInPlot = [ph / math.pi for ph in phaseL]



# easyPlotXYHoldON(getXiList(ans,2),getXiList(ans,1), "init = (omaga=0.0, theta=0.21)","Theta/ 1","Omega/ 1/s", "Phase Diagram")
# done()
# pSec = poincareSection(modSolution(ans), omgd,0. *math.pi)
# easyScatterPlotXYHoldON(getXiList(pSec,2),getXiList(pSec,1), "init = (omaga=0.0, theta=0.20)","Theta/ 1","Omega/ 1/s", "Phase Diagram")
# done()

from matplotlib import animation


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-math.pi, math.pi), ylim=(-2.5, 2.5))
line, = ax.plot([], [], 'o', markersize = 1.1 )
ph = ax.text(1.5,2.,'')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    ph.set_text("")
    return line, ph

# animation function.  This is called sequentially
def animate(i):
    pSec = dataL[i]
    x = getXiList(pSec, 2)
    y = getXiList(pSec, 1)
    line.set_data(x, y)
    ph.set_text('phase = %.3f Pi' % phaseLInPlot[i])#
    return line, ph

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frameN, interval=1, blit=True)

# anim.save('p-section.mp4', fps=25)
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html

plt.show()


