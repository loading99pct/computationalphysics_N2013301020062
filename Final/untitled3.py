# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 01:08:04 2016

@author: Administrator
"""

import random, math
import matplotlib.pyplot as plt
from dSolveAndPlot import *

L = 15
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
                                        
MTrace = []
nsteps = 800000
T = 0.2
beta = 1.0 / T
S = [random.choice([1, -1]) for k in range(N)]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1
    MTrace.append(sum(S))
# print S, sum(S)


easyPlotXYHoldON(range(nsteps), MTrace,"M vs. n", "step", "Total magnetization")
plt.show()
