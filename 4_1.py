#!/usr/bin/env python

"""python porting of example 4-4 at pp.145-147

"""

class Polynomial(object):
    def __init__(self, degree=0, coef={}):
        self.degree = int(degree)
        self.coef = coef

    def display(self):
        for i in reversed(xrange(self.degree+1)):
            if self.coef.has_key(i):
                print '%3.0fx^%d ' % (self.coef[i], i),
        print 

    
def addPoly(polyA, polyB):
    degree = max(polyA.degree,polyB.degree)
    coef = {}
    keys = set(polyA.coef.keys() + polyB.coef.keys())
    for k in keys:
        if polyA.coef.has_key(k):
            a = polyA.coef[k]
        else:
            a = 0
        if polyB.coef.has_key(k):
            b = polyB.coef[k]
        else:
            b = 0
        if a + b:
            coef[k] = a + b
    
    return Polynomial(degree, coef)


if __name__ == '__main__':
    A = Polynomial(3, {3:4,2:3,1:5})
    B = Polynomial(4, {4:3,3:1,1:2,0:1})
    
    C = addPoly(A,B)

    A.display()
    B.display()
    C.display()
    
