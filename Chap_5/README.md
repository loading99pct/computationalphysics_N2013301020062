
# 平板电容间的拉普拉斯方程数值求解 #

我们通过将系统离散化，通过迭代使系统逐渐收敛到真实解   

首先，我们求解具有如下构型的系统：      
length 代表计算方格大小，首先我们改变模拟尺度。   
platePos平板放置距离中心位置，这里首先取2   
plateLen平板的半长， 这里首先取2   

初始图像如下：   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/i1.png)   

对于不同的模拟尺度大小，分别迭代，如下动画所示：   

length = 60   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/iter.gif)   

length = 80   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/iter2.gif)   

length = 120   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/iter3.gif)   

对于length = 120，我们画出迭代到接近不动点时的状态   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/p1.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/s11.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/s1.png)   

对于另一组参数   
length：计算方格大小：120   
platePos:平板放置距离中心位置:10   
plateLen:板的半长:这里首先取:10   
我们得到   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/i2.png)   

反复迭代到接近不动点时的状态   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/iter4.gif)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/p2.png)   

![](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Chap_5/pic/s2.png)   
