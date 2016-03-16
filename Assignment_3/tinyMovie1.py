import os
import time
columnNum = 5
rowNum = 7
from charDict import getDictionary, blackQ
from printStar import printAtPosition
charDict = getDictionary()
for tms in range(5):
    for i in range(30):
        if i>=15:
            x,y = 30-i,30-i
        else:
            x,y = i,i
        os.system('cls')
        printAtPosition(charDict, 'A', x , 2*y ,'*',1 ,1)
        time.sleep(0.05)
