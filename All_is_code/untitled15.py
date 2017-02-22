# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:24:41 2016

@author: user
"""

'''import numpy as np
x=np.random.normal(size=25)
y=np.random.normal(size=25)
print(x.shape, y.shape)
z = np.vstack((x, y))
c = np.cov(z.T)
print(c.shape)
print(np.ma.cov(x.T,y.T))'''
import numpy as np

def E(X, P):
    expectedValue = 0
    for i in np.arange(0, np.size(X)):
        expectedValue += X[i] * (P[i] / np.size(X))
    return expectedValue 

def covariance(X, Y):
    XY = X * Y
    EX = E(X, np.ones(np.size(X)))
    EY = E(Y, np.ones(np.size(Y)))
    EXY = E(XY, np.ones(np.size(XY)))
    return EXY - (EX * EY)
    
l=[[]]

for i in 