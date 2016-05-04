
# 有阻尼周期驱动下的简单摆 #

以前的作业中，我们已经定义了在给定时间区间内求解一般微分方程的函数dSolve，   
   
[dSolve in Chap1](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/chap-1)   
   
借助之前的求解方法函数，定义函数dSolveUntil, 此函数不断迭代，直到状态（t,X）满足某个条件stopQ,   
返回解列表，此函数结构由nestUntilList给出   
   
已经定义了dSolveUntil,它和dSolve一样可以调用四种求解方法，默认采用 RK-4 求解   
[dSolveUntil in Chap2](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/Chap_2.1)   
   
   

本次作业中：   
1, 不同方法求解简单摆运动的准确性   
2, 有阻尼的单摆运动   
3, 有阻尼且有周期性驱动力的单摆运动， 以及不同驱动力周期下的稳定振幅     

## 不同方法求解简单摆运动的准确性 ##

dSolve可以调用四种求解方法，默认采用 RK-4 求解   

定义简单摆的运动微分方程（被映射为某个函数）   


```python

def simpleLinearPendulum(gOverL = 9.8):
    def foo(t,X):
        [omega, theta] = X
        return array([-gOverL*theta, omega])
    return foo

```

分别讨论用 RK4 和 前步欧拉法 求解  

stepSize = 0.01   
tMax = 10.   

分别用两种方法求解运动方程    


```python
ans1 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "RK4")
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = dSolve(simpleLinearPendulum(20.), array([0, 5*deg]), tMax, stepSize, method = "ForwardEuler")
ans2Omega = reduceStateList(ans2, [0])
ans2Theta = reduceStateList(ans2, [1])
```

分别画出角速度随时间变化,角度随时间变化，以及相空间轨迹    


```python
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
```

角速度随时间变化    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/1-different-theta-v.png)   

角度随时间变化   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/1-different-theta-x.png)   

相图   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/1-different-theta-ph.png)   

当求解时间更长时，欧拉法误差发散更大，RK4仍无明显发散   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/1-different-theta-x2.png)   

## 有线性阻尼的单摆运动 ##

定义有阻尼周期驱动的运动方程   


```python

def forcedDampedLinearPendulum(omgd, fd, q, gOverL):
    def foo(t,X):
        [omega, theta] = X
        return array([- gOverL*theta - q*omega + fd*math.sin(omgd*t), omega])
    return foo

```

设周期力为零，仅存在阻尼，求解运动方程    

1，欠阻尼


```python

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

```

角度随时间关系：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/2-dumping-x-1.png)   

相空间轨迹：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/2-dumping-ph-1.png)   

1，过阻尼   


```python

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

```

角度随时间关系：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/2-dumping-x-2.png)   

相空间轨迹：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/2-dumping-ph-2.png)   

##  有阻尼且有周期性驱动力的单摆运动， 以及不同驱动周期下的稳定振幅 ##

周期性驱动力下的运动   


```python

# forced
fd = 1.
omgd = 2.
gOverL = 9.8
q = 1.

stepSize = 0.01
tMax = 30.

    
ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")


```

角度随时间关系   


```python

ans1Theta = reduceStateList(ans1, [1])
ddp(ans1Theta,[""],xLabel = "t/s", yLabel = "Theta/ 1")
done()

```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/3-forced-x.png)   

相空间轨迹   


```python

oneDimNewtonPhaseSpaceSolutionPrintAndHoldOn(ans1)
done()

```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/3-forced-ph.png)   

定义计算振幅的函数   


```python

def amplitude(ans1, omegd, stepSize):
    takeLength =int(round(2 * (2*math.pi/omgd)/stepSize))
    ans1 = ans1[- takeLength :-1]
    xList = getXiList(ans1, 2)
    return (max(xList)-min(xList))/2.

```

得到不同驱动周期下的稳定振幅   

参数：   
fd = 1.   
gOverL = 9.8   
q = 1.   
   
stepSize = 0.01   
tMax = 30.   


```python

omgList = (np.linspace(0.5, 10., 100)).tolist()
ampList = []

for omgd in omgList:
    ans1 = dSolve(forcedDampedLinearPendulum(omgd, fd, q, gOverL), array([0, 5*deg]), tMax, stepSize, method = "RK4")
    ampList.append(amplitude(ans1, omgd, stepSize))

easyPlotXYHoldON(omgList, ampList, legendC = "", xLabel = "OmegaF / 1/s", yLabel = "Amplitude / 1", titleLabel = "Amplitude with different OmegaF")


```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.1/pictures/4-A-vs-omg.png)   
