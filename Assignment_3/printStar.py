import os
import time
columnNum = 5
rowNum = 7
from charDict import getDictionary, blackQ
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








