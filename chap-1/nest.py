'''
nest a function
nest(function, initialValue, times) 
nestList(function, initialValue, times) 
nestListIter(function, initialValue, times)
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

def nestListiter(f,x0,n):
    yield x0
    for i in range(n):
        x0 = f(x0)
        yield x0




