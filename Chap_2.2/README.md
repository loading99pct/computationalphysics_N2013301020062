
# 旋转物体的有阻尼抛体问题 #

以前的作业中，我们已经定义了在给定时间区间内求解一般微分方程的函数dSolve，   
   
[dSolve in Chap1](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/chap-1)   
   
本次作业中，借助之前的求解方法函数，定义函数dSolveUntil, 此函数不断迭代，直到状态（t,X）满足某个条件stopQ,   
返回解列表，此函数结构由nestUntilList给出   
   
修改画图函数，解除耦合，提取公因子；   
定义函数easyPlotXYHoldON;   
dSolutionFastPlot   
dSolutionPlotAndHoldOn   
detailedDSolutionPlotAndHoldOn    

上次作业中   
已经定义了dSolveUntil,它和dSolve一样可以调用四种求解方法，默认采用 RK-4 求解   
[dSolveUntil in Chap2](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/Chap_2.1)   
   
   

本次作业中：   
1, 物体有无旋转时的运动   
2, 给定速度以及旋转速度，不同发射角度下的运动   
3, 给定速度以及旋转速度，不同发射角度下的落地点，以及最远落地点   
4, 给定速度以及发射角度，不同旋转速度下的运动   

## 物体有无旋转时的运动 ##

已经定义了dSolveUntil,它和dSolve一样可以调用四种求解方法，默认采用 RK-4 求解   

定义有无旋转时的运动微分方程（被映射为某个函数）   


```python

def airDrugedSpinTraj(omega, s0OverM = 4.1e-4, g = 9.8):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        return array([-B2OverM(v)*v*vx - s0OverM*omega*vy, -g -B2OverM(v)*v*vy + s0OverM*omega*vx, vx, vy])
    return foo

```

落地条件（针对某一状态的谓词函数），通过这个停止条件，求解将一直进行直到物体落地   


```python
def stopQ(state):
    return getT(state) != 0 and getX(state)[3] <= 0
```

在vx0 = 50 m/s, vy0 = 50 m/s, 转速omega = 2000 rpm, 分别求解有无旋转的运动方程    


```python
ans1 = dSolveUntil(airDrugedSpinTraj(rpm(omega)), array([vx0,vy0,0.,0.]), 0.05,stopQ)
ans1v = reduceStateList(ans1, [0,1])
ans1x = reduceStateList(ans1, [2,3])

ans2 = dSolveUntil(airDrugedSpinTraj(0.), array([vx0,vy0,0.,0.]), 0.05,stopQ)
ans2v = reduceStateList(ans2, [0,1])
ans2x = reduceStateList(ans2, [2,3])
```

分别画出速度随时间变化,位置随时间变化，以及运动轨迹    


```python
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
```

速度随时间变化    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/1-with-and-without-spin-v.png)   

位置随时间变化   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/1-with-and-without-spin-x.png)   

运动轨迹   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/1-with-and-without-spin-traj.png)   

## 给定速度以及旋转速度，不同发射角度下的运动    ##

定义通过给定角度和转速求解运动方程（直到落地）的函数   


```python
def solveTrajectoryByAngle(speed, rpmval, angle):
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedSpinTraj(rpm(rpmval)), array([vx,vy,0.,0.]), 0.05,stopQ)
```

速度默认70 m/s, 转速omega = 2000, 调整发射角度，求得轨迹如下   


```python
for angle in range(10,90,10):
    ans1 = solveTrajectoryByAngle(70., 2000., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Theta = "+str(angle),"x/m","y/m", "Y - X")
plt.xlim(-20,260)
plt.ylim(0,150)
plt.show() 
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/2-different-angle-1.png)   

加密发射角度的采样（角度从0 到 90 度），得到轨迹的包络，这是物体可达到的范围   


```python
for angle in range(0,90,2):
    ans1 = solveTrajectoryByAngle(70.,2000., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "","x/m","y/m", "Y - X")
plt.xlim(-50,260)
plt.ylim(0,150)
plt.show() 
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/2-different-angle-2.png)   

将转速改为5000. （角度从0 到 90 度）得到包络：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/2-different-angle-3.png)   

## 给定速度以及旋转速度，不同发射角度下的落地点，以及最远落地点    ##

定义通过给定解提取落地点距离的函数   


```python

def landingX(result):
    finalState = result[-1]
    return getX(finalState)[2]

```

从而定义给定速度，旋转速度，发射角度，给出落地距离的函数   


```python

def landingPointByAngle(speed, rpmval, angle):
    return landingX(solveTrajectoryByAngle(speed, rpmval, angle))

```

画出落地点关于发射角度（在给定速度v = 70.m/s， 转速2000.）的关系


```python
n = 100
thetaList = [(i * 90. / n) for i in range(n)]
landingList = map(lambda angle: landingPointByAngle(70., 2000., angle), thetaList)
easyPlotXYHoldON(thetaList, landingList, "","theta/degree","x/m", "X_landing - Theta")
plt.show()
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/4-landing-point-1.png)   

画出落地点关于发射角度（在给定速度v = 70.m/s， 转速12000.）的关系   


```python
n = 100
thetaList = [(i * 90. / n) for i in range(n)]
landingList = map(lambda angle: landingPointByAngle(70., 12000., angle), thetaList)
easyPlotXYHoldON(thetaList, landingList, "","theta/degree","x/m", "X_landing - Theta")
plt.show()

```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/4-landing-point-2.png)   

突变原因如下一节解释。   

##  给定速度以及发射角度，不同旋转速度下的运动 ##

在v=70m/s,发射角度45度时， 改变转速omega   


```python

for omega in range(0,9000,1000):
    ans1 = solveTrajectoryByAngle(70., omega, 45.)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Omega = "+str(omega),"x/m","y/m", "Y - X")
plt.xlim(-20,260)
plt.ylim(0,150)
plt.show() 

```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/3-different-omega.png)   

当角速度足够大的时候：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.2/pictures/3-special.png)   

这解释了上一节落地点突变的原因。   
