# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:07:12 2016

@author: user
"""

'''import matlab.engine as me

eng = me.start_matlab()
tf = eng.isprime(37)
print(tf)'''

#import numpy as np
#import pandas.DataFrame as df
#ezyTrain = np.loadtxt('EASY_TRAIN.csv', delimiter = ',', dtype = None)#, usecols = (range(26)))
#ezyTrainLabels = np.loadtxt('EASY_TRAIN.csv', usecols = (range(27,28)))
#print(ezyTrain.shape);

#print(ezyTrain[:,ezyTrain.shape[1]-1])
#df = df.from_csv('myfile.txt', sep='\t')

import csv
import numpy as np
with open('EASY_TRAIN.csv', 'r') as f:
  reader = csv.reader(f)
  ezyTrain = list(reader)

ezyTrain = np.matrix(ezyTrain)
#print(ezyTrain[:, -1:])
trainingLabelFromCsv = ezyTrain[:, -1:]
labelSet = set(ezyTrain[:, -1:].flat)
#print(labelSet)
#labelMap = {}
#for i in range(len(ezyTrain)):
labelMap={key+1:value for key, value in enumerate(labelSet)}
for i in labelMap:
    #print(labelMap.get(i))
    trainingLabelFromCsv = [i for j in trainingLabelFromCsv if j == labelMap.get(i)]
    print(trainingLabelFromCsv)
#print(labelMap)