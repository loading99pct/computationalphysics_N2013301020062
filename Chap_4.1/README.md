
# 引力随距离指数项不为-2时轨道的进动 #

本文中，我们计算对不同的指数项大小，以及不同的偏心率，轨道进动的情况。   

假设力随距离r有：F(r) = k r^n   

## 不同的指数项大小的轨道进动 ##

这里，我们取万有引力常数与中心天体质量的乘积k M = 1.0,中心天体视为固定的。 vx = 0.0, vy = 0.6, x = 1.0, y = 0.0, 模拟时间长度30, 以上系数均已无量纲化。   
分别讨论n = -1, -2.05, -1, 1, 2 的情况

n = -2.00， 轨道是闭合的   
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difn1.png)   
n = -2.05， 轨道不是闭合的，有比较小的进动    
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difn2.png)   
n = -1.00， 轨道不是闭合的，有比较大的进动   
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difn3.png)   
n = 1.00， 轨道同样是闭合的   
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difn4.png)   
n = 2.00， 轨道不是闭合的，有比较大的进动   
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difn5.png)   

下面的 GIF 动画描述了进动随不同的指数项大小变化的情况。可以看出，进动随n的增大先减小，然后反向增大   

[https://github.com/loading99pct/computationalphysics_N2013301020062/blob/master/Chap_4.1/pic/nvar2.gif]()   
（动画较大，加载需要时间）      

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/nvar2.gif)

## 对不同离心率的轨道进动 ##

我们通过调节vy来改变偏心率：   

v = 1.0   
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difv4.png)   
v = 0.8
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difv3.png)   
v = 0.5  
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difv2.png)   
v = 0.1  
![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/difv1.png)   

下面的动画描述了进动随初始速度变化的情况。可以看出，随着轨道离心率的减小，进动也越来越不明显   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_4.1/pic/vvar.gif)
