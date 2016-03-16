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


