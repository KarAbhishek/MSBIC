# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:24:31 2016

@author: user
"""
import numpy as np
import sklearn
class BaseLearner():
    def __init__(self):
        self.trainingXData = None
        self.trainingYLabels = None
        self.testXData = None
        self.model = None
                    
    def useModel(self, modl):
        self.model = modl

    def loadTestData(self, testX):
        self.testXData = testX
        
    def loadTrainingData(self, trainX, trainY):
        self.trainingXData = trainX
        self.trainingYLabels = trainY
        
    def fitting(self):
        return self.model.fit(self.trainingXData, self.trainingYLabels)
        
    def prediction(self):
        return self.model.predict(self.testXData)
    


csvTrainData = np.genfromtxt('EASY_TRAIN.CSV', delimiter = ',', dtype = 'str')
print(csvTrainData[0])
trainX = np.array(csvTrainData[:, :csvTrainData.shape[1]-1], 'float64')
print(trainX[0])
testX = np.genfromtxt('EASY_TEST.CSV', delimiter = ',', dtype = 'str')
true_Labels = csvTrainData[:, -1:]
#print(true_Labels[0])
baseLearner = BaseLearner()
baseLearner.useModel(sklearn.ensemble.RandomForestClassifier())
baseLearner.fitting()
print(baseLearner.prediction())