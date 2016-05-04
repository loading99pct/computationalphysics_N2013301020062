'''
nest a function
nest(function, initialValue, times) 

nestList(function, initialValue, times) 
nestListIter(function, initialValue, times)

nestUntil(f, x, stopQ, maxStep = 100000)
nestUntilList(f, x, stopQ, maxStep = 100000)
'''

def nest(f,x0,n):
    "return f(f(...f(x)))"
    i = 0
    while i < n:
        x0 = f(x0)
        i = i + 1
    return x0

def nestList(f,x,n):
    """
    return [x,f(x),f(f(x)),...,f(f(...f(x)))]
    [nest(f,x,0) to nest(f,x,n)]
    """
    result = [x]
    for i in range(n):
        x = f(x)
        result.append(x)
    return result


def nestUntil(f, x, stopQ, maxStep = 100000):
    """
    nest f begin with x, until stopQ(x) => True
    return [x,f(x),f(f(x)),...,f(f(...f(x)))]
    [nest(f,x,0) to nest(f,x,nx)]
    """
    n = 0
    while (not stopQ(x)):

        x = f(x)

        n = n + 1
        if n >= maxStep:
            print "Error : nestUntilList::Out of maxStep = ",maxStep ,", x =", x 
            break
    return x


def nestUntilList(f, x, stopQ, maxStep = 100000):
    """
    nest f begin with x, until stopQ(x) => True
    return [x,f(x),f(f(x)),...,f(f(...f(x)))]
    [nest(f,x,0) to nest(f,x,nx)]
    """
    n = 0
    x0 = x
    result = [x]
    while (not stopQ(x)):
        x = f(x)
        result.append(x)
        n = n + 1
        if n > maxStep:
            print "Error(Warning) : nestUntilList::Out of maxStep",maxStep ,",\tx =", x, "x0 = ",x0
            break
    return result
'''
def nestListiter(f,x0,n):
    yield x0
    for i in range(n):
        x0 = f(x0)
        yield x0

'''
'''
test

print nestUntilList(lambda x: x+1, 0, lambda x: x>=10)
print nestUntil(lambda x: x+1, 0, lambda x: x>=20)
print nestUntil(lambda x: x+1, 0, lambda x: x>=20,100)
print nestUntil(lambda x: x+1, 0, lambda x: x>=20,10)
print nestUntilList(lambda x: x**2, 3, lambda x: x>=100)
'''
