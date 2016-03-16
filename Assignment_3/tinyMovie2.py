import os
import time
columnNum = 5
rowNum = 7
from charDict import getDictionary, blackQ
from printStar import printAtPosition
charDict = getDictionary()
import math

deltaTheta = 0.2
r = 8
ox = 13
oy = 10
x, y = 0, 0
os.system('cls')
for tms in range(8):
    for num in range(0, int(math.pi/deltaTheta)+1):
        theta = 2 * num * deltaTheta 
        x, y = int(round(oy + r * math.sin(theta))),int(round(ox + r * math.cos(theta)))

        os.system('cls')
        printAtPosition(charDict, 'M', x , 2*y ,'m',2 ,1)
        time.sleep(0.05)

    
