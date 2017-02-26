# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:00:11 2016
"""
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import pandas as pd
#from sklearn.linear_model import LinearRegression

meanTrain = np.array([0,0])
stdTrain = np.array([0,0])
def standardize(X, standardizeOnlyX):
    modX = X
    #print(X)
    global meanTrain
    global stdTrain
    #print(np.array_equal(meanTrain, np.array([0,0])) and np.array_equal(stdTrain, np.array([0,0])))
    
    if(np.array_equal(meanTrain, np.array([0,0])) and np.array_equal(stdTrain, np.array([0,0]))):
        meanTrain = np.mean(X, axis = 0)
        stdTrain = np.std(X, axis = 0, ddof=1)
    #print(meanTrain,stdTrain)
    if standardizeOnlyX:
        for colIdx in range(len(X[0])):
            modX[:, colIdx] = (X[:, colIdx]-meanTrain[colIdx+1])/stdTrain[colIdx+1]
        return modX
    for colIdx in range(len(X[0])):
        modX[:, colIdx] = (X[:, colIdx]-meanTrain[colIdx])/stdTrain[colIdx]
    #Y[0] = Y[0]-np.mean(Y[0], axis = 0)/np.std(Y[0], axis = 0)
    #print(modX)
    np.savetxt("10_600_Mean.csv", meanTrain, delimiter=",", fmt='%s')
    np.savetxt("10_600_Std.csv", stdTrain, delimiter=",", fmt='%s')
    return modX
    
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
    #print(np.array(lsOflsBinaries))
    return lsOflsBinaries#lsOfBnaryStrings

def L_loss(Y, W, X, isStandardized):
    #print(W.shape)
    #print(X.shape)
    prediction = generatePrediction(X,W, isStandardized)
    np.savetxt("10_600_before_std_prediction.csv", prediction,  delimiter=",", fmt='%s')
    prediction = reverseStandardization(prediction)
    print(prediction)
    np.savetxt("10_600_after_std_prediction.csv", prediction,  delimiter=",", fmt='%s')    
    residual = np.abs(Y - prediction)
    #print(residual)
    #plt.scatter(range(1, len(residual)+1), residual)
    #outlierRemoval(residual)
    return np.mean(residual**2)
    
def generatePrediction(X,W, isStandardized):
    if(isStandardized):
        X = standardize(X, True)
    return np.dot(X, W)
    
def linReg(X, Y):
    return np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))

def reverseStandardization(Y):
    global meanTrain
    global stdTrain
    #ret = np.zeros(len(Y))
    #print(len(Y))
    ret = (Y*stdTrain[0]+meanTrain[0])
    #for colIdx in range(len(Y)):
        #ret[colIdx] = (Y[colIdx]*stdTrain[colIdx]+meanTrain[colIdx])
    print(stdTrain[0])
    print(meanTrain[0])
    return ret
    
def linRegAndLossCalc(Xtrain, isStandardized, testAndTrainDividingRange):
    #print(Xtrain[0:400, :])
    if(isStandardized):
        train = standardize(Xtrain[0:testAndTrainDividingRange, :], False)
    else:
        train = Xtrain
    test = Xtrain[testAndTrainDividingRange:Xtrain.shape[0], :]
    
    train = outlierRemoval(train)
    
    ytrain = train[:, 0]
    Xtrain = train[:, 1:]
    
    Xtest = test[:, 1:]
    ytest = test[:, 0]
    
    W = linReg(Xtrain, ytrain)
    #print(W)
    return L_loss(ytest, W, Xtest, isStandardized)

def morphFeaturesAfterDummyCoding(Xtrain):
    inputs = Xtrain[:, 1:]
    categoricalInputs = inputs[:, [-2, -1]]
    modifInput = Xtrain[:, :-2]# +
    
    return (np.concatenate((modifInput, dummyCodingAttempt2(categoricalInputs[:, 0]), dummyCodingAttempt2(categoricalInputs[:, 1])), axis = 1 ))
    
def outlierRemoval(Xtotal):
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

def forwardStageWise(Xtotal, testAndTrainDividingRange, XtestInput):
    #Xtotal = standardize(Xtotal, False)
    #Y = Xtotal[:, 0]
    train = Xtotal[0:testAndTrainDividingRange, :]
    train = standardize(train, False)
    train = outlierRemoval(train)
    Xtrain = train[:, 1:]
    Y = train[:, 0]
    #Xtrain = standardize(Xtrain, False)
    np.savetxt("10_600_fwdstg_XTrain.csv", Xtrain, delimiter=",", fmt='%s')
    if(XtestInput == None):
        Xtest = Xtotal[testAndTrainDividingRange:, 1:]
        Ytest = Xtotal[testAndTrainDividingRange:, 0]
    else:
        Xtest = XtestInput
        Ytest = np.zeros(Xtest.shape[0])
    #print(Xtrain.shape[1])
    W = np.zeros(Xtrain.shape[1])
    grad = np.zeros(Xtrain.shape[1])
    res = Y[:testAndTrainDividingRange]
    #bestfeat = 0
    for iter in range(500):
        #R = res - np.dot(Xtrain, W).flatten()
        #grad = (np.dot(Xtrain.T, R)+ (0.4*W).flatten())/Xtotal.shape[0];
        grad = (np.dot(Xtrain.T, res) + (0.4*W).flatten())/Xtrain.shape[0]
        bestfeat = np.argmax(abs(grad))
        W[bestfeat] = W[bestfeat] + grad[bestfeat]
        res = res - Xtrain[:, bestfeat] * grad[bestfeat];
        
    print(W)
    return L_loss(Ytest, W, Xtest, True)
'''    
def polynomialFeatureAddition(Xtotal):
    X1=Xtotal[:, 2]
    X2=Xtotal[:, 4]
    X3=Xtotal[:, 6]
    XRemaining = Xtotal[:, 1] + Xtotal[:, 3] + Xtotal[:, 5] + Xtotal[:, 7:]
    polyFeatureSet = [X1**2, X2**2, X3**2, X1*X2, X2*X3, X1*X3]
    return XRemaining+polyFeatureSet
'''    
def polynomialFeatureAddition(X):
    print (X.shape)
    f1 = np.array([[elem**2] for elem in X[:,5]])
    f2 = np.array([[elem**2] for elem in X[:,7]])
    f3 = np.array([[elem[0]*elem[2]] for elem in X[:,5:(7+1)]])
   
    return np.concatenate((X,f1,f2,f3),axis=1)
 

 
 
Xtotal = np.genfromtxt('regression_hw.csv', delimiter = ',')
#plt.scatter(Xtotal, Xtotal)
#scatter_matrix(pd.DataFrame(Xtotal), alpha=0.2, figsize=(6, 6), diagonal='kde')
Xtotal = morphFeaturesAfterDummyCoding(Xtotal)
       
Xtotal = polynomialFeatureAddition(Xtotal)

#np.savetxt("10_600_Dum.csv", Xtotal[0:400, :], delimiter=",", fmt='%s')
#Xtotal = outlierRemoval(Xtotal)
#np.savetxt("10_600_Standardize.csv", standardize(Xtotal[0:400, :], False), delimiter=",", fmt='%s')
#print(Xtrain.shape)
#print(linRegAndLossCalc(Xtotal, True, 400))
#print(apply_cv(pipeline,Xtotal[1:], Xtotal[0],4,scorer=mse))
XtestInput = np.genfromtxt('regression_hw_testx.csv', delimiter = ',')
XtestInput = morphFeaturesAfterDummyCoding(XtestInput)
XtestInput = polynomialFeatureAddition(XtestInput)
print(forwardStageWise(Xtotal, Xtotal.shape[0], XtestInput))
