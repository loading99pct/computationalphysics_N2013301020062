
# Assignment_3

## 数据的处理

处理如下文件，得到从字母到点阵信息的字典
0x00,0x00,0x2f,0x00,0x00,!
0x00,0x60,0x60,0x00,0x00,.
0x00,0x00,0x00,0x00,0x00, 
0x7E,0x11,0x11,0x11,0x7E,A
0x7F,0x49,0x49,0x49,0x36,B
0x3E,0x41,0x41,0x41,0x22,C
0x7F,0x41,0x41,0x22,0x1C,D
.
.
.
0x1C,0x20,0x40,0x20,0x1C,v
0x3C,0x40,0x30,0x40,0x3C,w
0x44,0x28,0x10,0x28,0x44,x
0x0C,0x50,0x50,0x50,0x3C,y
0x44,0x64,0x54,0x4C,0x44,z
希望通过‘charDict.py’文件，读入上述txt文件，并生成字典
{'!': ['0000000', '0000000', '0101111', '0000000', '0000000'],
'.': ['0000000', '1100000', '1100000', '0000000', '0000000'],
'A': ['1111110', '0010001', '0010001', '0010001', '1111110'],
.
.
.
'v': ['0011100', '0100000', '1000000', '0100000', '0011100'],
'y': ['0001100', '1010000', '1010000', '1010000', '0111100'], 
'x': ['1000100', '0101000', '0010000', '0101000', '1000100'], 
'z': ['1000100', '1100100', '1010100', '1001100', '1000100']}
代码如下：


```python
import string

columnNum = 5
rowNum = 7

def getDictionary():
    '''
    usage myDict=getDictionary()
    '''

    def normALine(a):
        '''
        st = ['0x00', '0x00', '0x2f', '0x00', '0x00', '!\n']
        to  ['0x00', '0x00', '0x2f', '0x00', '0x00', '!']
        ( left to right [bottom to top, bottom to top, ...] )
        '''
        a[-1]=a[-1][0]
        return a

    def strHexToStrBin7(st):
        '''
        strHexToStrBin7('0x3f')->'011111'
        '''
        def strHexToStrBin(st):
            num=int(st,16)
            return bin(num)[2:]
        def completeToN(st,num):
            if len(st) < num:
                 st = '0'*(num - len(st)) + st
            return st
        def completeTo7(st):
            # '1011' to '0001011'
            return completeToN(st,7)
        return completeTo7(strHexToStrBin(st))

    odata=open('data.txt','r')
    lineN=54
    ldata=[]
    for line in odata:
        ldata.append(line.split(','))
    charDict={}
    for eachdata in ldata:
        eachdata=normALine(eachdata)
        charDict[eachdata[-1]] = map(strHexToStrBin7,eachdata[0:-1])
    odata.close()
    return charDict


def blackQ(dictionary,letter,i,j):
    # return True or False
    return dictionary[letter][j][rowNum-i] == '1'
'''
def getPositionIJ(dictionary,letter,i,j):
    # return '1' or '0'
    # this function dose not abstract the data structure of the dictionary
    return dictionary[letter][j][rowNum-i]
'''
```




    "\ndef getPositionIJ(dictionary,letter,i,j):\n    # return '1' or '0'\n    # this function dose not abstract the data structure of the dictionary\n    return dictionary[letter][j][rowNum-i]\n"



通过charDict = getDictionary()得到字典


```python
charDict
```




    {' ': ['0000000', '0000000', '0000000', '0000000', '0000000'],
     '!': ['0000000', '0000000', '0101111', '0000000', '0000000'],
     '.': ['0000000', '1100000', '1100000', '0000000', '0000000'],
     'A': ['1111110', '0010001', '0010001', '0010001', '1111110'],
     'B': ['1111111', '1001001', '1001001', '1001001', '0110110'],
     'C': ['0111110', '1000001', '1000001', '1000001', '0100010'],
     'D': ['1111111', '1000001', '1000001', '0100010', '0011100'],
     'E': ['1111111', '1001001', '1001001', '1001001', '1000001'],
     'F': ['1111111', '0001001', '0001001', '0001001', '0000001'],
     'G': ['0111110', '1000001', '1001001', '1001001', '1111010'],
     'H': ['1111111', '0001000', '0001000', '0001000', '1111111'],
     'I': ['0000000', '1000001', '1111111', '1000001', '0000000'],
     'J': ['0100000', '1000000', '1000001', '0111111', '0000001'],
     'K': ['1111111', '0001000', '0010100', '0100010', '1000001'],
     'L': ['1111111', '1000000', '1000000', '1000000', '1000000'],
     'M': ['1111111', '0000010', '0001100', '0000010', '1111111'],
     'N': ['1111111', '0000100', '0001000', '0010000', '1111111'],
     'O': ['0111110', '1000001', '1000001', '1000001', '0111110'],
     'P': ['1111111', '0001001', '0001001', '0001001', '0000110'],
     'Q': ['0111110', '1000001', '1010001', '0100001', '1011110'],
     'R': ['1111111', '0001001', '0011001', '0101001', '1000110'],
     'S': ['1000110', '1001001', '1001001', '1001001', '0110001'],
     'T': ['0000001', '0000001', '1111111', '0000001', '0000001'],
     'U': ['0111111', '1000000', '1000000', '1000000', '0111111'],
     'V': ['0011111', '0100000', '1000000', '0100000', '0011111'],
     'W': ['0111111', '1000000', '0111000', '1000000', '0111111'],
     'X': ['1100011', '0010100', '0001000', '0010100', '1100011'],
     'Y': ['0000111', '0001000', '1110000', '0001000', '0000111'],
     'Z': ['1100001', '1010001', '1001001', '1000101', '1000011'],
     'a': ['0100000', '1010100', '1010100', '1010100', '1111000'],
     'b': ['1111111', '1001000', '1000100', '1000100', '0111000'],
     'c': ['0111000', '1000100', '1000100', '1000100', '0100000'],
     'd': ['0111000', '1000100', '1000100', '1001000', '1111111'],
     'e': ['0111000', '1010100', '1010100', '1010100', '0011000'],
     'f': ['0001000', '1111110', '0001001', '0000001', '0000010'],
     'g': ['0001100', '1010010', '1010010', '1010010', '0111110'],
     'h': ['1111111', '0001000', '0000100', '0000100', '1111000'],
     'i': ['0000000', '1000100', '1111101', '1000000', '0000000'],
     'j': ['0100000', '1000000', '1000100', '0111101', '0000000'],
     'k': ['1111111', '0010000', '0101000', '1000100', '0000000'],
     'l': ['0000000', '1000001', '1111111', '1000000', '0000000'],
     'm': ['1111100', '0000100', '0011000', '0000100', '1111000'],
     'n': ['1111100', '0001000', '0000100', '0000100', '1111000'],
     'o': ['0111000', '1000100', '1000100', '1000100', '0111000'],
     'p': ['1111100', '0010100', '0010100', '0010100', '0001000'],
     'q': ['0001000', '0010100', '0010100', '0011000', '1111100'],
     'r': ['1111100', '0001000', '0000100', '0000100', '0001000'],
     's': ['1001000', '1010100', '1010100', '1010100', '0100000'],
     't': ['0000100', '0111111', '1000100', '1000000', '0100000'],
     'u': ['0111100', '1000000', '1000000', '0100000', '1111100'],
     'v': ['0011100', '0100000', '1000000', '0100000', '0011100'],
     'w': ['0111100', '1000000', '0110000', '1000000', '0111100'],
     'x': ['1000100', '0101000', '0010000', '0101000', '1000100'],
     'y': ['0001100', '1010000', '1010000', '1010000', '0111100'],
     'z': ['1000100', '1100100', '1010100', '1001100', '1000100']}



函数def blackQ(dictionary,letter,i,j)通过数据抽象将数据的表式（在‘charDict.py’中）与‘printStar.py’中数据的使用隔离开。注意到python中同样存在位级运算，可以在之后将数据的表示仍采用原始数据的十六进制，只需修改界面函数，而不影响打印程序。


```python
def blackQ(dictionary,letter,i,j):
    # return True or False
    return dictionary[letter][j][rowNum-i] == '1'
```

## 数据打印

如下界面函数用于打印字母：


```python
def printAShortString(dictionary, string, star = '*',  magnificationFactorX = 1, magnificationFactorY = 1):
    '''
    defination
    具体变量作用如下：
        string 为待打印的字符或字符串
        star变量表示用何种符号填充字符，默认为星号 *
        magnificationFactorX, magnificationFactorY 分别用来指定沿横向和纵向的放大倍数，默认为2， 1
    '''
def ezPrint(string, star = '*',  magnificationFactorX = 2, magnificationFactorY = 1):
   '''
   easy print 
   '''


```

由于在全局变量中定义了charDict为字典，采用ezPrint方便打印

### string 为待打印的字符或字符串 ###


```python
ezPrint('a')
```

                 
                 
         ******  
               **
         ********
       **      **
         ********
    


```python
ezPrint('Print')
```

       ********                      **                      **      
       **      **                                            **      
       **      **   **  ****       ****       **  ****     ******    
       ********     ****    **       **       ****    **     **      
       **           **               **       **      **     **      
       **           **               **       **      **     **    **
       **           **             ******     **      **       ****  
    

### star变量表示用何种符号填充字符，默认为星号 * ###


```python
ezPrint('W','W')
```

       WW      WW
       WW      WW
       WW      WW
       WW  WW  WW
       WW  WW  WW
       WW  WW  WW
         WW  WW  
    


```python
ezPrint('orz','O')
```

                                           
                                           
         OOOOOO     OO  OOOO     OOOOOOOOOO
       OO      OO   OOOO    OO         OO  
       OO      OO   OO               OO    
       OO      OO   OO             OO      
         OOOOOO     OO           OOOOOOOOOO
    

### magnificationFactorX, magnificationFactorY 分别用来指定沿横向和纵向的放大倍数，默认为2， 1 ###


```python
ezPrint('TAT','$',1,1)
```

       $$$$$    $$$    $$$$$
         $     $   $     $  
         $     $   $     $  
         $     $   $     $  
         $     $$$$$     $  
         $     $   $     $  
         $     $   $     $  
    


```python
ezPrint('TAT','~',2,1)
```

       ~~~~~~~~~~     ~~~~~~     ~~~~~~~~~~
           ~~       ~~      ~~       ~~    
           ~~       ~~      ~~       ~~    
           ~~       ~~      ~~       ~~    
           ~~       ~~~~~~~~~~       ~~    
           ~~       ~~      ~~       ~~    
           ~~       ~~      ~~       ~~    
    


```python
ezPrint('TAT','|',4,2)
```

       ||||||||||||||||||||       ||||||||||||       ||||||||||||||||||||
       ||||||||||||||||||||       ||||||||||||       ||||||||||||||||||||
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||||||||||||||||||           ||||        
               ||||           ||||||||||||||||||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
               ||||           ||||            ||||           ||||        
    


```python
ezPrint('TAT','$',6,3)
```

       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$               $$$$$$            
                   $$$$$$               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$               $$$$$$            
                   $$$$$$               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
                   $$$$$$               $$$$$$                  $$$$$$               $$$$$$            
    

具体代码如下（与代码源文件‘printStar.py’略有差别）：


```python
import os
import time
columnNum = 5
rowNum = 7
charDict = getDictionary()

def printAShortString(dictionary, string, star = '*',  magnificationFactorX = 1, magnificationFactorY = 1):
    # fill the pattern by,e.g., '*'
    def getNthLineOfALetter(letter,nthRow):
        line = ''
        for j in range(columnNum):
            if blackQ(dictionary, letter, nthRow, j):
                line = line + magnificationFactorX * star
            else:
                line = line + magnificationFactorX * ' '
        return line
    def getNthLineOfAString(string, nthRow, gapNum):
        # get ith line 
        line = ''
        for letter in string:
            line = line + gapNum*' ' + getNthLineOfALetter(letter, nthRow)
        return line
    
    for nthRow in range(1, rowNum + 1):
        for i in range(magnificationFactorY):
            print getNthLineOfAString(string, nthRow, 3)
            
def ezPrint(string, star = '*',  magnificationFactorX = 2, magnificationFactorY = 1):
    return printAShortString(charDict, string, star,  magnificationFactorX, magnificationFactorY)
```

## 动画显示

动画显示借助如下函数：


```python
def printAtPosition(dictionary, string, x = 0, y = 0, star = '*',  magnificationFactorX = 1, magnificationFactorY = 1):
    '''
    在屏幕制定位置（x，y）显示字符,
    参数意义与上函数相同
    '''

```

借此，可以在屏幕一位置打印，等待后，清屏，再次打印，如此循环

两个小动画如‘tinyMovie1.py’和‘tinyMovie1.py’，演示如下：

‘tinyMovie1.py’将某一字符串沿对角线反复移动（gif图片未压缩（1MB），流畅运行可能需要等待时间）

![tiny_movie_1](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Assignment_3/bandicam%202016-03-16%2001-18-21-191~2.gif)

‘tinyMovie2.py’将某一字符串圆周运动（gif图片未压缩(0.5MB)，流畅运行可能需要等待时间）

![tiny movie 1](https://raw.githubusercontent.com/loading99pct/computationalphysics_N2013301020062/master/Assignment_3/bandicam%202016-03-16%2001-16-51-488%2000_00_00-00_00_10~2.gif)

两段演示代码核心部分如下：

1.在制定位置显示特定字符


```python
def printAtPosition(dictionary, string, x = 0, y = 0, star = '*',  magnificationFactorX = 1, magnificationFactorY = 1):
    # fill the pattern by,e.g., '*'
    '''if''' 
    def getNthLineOfALetter(letter,nthRow):
        line = ''
        for j in range(columnNum):
            if blackQ(dictionary, letter, nthRow, j):
                line = line + magnificationFactorX * star
            else:
                line = line + magnificationFactorX * ' '
        return line
    def getNthLineOfAString(string, nthRow, gapNum):
        # get ith line 
        line = ''
        for letter in string:
            line = line + gapNum*' ' + getNthLineOfALetter(letter, nthRow)
        return line
        for i in range(x):
            print ''
    for nthRow in range(1, rowNum + 1):
        for i in range(magnificationFactorY):
            print ' ' * y+getNthLineOfAString(string, nthRow, 3)
```

2.第一段演示动画核心部分


```python
for tms in range(10):#ten times
    for i in range(30):
        if i>=15:
            x,y = 30-i,30-i
        else:
            x,y = i,i
        os.system('cls')
        printAtPosition(charDict, 'A', x , 2*y ,'*',1 ,1)
        time.sleep(0.05)


```

3.第二段演示动画核心部分


```python
for tms in range(8):#eight times
    for num in range(0, int(math.pi/deltaTheta)+1):
        theta = 2 * num * deltaTheta 
        x, y = int(round(oy + r * math.sin(theta))),int(round(ox + r * math.cos(theta)))

        os.system('cls')
        printAtPosition(charDict, 'M', x , 2*y ,'m',2 ,1)
        time.sleep(0.05)

```
