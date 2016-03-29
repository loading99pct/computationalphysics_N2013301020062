''' 
    cl:[f1,f2,...,fm]T -> F: R^n -> R^m
                            X -> Y = F(X)
                            [x1,x2,...,xn]T -> [y1,y2,...ym]T
    where Y = F(X), i.e.
          y1 = f1(x1,x2,...,xn)
          y1 = f1(x1,x2,...,xn)
          .
          .
          ym = fn(x1,x2,...,xn)
'''

'''
def cl(fs):
    def cdf(xs):
        return map(lambda f,x : apply(f, [x]), fs, xs)
    return cdf
'''
'''
def cl(fs):
    return lambda xs: map(lambda f,x : apply(f, [x]), fs, xs)
'''