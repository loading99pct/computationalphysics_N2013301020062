import random, math, pylab

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

L = 12
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}
n_spins_to_flip = N * 500
list_T = [1.0 + 0.2 * i for i in range(15)]
list_av_m = []
S = [random.choice([1, -1]) for k in range(N)]
M = sum(S)


list_Z = []
list_cv = []
list_E_av = []
list_E2_av = []



for T in list_T:
    print T
    
    Z = 0.0
    E_av = 0.0
    M_av = 0.0
    E2_av = 0.0
    
    
    
    p  = 1.0 - math.exp(-2.0 / T)
    M_tot = 0.0
    n_flipped_spins = 0
    nsteps = 0
    while n_flipped_spins < n_spins_to_flip:
        k = random.randint(0, N - 1)
        Pocket, Cluster = [k], [k]
        while Pocket != []:
            j = random.choice(Pocket)
            for l in nbr[j]:
                if S[l] == S[j] and l not in Cluster and random.uniform(0.0, 1.0) < p:
                    Pocket.append(l)
                    Cluster.append(l)
            Pocket.remove(j)
        for j in Cluster:
            S[j] *= -1
        M -= 2 * len(Cluster) * S[k]
        n_flipped_spins += len(Cluster)
        M_tot += abs(M)
        nsteps += 1
        
        
        E = energy(S, N, nbr)
        weight = math.exp(- E / T)
        Z += weight
        E_av += weight * E
        E2_av += weight * E ** 2
        
    E2_av /= Z
    E_av /= Z
    cv = (E2_av - E_av ** 2) / N / T ** 2
    
    list_E_av.append(E_av)
    list_E2_av.append(E2_av)
    list_cv.append(cv)
    list_Z.append(Z)
        
        
    list_av_m.append(M_tot / float(nsteps) / N)
    
pylab.plot(list_T, list_av_m, 'bo-', clip_on=False)
pylab.title('%i x %i lattice (periodic boundary conditions)' % (L, L))
pylab.xlabel('$T$', fontsize=16)
pylab.ylabel('$<|M|>/N$', fontsize=16)
pylab.savefig('plot_cluster_av_magnetization_L%i.png' % L)


'''
list_cv = []
for T in list_T:
    Z = 0.0
    E_av = 0.0
    M_av = 0.0
    E2_av = 0.0
    for E in dos.keys():
        weight = math.exp(- E / T) * dos[E]
        Z += weight
        E_av += weight * E
        E2_av += weight * E ** 2
    E2_av /= Z
    E_av /= Z
    cv = (E2_av - E_av ** 2) / N / T ** 2
    list_cv.append(cv)
'''
import matplotlib.pyplot as plt
from dSolveAndPlot import *

pylab.plot(list_T, list_cv, 'bo-', clip_on=False)
plt.show()

easyPlotXYHoldON(list_T, list_cv,"M vs. n", "step", "Total magnetization")
plt.show()