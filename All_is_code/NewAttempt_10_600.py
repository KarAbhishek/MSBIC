# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:54:35 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:57:04 2016

@author: user
"""

import numpy as np

def dummyCodingAttempt2(certainfeature):
    uniqueFeatureValues = np.unique(certainfeature)
    lsBnary = [0 for i in range(len(uniqueFeatureValues))]
    origBnary = list(lsBnary)
    #lsOfBnaryStrings = ['a' for x in range(len(certainfeature))]
    lsOflsBinaries = [[] for x in range(len(certainfeature))]
    for index in range(uniqueFeatureValues.shape[0]):
        lsOfLocations = np.where(certainfeature == uniqueFeatureValues[index])
        for i in np.nditer(lsOfLocations):
            #print(i)
            lsBnary[index] = 1
            lsOflsBinaries[i] = list(lsBnary)
            
            #print(''.join(lsBnary))
            lsBnary = list(origBnary)
            
    #lsOfBnaryStrings = [''.join(lsOflsBinaries[i]) for i in range(len(lsOflsBinaries))]
    print(np.array(lsOflsBinaries))
    return lsOflsBinaries#lsOfBnaryStrings
    
'''def standardize():
    
    mean(Y)
    mean(X)
    std(Y)
    std(x)
    Y-mean(Y)/std(Y)
    X-mean(X)/std(X)
    '''

def standardize(X):
    modX = X
    for colIdx in range(len(X[0])):
        modX[colIdx] = (modX[colIdx]-np.mean(modX[colIdx], axis = 0))/(np.std(modX[colIdx], axis = 0))
    #Y[0] = Y[0]-np.mean(Y[0], axis = 0)/np.std(Y[0], axis = 0)
    return modX#np.concatenate((X,Y), axis = 1)
    
    
    
    
ls = np.genfromtxt('regression_hw.csv', delimiter = ',')
labels = ls[:, 0]
inputs = ls[:, 1:]
categoricalInputs = inputs[:, [-2, -1]]

modifInput = inputs[:, :-2]# + 
modifInput = (np.concatenate((modifInput, dummyCodingAttempt2(categoricalInputs[:, 0]), dummyCodingAttempt2(categoricalInputs[:, 1])), axis = 1 ))
np.savetxt("10_600_DumCode_Output.csv", modifInput, delimiter=",", fmt='%s')
#stdizedMatrix = standardize(np.concatenate((modifInput, labels), axis = 1))
#print(stdizedMatrix)
