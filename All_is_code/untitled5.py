# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:26:00 2016

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

npMatrx = np.genfromtxt('sample.csv',delimiter= ',')
normalList = [x for x in npMatrx.T]
normalList.sort()
n = len(normalList)
plotty = [[0 for x in range(len(normalList)+1)] for y in range(2)]
prob = [0 for x in range(len(normalList)+1)]
for i, el in enumerate(normalList):
    prob[i+1] = (i)/(n-1)
    print(prob[i+1])
    print('i  :')
    print(i+1)
    #plotty[prob[i+1], i+1]
    
print(prob[0])
print(i+2)
plt.plot(prob, normalList)
plt.show()
    
print('dhasjkdhs', 1,'adsasd')