
# 周期驱动有阻尼非线性单摆的混沌特性 #

以前的作业中，我们已经定义了在给定时间区间内求解一般微分方程的函数dSolve，   
   
[dSolve in Chap1](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/chap-1)   
   
借助之前的求解方法函数，定义函数dSolveUntil, 此函数不断迭代，直到状态（t,X）满足某个条件stopQ,   
返回解列表，此函数结构由nestUntilList给出   
   
已经定义了dSolveUntil,它和dSolve一样可以调用四种求解方法，默认采用 RK-4 求解   
[dSolveUntil in Chap2](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/Chap_2.1)   
   
   

本次作业中：   
1, 对初值的敏感依赖性   
2, 庞加莱截面        

## 对初值的敏感依赖性 ##

dSolve可以调用四种求解方法，默认采用 RK-4 求解   

定义周期驱动有阻尼非线性单摆的运动微分方程（被映射为某个函数）   


```python

def forcedDampedNonlinearPendulum(omgd, fd = 1.2, q = 0.5 , gOverL = 1.):
    def foo(t,X):
        [omega, theta] = X
        return array([- gOverL*math.sin(theta) - q*omega + fd*math.sin(omgd*t), omega])
    return foo

```

考虑在初始条件有微小差别下的情况，这里角度有细微差别   

[omega, theta] = [0., 0.20]   
[omega, theta] = [0., 0.21]   

分别用两个初值求解运动方程    


```python

ans1 = dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.20]), tMax, stepSize, method = "RK4")
ans1Omega = reduceStateList(ans1, [0])
ans1Theta = reduceStateList(ans1, [1])

ans2 = dSolve(forcedDampedNonlinearPendulum(2./3.), array([0., 0.21]), tMax, stepSize, method = "RK4")
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

角度随时间变化（未取模）  

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/1-theta.png)   

角度随时间变化（取模）   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/1-modTheta.png)   

角速度随时间变化    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/1-omega.png)   

相图   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/1-phase.png)   

可以看出，初始结果的微小差别会随着时间被放大，并占据主导   

## 庞加莱截面 ##

将庞加莱截面定义为对解的频闪提取   


```python

def poincareSection(solution, omgd, phase = 0., tmin = 50):
	def mulOfTQ(t, omgd):
		n = (t - phase/omgd)/ (2*math.pi/omgd)
		return fEqQ(round(n), n)
	n = len(solution)
	sol = solution#[int(round(0.2*n)):-1]
	sectionPoints = filter(lambda state: mulOfTQ(getT(state), omgd) and getT(state) > tmin, sol)
	return sectionPoints

```

求解运动方程，并提取出不同初始相位下的庞加莱截面，并画出如下    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection-0.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection-1.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection-2.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection-3.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection-4.png)   

以及，画出不同相位的动态图如下（gif，加载需要时间）   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_3.2/pictures/2-poincareSection.gif)   

从庞加莱截面的有序性可以看出，即使混沌之中，也存在规律   
