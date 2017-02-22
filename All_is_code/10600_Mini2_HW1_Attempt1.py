# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:57:04 2016

@author: user
"""

import numpy as np
#import csv
    
#Categorical
#Find Residual -sort Above threshold remove outlier and repeat
#Outlier - 

#Feature Extraction -- Not needed
#Outlier Removal
#Feature Removal --     
def dummyCodingAttempt2(certainfeature):
    uniqueFeatureValues = np.unique(certainfeature)
    lsBnary = ['0' for i in range(len(uniqueFeatureValues))]
    origBnary = list(lsBnary)
    lsOfBnaryStrings = ['a' for x in range(len(certainfeature))]
    lsOflsBinaries = [[] for x in range(len(certainfeature))]
    for index, valueInUniqFeature in enumerate(uniqueFeatureValues):
        lsOfLocations = np.where(certainfeature == valueInUniqFeature)
        #lsOfLocations = lsOfLocations.tolist()
        print('BABABOE',lsOfLocations)
        print('BABABOR')
        for i in np.nditer(lsOfLocations):
            print(i)
            lsBnary[index] = '1'
            lsOflsBinaries[i] = list(lsBnary)
            
            #print(''.join(lsBnary))
            lsBnary = list(origBnary)
            
    lsOfBnaryStrings = [''.join(lsOflsBinaries[i]) for i in range(len(lsOflsBinaries))]
    print(lsOfBnaryStrings)
    return lsOfBnaryStrings


ls = np.genfromtxt('regression_hw.csv', delimiter = ',')
#print(ls)
#labels, inputs = zip(*[(x[0], x[1:]) for x in ls])
labels = [x[0] for x in ls]
inputs = [x[1:] for x in ls]


categoricalInputs = [0]*2
categoricalInputs[0] = [x[-2: -1] for x in ls]
categoricalInputs[1] = [x[-1:] for x in ls]
#print(list(categoricalInputs))
print('CHCHAHA')
#
npArr = np.array([])
modifInput = [dummyCodingAttempt2(feature) for feature in categoricalInputs]
print(modifInput)    
#print(dummyCodingAttempt2(np.array([1, 2, 3, 4, 4, 3, 6])))
np.savetxt("10_600_DumCode_Output.csv", modifInput, delimiter=",", fmt='%s')
