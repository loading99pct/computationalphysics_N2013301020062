
# 考虑空气阻力随高度变化下的抛体问题 #

上次作业中，我们已经定义了在给定时间区间内求解一般微分方程的函数dSolve，   
   
[dSolve in Chap1](https://github.com/loading99pct/computationalphysics_N2013301020062/tree/master/chap-1)   
   
本次作业中，借助之前的求解方法函数，定义函数dSolveUntil, 此函数不断迭代，直到状态（t,X）满足某个条件stopQ,   
返回解列表，此函数结构由nestUntilList给出   
   
修改画图函数，解除耦合，提取公因子；   
定义函数easyPlotXYHoldON;   
dSolutionFastPlot   
dSolutionPlotAndHoldOn   
detailedDSolutionPlotAndHoldOn    
   




本次作业中：   
1, 考虑/不考虑 空气随高度变化时的影响的运动   
   
以下考虑空气随高度变化时的影响的运动   
2, 给定速度，不同发射角度下的运动   
3, 给定速度，不同发射角度下的落地点，以及最远落地点  
4, 给定速度，改变角度以使物体的落地点在（X,Y），其中Y可与发射点不等高   

## 考虑/不考虑 空气随高度变化时的影响的运动 ##

已经定义了dSolveUntil,它和dSolve一样可以调用四种求解方法，默认采用 RK-4 求解   


```python
def dSolveUntil(func, x0, stepSize, stopQ, method = "RK4", tMax = 1000):
    '''
    doc: havent
    stopQ is about a state
    '''
    x0 = normalize(x0)
    maxStep = int(math.ceil(float(tMax) / stepSize))
    methodFunc = __methodDictionary[method]
    toNext = lambda state: methodFunc(state, func, stepSize)
    return nestUntilList(toNext, makeState(0, x0), stopQ, maxStep)
```

分别定义考虑/不考虑 空气随高度变化时的运动微分方程（被映射为某个函数）   

不考虑空气随高度变化   


```python
def airDrugedTrajConstB2(B2OverM, g):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        return array([-B2OverM*v*vx, -g -B2OverM*v*vy, vx, vy])
    return foo
    
```

考虑空气随高度变化


```python
def airDrugedTrajVarB2(B2OverM0, g):
    def foo(t,X):
        [vx,vy,x,y] = X
        v = math.sqrt(vx**2 + vy**2)
        uniRho = (1 - 6.5e-3 * y / 288.15) ** 2.5
        return array([-B2OverM0 * uniRho * v * vx, -g -B2OverM0 * uniRho * v * vy, vx, vy])
    return foo
```

落地条件（针对某一状态的谓词函数），通过这个停止条件，求解将一直进行直到物体落地   


```python
def stopQ(state):
    return getT(state) != 0 and getX(state)[3] <= 0
```

在vx = 700 m/s, vy = 700 m/s, 分别求解运动方程    


```python
ans1 = dSolveUntil(airDrugedTrajConstB2(4.0e-5, 9.8), array([700.,700.,0.,0.]), 0.05,stopQ)
ans1v = reduceStateList(ans1, [0,1])
ans1x = reduceStateList(ans1, [2,3])

ans2 = dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([700.,700.,0.,0.]), 0.5,stopQ, tMax = 200)
ans2v = reduceStateList(ans2, [0,1])
ans2x = reduceStateList(ans2, [2,3])
```

分别画出速度随时间变化,位置随时间变化，以及运动轨迹    


```python
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
```

速度随时间变化    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/1-with-or-without-1.png)   

位置随时间变化   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/1-with-or-without-2.png)   

运动轨迹   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/1-with-or-without-3.png)   

## 给定速度，求解不同发射角度下的运动 ##

定义通过给定角度求解运动方程（直到落地）的函数   


```python
def solveTrajectoryByAngle(speed, angle):
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([vx,vy,0.,0.]), 0.05,stopQ)
```

速度默认700 m/s, 调整发射角度，求得轨迹如下   


```python
for angle in range(10,90,10):
    ans1 = solveTrajectoryByAngle(700., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2), "Theta = "+str(angle),"x/m","y/m", "Y - X")
plt.ylim(0,15000)
plt.show() 
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/different-angle-1.png)   

加密发射角度的采样，得到轨迹的包络，这是物体可达到的范围   


```python
for angle in range(10,90,3):
    ans1 = solveTrajectoryByAngle(700., angle)
    ans1x = reduceStateList(ans1, [2,3])
    easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"","x/m","y/m", "Y - X")
plt.ylim(0,15000)
plt.show() 
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/different-angle-2.png)   

## 给定速度，不同发射角度下的落地点，以及最远落地点 ##

定义通过给定解提取落地点距离的函数   


```python

def landingX(result):
    finalState = result[-1]
    return getX(finalState)[2]

```

从而定义给定速度，发射角度，给出落地距离的函数   


```python

def landingPointByAngle(speed, angle):
    return landingX(solveTrajectoryByAngle(speed, angle))

```

画出落地点关于发射角度（在给定速度v = 700.m/s时）的关系

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/landing-point.png)    

求解最大距离时的反射角度，即是求解函数 lambda angle: landingPointByAngle(700., angle) 的最大值   


```python

landFarestTheta = maximize(lambda angle: landingPointByAngle(700., angle), 40., method='Nelder-Mead', tol=1e-6).x

```

最远射程对应的角度 landFarestTheta = -43.531   
最远射程： 24640.14 m   

##  给定速度，改变角度以使物体的落地点在（X,Y），其中Y可与发射点不等高 ##

此问题不是初值问题（IVP）,属于边界值问题（BVP），瞄准求解   

给定速度下，物体达到给定X_Tar位置时的Y位置是发射角度的函数,   
所以Y和Y_Tar的差值是发射角度的函数,   
当准确落在（X_Tar，Y_Tar），Y（theta） - Y_Tar == 0   
问题转化为求解方程Y（theta） - Y_Tar == 0的根   

定义方程左手边为函数：   


```python
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
```

它给出Y（theta） - Y_Tar   

二分法求根，注意到给定速度大小，解不唯一，问题有两个解   

假设给定速度 V = 500 m/s; 目标落点 （10000.， 4000.）   


```python

vel = 500.
xTarget = 10000.
yTarget = 4000.

theta1 = bisect(lambda a: solvediffByAngle(vel, a, xTarget, yTarget),40.,50.)
theta2 = bisect(lambda a: solvediffByAngle(vel, a, xTarget, yTarget),60.,70.)

```

theta1 = 41.05 degree   
theta1 = 66.46 degree   

画出两条轨迹   


```python
def solveTrajectoryByAngleQ2(speed, angle,xTarget, yTarget):
    def stop2Q(state,xTarget):
        return getX(state)[2] >= xTarget 
    theta = angle * math.pi / 180.
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    return dSolveUntil(airDrugedTrajVarB2(4.0e-5, 9.8), array([vx,vy,0.,0.]), 0.05,lambda s:stop2Q(s,xTarget))

ans1 = solveTrajectoryByAngleQ2(vel, theta1, xTarget, yTarget)
ans1x = reduceStateList(ans1, [2,3])
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"theta = "+str(theta1),"x/m","y/m", "Y - X")

ans1 = solveTrajectoryByAngleQ2(vel, theta2, xTarget, yTarget)
ans1x = reduceStateList(ans1, [2,3])
easyPlotXYHoldON(getXiList(ans1x,1),getXiList(ans1x,2),"theta = "+str(theta2),"x/m","y/m", "Y - X")
plt.ylim(0,9000)
plt.show()
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_2.1/pic/shoot.png)   
