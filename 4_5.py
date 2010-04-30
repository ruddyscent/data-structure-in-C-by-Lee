#!/usr/bin/env python

"""python porting of example 4-5 at p.152

"""


class Matrix(object):
    def __init__(self, row, col, elements):
        self.row = row
        self.col = col
        self.elements = elements

    def transpose(self):
        self.row, self.col = self.col, self.row
        
        elements = {}
        for i, j in self.elements:
            elements[j,i] = self.elements[i,j]
            
        self.elements = elements


if __name__ == '__main__':
    A = Matrix(3,3,{(0,1):1,(1,0):2})
    A.transpose()
    
    print A.elements
