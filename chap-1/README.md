
这是markdown 预览文件, 正式版为jupyter文件

本次作业，目前完成了通用的求解X'=F(t,X)形式微分方程（X可以为标量或矢量）的程序  
目前可以采用 Runge - Kutta 家族下的四种显式的求解法求解，包括  
Forward Euler Method  
Explicit Trapezoidal Method  
MidPoint Method  
RK4 Method  
注意到本课程多章均涉及微分方程求解，不妨设计通用的求解多元一阶微分方程组的函数，  
多元高阶微分方程组可以约化为一阶方程组的求解。  
为了自动约化高阶方程，需要进行元语言抽象，并编写求值器或解释器（有没有更简单的的方法？）  
所以，这里的一般求解方法为，将高阶方程手动化为相应个数的一阶，并通过dSolve函数求解。
# 一般微分方程的求解函数 #

## dSolve函数 ##
在这里，一个微分方程组被映射为程序中的一个函数，即微分方程的右手边一系列函数的集合（ X'[t] = F[t,X] 对应于程序中的 F），接受时间t和矢量X,给出X'

通过高阶函数，可以将"通过迭代法数值求解微分方程求解" 与 "具体的求解方法" 二者解耦。

某一 Runge-Kutta 家族下的求解法，被映射到程序中的一个高阶函数，
它接受待解得微分方程的RHS-Function作为参数，输入某一时刻状态（t(i),X(i)）,输出下一时刻状态（t(i+1),X(i+1)）

dSolve函数（目前）通过采用某一显式求解法（目前给出了四种常见方法供选择，如下节所列），对初始条件使用指定方法反复迭代（通过nest.py 中的 nestList函数）生成离散的状态列表。

dSolve可以求解一元微分方程或多元微分方程组（遵循下面要求的格式），但是目前如需求解高阶方程须手动化为多元一阶形式。

dSolve solves a system of first-order differential equations
(or A first-order differential equation, of course) of the form:

-----------------------------------------------

                X'[t] = F[t,X]
                
-----------------------------------------------
(
                
    where  X = (x1,x2,...,xn)T
    F:  X -> Y
        (x1,x2,...,xn)T -> (y1,y2,...,yn)T
        where:
        y1 = f1(t,x1,x2,...,xn),
        y1 = f1(t,x1,x2,...,xn),
        .
        .
        yn = f1(t,x1,x2,...,xn) 
)

with initial value X[0] =x0,
(
    !!! if xi is a vector, 
    it should be given by the data structure "array" defined in numpy package
    e.g. numpy.array([x1,x2,x3])
)

from t = 0 to t = tMax,

with fixed step size = stepSize,

using method selected from __methodDictionary


Output: [state0, state1,... ]
    where statei has the form [ti, xi] for a ODE, 
        or [ti, array([x1i,x2i...])] for s system of ODEs
            
This function is impliment as follows:


```python

def dSolve(func, x0, tMax, stepSize, method = "RK4"):
    times = int(math.ceil(float(tMax) / stepSize))
    methodFunc = __methodDictionary[method]
    toNext = lambda state: methodFunc(state, func, stepSize)
    return nestList(toNext, makeState(0, x0), times)

```

## Four methed in Runge-Kutta's family ##
Map different methed in Runge-Kutta's familly to a Higher-order function, 
which takes a high-order function F (in X'[t] = F[t,X]) and state[i] as input, give state[i+1]

```python
"""
the constructor and selector of a State:(t,X) 
"""
def makeState(t, x): return [t,x]
def getX(state): return state[1]
def getT(state): return state[0]

```
In the following method:
xi could be a scalar, or a vector
    if xi is a vector, 
    it should be given by the data structure "array" defined in numpy package
    e.g. numpy.array([x1,x2,x3])
the f is the RHS-function in X'[t] == f(X,t)
    f: ti,xi -> xii
    f should be defined in the form 
        define f(ti, Xi):  
            return a vector with the same size as Xi
        or given by a equivalent lambda expression
with fixed step size h, and a given f,
the followingMethod is a iterative function 
    followingMethod: state ->state
                     (ti,xi) -> (tii,xii)
### 前向欧拉法 ###


```python
def forwardEulerMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    tii = ti + h  # tii = Subscibe[t,i+1]
    xii = xi + h * f(ti,xi)  # xii = Subscibe[x,i+1]
    return makeState(tii,xii)
```

### 显式梯形法 ###


```python
def explicitTrapezoidalMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    tii = ti + h  
    xii = xi + h/2.0 *(f(ti,xi) + f(ti+h, xi+h*f(ti,xi)))
    return makeState(tii,xii)
```

### 中点法 ###


```python
def midPointMethod(state, f, h):
    ti = getT(state)
    xi = getX(state)
    h = float(h)
    tii = ti + h
    xii = xi + h * f(ti+h/2, xi+h/2*f(ti,xi))
    return makeState(tii,xii)
```

### RK4方法 ###


```python
def rk4Method(state, f, h):
    '''
    Classic fourth-order Runge-Kutta method
    '''
    ti = getT(state)
    xi = getX(state)
    h = float(h)
    tii = ti + h 
    s1 = f(ti,xi)
    s2 = f(ti+h/2, xi+h/2*s1)
    s3 = f(ti+h/2, xi+h/2*s2)
    s4 = f(ti+h, xi+h*s3)
    xii = xi + h/6 * (s1 + 2*s2 + 2*s3 +s4)
    return makeState(tii,xii)
```

### 方法字典 ###
dSolve中的求解方法在以下字典之一中选择

```python
__methodDictionary={\
    "ForwardEuler":forwardEulerMethod,\
    "ExplicitTrapezoidal":explicitTrapezoidalMethod,\
    "Midpoint":midPointMethod,\
    "RK4":rk4Method\
}
```

## 辅助函数：快速画图 ##
dSolveAndFastPlot
dSolveAndFastPlot(func, x0, tMax, stepSize, method = "RK4")：
用于快速查看结果，略
dSolveAndDetailedPlotAndHoldOn
def dSolveAndDetailedPlotAndHoldOn(func, x0, tMax, stepSize, method,\
 labelList, xLabel = "", yLabel = "", titleLabel = ""): 
用于详细画图，略
## 本章习题 ##
第一题自由下落，仅作演示辅助函数dSolveAndFastPlot （简记为 dfp），速度随时间变化如下（仅作演示，坐标从略）：

```python

def freeFallingFunc1():
    return lambda t,x: -9.8
dSolveAndFastPlot(freeFallingFunc1(), 0, 10.,0.05,"ForwardEuler")

```

![ff](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/freeFallingFunc1.png)

第三题阻尼下落，演示dSolve函数生成结果。
辅助函数dSolveAndDetailedPlotAndHoldOn，以下简记为 dfp


```python

def airDragedFallingFunc3(a,b):
    return lambda t,v: a - b * v
print dSolve(airDragedFallingFunc3(9.8, 1. ), 0, 10.,0.5)
dfp(airDragedFallingFunc3(9.8, 1. ), 0, 10.,0.05,"ForwardEuler")

```

    [[0, 0], [0.5, 3.853645833333333], [1.0, 6.191925726996528], [1.5, 7.6107257666411225], [2.0, 8.47161224902964], [2.5, 8.993973057353923], [3.0, 9.31092636032152], [3.5, 9.503244380090923], [4.0, 9.619937345211419], [4.5, 9.69074323290172], [5.0, 9.733706180380471], [5.5, 9.759774843824609], [6.0, 9.775592548466495], [6.5, 9.785190270293473], [7.0, 9.79101388796453], [7.5, 9.794547489311812], [8.0, 9.79669157554597], [8.5, 9.797992544537008], [9.0, 9.79878193457584], [9.5, 9.799260913427528], [10.0, 9.799551543824515]]
    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/airDragedFallingFunc3.png)  
当采用不同的步长时：

```python

def airDragedFallingFunc3(a,b):
    return lambda t,v: a - b * v
    
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.5,"ForwardEuler",\
    ["step size = 0.5"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.1,"ForwardEuler",\
    ["step size = 0.05"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,0.005,"ForwardEuler",\
    ["step size = 0.005"],"t/s", "v/m.s-1","air Draged Falling")
plt.show()
    
```

![ds](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/airDragedFallingFunc3%20-%20cmp1.png)

随着步长减小，解从单侧逐渐靠近真实值。  
  
相同步长，当采用不同方法时：


```python
stpsz = 0.8

ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"ForwardEuler",\
    ["ForwardEuler"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"ExplicitTrapezoidal",\
    ["ExplicitTrapezoidal"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"Midpoint",\
    ["Midpoint"])
ddp(airDragedFallingFunc3(9.8, 1. ), 0, 8.,stpsz,"RK4",\
    ["RK4"])

xx = np.linspace(0., 8., 256, endpoint=True)
vv =9.8 -9.8*np.exp(-xx)
plt.plot(xx,vv,label = "real solution")
plt.legend(loc='upper right', frameon=False)
plt.show()
```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/airDragedFallingFunc3%20-%20cmp2.png)
可以看出，即使在步长极大时，梯形法和RK4方法仍符合的很好第四题演示dSolve求解多元ODE，图片仅为示意，坐标从略

```python

def decayFunc4(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA, 0],[1./tauA,-1./tauB]]),nab)
print dSolve(decayFunc4(1.,1.), array([1.5,0.]), 10.,0.5,"RK4")
dfp(decayFunc4(1.,1.), array([1.5,0.]), 10.,0.05,"RK4")

```

    [[0, array([ 1.5,  0. ])], [0.5, array([ 0.91015625,  0.453125  ])], [1.0, array([ 0.55225627,  0.54988607])], [1.5, array([ 0.33509299,  0.50048224])], [2.0, array([ 0.20332466,  0.40490404])], [2.5, array([ 0.12337147,  0.30710495])], [3.0, array([ 0.07485821,  0.22361079])], [3.5, array([ 0.04542178,  0.15829392])], [4.0, array([ 0.02756061,  0.1097693 ])], [4.5, array([ 0.01672297,  0.07493041])], [5.0, array([ 0.01014701,  0.05051732])], [5.5, array([ 0.00615691,  0.03371768])], [6.0, array([ 0.00373583,  0.0223188 ])], [6.5, array([ 0.0022668 ,  0.01467093])], [7.0, array([ 0.00137543,  0.00958666])], [7.5, array([ 0.00083457,  0.0062324 ])], [8.0, array([ 0.00050639,  0.00403375])], [8.5, array([ 0.00030726,  0.00260053])], [9.0, array([ 0.00018644,  0.00167075])], [9.5, array([ 0.00011313,  0.00107008])], [10.0, array([  6.86412513e-05,   6.83466537e-04])]]
    

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/decayFunc4-1.png)  
第五题，达到平衡态的演示：

```python
def decayFunc5(tauA, tauB):
    return lambda t,nab: np.dot(array([[-1./tauA,1./tauB],[1./tauA,-1./tauB]]),nab)
ddp(decayFunc5(1.,1.5), array([2.0,0.5]), 5.,0.05,"RK4",["N_A","N_B"],"t/s","N/1")
plt.show()

```

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/chap-1/decayFunc5.png)
