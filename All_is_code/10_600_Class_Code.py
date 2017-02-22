# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:33:15 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:00:11 2016
"""
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression

meanTrain = np.array([0,0])
stdTrain = np.array([0,0])
class Standardization:
    def standardize(self, X, standardizeOnlyX):
        modX = X
        #print(X)
        global meanTrain
        global stdTrain
        #print(np.array_equal(meanTrain, np.array([0,0])) and np.array_equal(stdTrain, np.array([0,0])))
        
        if(np.array_equal(meanTrain, np.array([0,0])) and np.array_equal(stdTrain, np.array([0,0]))):
            meanTrain = np.mean(modX, axis = 0)
            stdTrain = np.std(modX, axis = 0)
        #print(meanTrain,stdTrain)
        if standardizeOnlyX:
            for colIdx in range(len(X[0])-1):
                modX[:, colIdx] = (X[:, colIdx]-meanTrain[colIdx+1])/stdTrain[colIdx+1]
            return modX
        for colIdx in range(len(X[0])):
            modX[:, colIdx] = (X[:, colIdx]-meanTrain[colIdx])/stdTrain[colIdx]
        #Y[0] = Y[0]-np.mean(Y[0], axis = 0)/np.std(Y[0], axis = 0)
        
        print('Mean Train: ', meanTrain)
        print('Std Train: ', stdTrain)
        return modX
    
    def reverseStandardization(self, Y):
        global meanTrain
        global stdTrain
        #ret = np.zeros(len(Y))
        #print(len(Y))
        ret = (Y*stdTrain[0]+meanTrain[0])
        #for colIdx in range(len(Y)):
            #ret[colIdx] = (Y[colIdx]*stdTrain[colIdx]+meanTrain[colIdx])
        return ret
    
class EverythingElse:
    def dummyCodingAttempt2(self, certainfeature):
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
        #print(np.array(lsOflsBinaries))
        return lsOflsBinaries#lsOfBnaryStrings
    
    def L_loss(self, Y, W, X, isStandardized):
        #print(W.shape)
        #print(X.shape)
        prediction = generatePrediction(X,W, isStandardized)
        prediction = reverseStandardization(prediction)
        residual = np.abs(Y - prediction)
        #print(residual)
        #plt.scatter(range(1, len(residual)+1), residual)
        #outlierRemoval(residual)
        return np.mean(residual**2)
        
    def generatePrediction(self, X,W, isStandardized):
        if(isStandardized):
            X = standardize(X, True)
        return np.dot(X, W)
        
    def linReg(self, X, Y):
        return np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
    
        
    def linRegAndLossCalc(self, Xtotal, isStandardized, testAndTrainDividingRange):
        #print(Xtotal[0:400, :])
        if(isStandardized):
            train = standardize(Xtotal[0:testAndTrainDividingRange, :], False)
        else:
            train = Xtotal
        test = Xtotal[testAndTrainDividingRange:500, :]
        
        ytrain = train[:, 0]
        Xtotal = train[:, 1:]
        
        Xtest = test[:, 1:]
        ytest = test[:, 0]
        
        W = linReg(Xtotal, ytrain)
        #print(W)
        return L_loss(ytest, W, Xtest, isStandardized)
    
    def morphFeaturesAfterDummyCoding(self, Xtotal):
        inputs = Xtotal[:, 1:]
        categoricalInputs = inputs[:, [-2, -1]]
        modifInput = Xtotal[:, :-2]# +
        
        return (np.concatenate((modifInput, dummyCodingAttempt2(categoricalInputs[:, 0]), dummyCodingAttempt2(categoricalInputs[:, 1])), axis = 1 ))
        
    def outlierRemoval(self, Xtotal):
        W = linReg(Xtotal[:, 1:], Xtotal[:,0])
        prediction = generatePrediction(Xtotal[:, 1:],W, False)
        #prediction = reverseStandardization(prediction)
        residual = Xtotal[:,0] - prediction
        #print(sorted(residual))
        #print(np.where(residual>3.5))
        #print(np.where(residual<-2.8))
        Xtotal = np.delete(Xtotal, np.append(np.where(residual>3.5), np.where(residual<-2.8)) , axis = 0)
        #plt.scatter(range(len(residual)), residual)
        #plt.show()
        return Xtotal
    
    def forwardStageWise(self, Xtotal):
        Xtotal = standardize(Xtotal, False)
        Y = Xtotal[:, 0]
        Xtrain = Xtotal[0:400, 1:]
        Xtest = Xtotal[400:, 1:]
        Ytest = Xtotal[400:, 0]
        #print(Xtrain.shape[1])
        W = np.zeros(Xtrain.shape[1])
        grad = np.zeros(Xtrain.shape[1])
        res = Y[:400]
        #bestfeat = 0
        for iter in range(500):
            #R = res - np.dot(Xtrain, W).flatten()
            #grad = (np.dot(Xtrain.T, R)+ (0.3*W).flatten())/Xtotal.shape[0];
            grad = (np.dot(Xtrain.T, res))/Xtrain.shape[0]
            bestfeat = np.argmax(np.abs(grad))
            W[bestfeat] = W[bestfeat] + grad[bestfeat]
            res = res - Xtrain[:, bestfeat] * grad[bestfeat];
            
        #print(W)
        return L_loss(Ytest, W, Xtest, False)
        
    def polynomialFeatureAddition(self, Xtotal):
        X1=Xtotal[:, 2]
        X2=Xtotal[:, 4]
        X3=Xtotal[:, 6]
        XRemaining = Xtotal[:, 1] + Xtotal[:, 3] + Xtotal[:, 5] + Xtotal[:, 7:]
        polyFeatureSet = [X1, X2, X3, X1**2, X2**2, X3**2, X1*X2, X2*X3, X1*X3]
        return XRemaining+polyFeatureSet
    
    

Xtotal = np.genfromtxt('regression_hw.csv', delimiter = ',')
Xtotal = morphFeaturesAfterDummyCoding(Xtotal)
#Xtotal = polynomialFeatureAddition(Xtotal)
#Xtotal = outlierRemoval(Xtotal)
#print(Xtrain.shape)
#print(
linRegAndLossCalc(Xtotal, True, 400)
#)
#print(
forwardStageWise(Xtotal)
#)



''' 
Xtest = Xtrain[-100:0, 1:]
ytrain = Xtrain[:400, 0]
Xtrain = Xtrain[:, 1:]



Xtest = np.genfromtxt('regression_hw_testx.csv', delimiter = ',')
clf = LinearRegression()
clf.fit(Xtrain,ytrain)
print(clf.predict(Xtest))'''