# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 05:50:22 2016

@author: Abhishek
"""

import numpy as np
def createFeatures(train):
    print(train.shape[0]-5)
    totalFeatures = np.empty((train.shape[0]-5,1));
   
    #print(train.shape[0])
    
    for rowNum in range(6):
        #rowNum = 1
        ls = []
        for i in range(5, train.shape[0]):
            feature = np.array([]);
            for T in range(i-5, i):
                feature = np.append(feature, np.log(train[T+1][rowNum]/train[T][rowNum]))
                #print(np.log10(train[T+1][0]/train[T][0]), end=' ')
            #print(feature.shape)
            
            ls.append(feature)
            #print()
            
        features = np.array(ls)    
        #print('Features here : ', features)
        totalFeatures = np.concatenate((totalFeatures, features), axis = 1)
    
    totalFeatures = np.delete(totalFeatures, 0, 1)    
    np.savetxt("10_600_GGM_trainFeatures.csv", totalFeatures, delimiter=",", fmt='%s')
    return totalFeatures

def createFeature(validate):
    #print(validate.shape[0]-5)
    totalFeatures = np.empty((validate.shape[0],1));
   
    #print(validate.shape[0])
    
    for rowNum in range(6):
        #rowNum = 1
        ls = []
        for i in range(0, validate.shape[0]):
            feature = np.array([]);
            for T in range(i-5, i):
                if(T<0):    
                    feature = np.append(feature, np.nan)
                else:
                    feature = np.append(feature, np.log(validate[T+1][rowNum]/validate[T][rowNum]))
                #print(np.log10(validate[T+1][0]/validate[T][0]), end=' ')
            #print(feature.shape)
            
            ls.append(feature)
            #print()
            
        features = np.array(ls)    
        #print('Features here : ', features)
        #print(totalFeatures.shape, features.shape)
        totalFeatures = np.concatenate((totalFeatures, features), axis = 1)
    
    totalFeatures = np.delete(totalFeatures, 0, 1)    
    np.savetxt("10_600_GGM_validateFeatures.csv", totalFeatures, delimiter=",", fmt='%s')
    return totalFeatures

#def createCovarianceMatrix(rowOfNonNAN):
#    return np.ma.cov(rowOfNonNAN.T, ddof = 0)

def createCovMatrices(train):
    print(1/train.shape[0])
    return (np.dot(train.T,train)/train.shape[0])
    
def centering(trainFeats, meanTerms):
    modtrainFeats = trainFeats
    for colIdx in range(len(trainFeats[0])):
        modtrainFeats[:, colIdx] = (trainFeats[:, colIdx]-meanTerms[colIdx])
    return modtrainFeats

def marginalize(validateFeat, C, omega_precMatrix):
    nanIdxes = np.where(np.isnan(validateFeat))
    nonNanIdxes = np.where(np.isfinite(validateFeat))
    if(len(nanIdxes)!=0):
        C = np.delete(C, nanIdxes, 0)
        C = np.delete(C, nanIdxes, 1)
        omega_precMatrix = np.linalg.inv(C)
    return omega_precMatrix, nonNanIdxes
    #for valColIdx in range(validateFeats.shape[1]):
     #   
      #  if(validateFeats[valRowIdx][valColIdx] == np.nan):
            
       #     recalPrec = True
       #     break
    #if(recalPrec):
     #   omega_precMatrix = recalculatePrecisionMatrix(C)
#def Abv(omega_precMatrix, trainFeats, idx):
#    A = train[idx, idx]
#    b = np.delete(train[idx, :], train)
#    v = trainFeats[idx, idx]

def conditioning(mu_u, meanTerms, validateFeats, valRowIdx, prec, trainShapeColNo, nonNanIdx):
    #idxA = prec.shape[0]/trainShapeColNo
    #A=prec[valRowIdx, idxA]
    
    nonNanIdx = list(nonNanIdx)[0]
#    list4=[]
#    listNot4=[]
#    for idm in range(len(nonNanIdx)):
#        if nonNanIdx[idm] == 4:
#            list4.append(idm)
#        else:
#            listNot4.append(idm)
    is4 = np.where(nonNanIdx == 4)
    isNot4 = np.where(nonNanIdx != 4)
    #A = prec[np.where(nonNanIdx == 4), np.where(nonNanIdx == 4)]
    #A = prec[list4,list4]
    A = prec[is4, is4]
    b = prec[is4, isNot4]
    #b=  prec[list4,listNot4]
    v = validateFeats[valRowIdx, nonNanIdx[isNot4]]
    mu_v = meanTerms[nonNanIdx[isNot4]]
    return (mu_u - np.dot(np.linalg.inv(A), np.dot(b, v-mu_v)) )

def loss(Y, prediction):   
    residual = np.abs(Y - prediction)
    return np.mean(residual**2)
    
train = np.genfromtxt('train.csv', delimiter = ',')
train = np.delete(train, 0, 0)
trainPredictionColMean = (train)

validate = np.genfromtxt('val.csv', delimiter = ',')
validate = np.delete(validate, 0, 0)

test = np.genfromtxt('test.csv', delimiter = ',')

trainFeats = createFeatures(train);
validateFeats = createFeature(validate);

meanTerms = np.mean(trainFeats, axis = 0)

mu_u = meanTerms[5];
mu_v = meanTerms[:4]
#print(meanTerms.shape)
np.savetxt("10_600_GGM_mean.csv", np.matrix(meanTerms), delimiter=",", fmt='%s')

#trainFeats = centering(trainFeats, meanTerms)

#print(trainFeats[:2])
#createCovMatrices(trainFeats[:2])
C = createCovMatrices(trainFeats)
np.savetxt("10_600_GGM_covariance_matrix.csv", C, delimiter=",", fmt='%s')
#print(C)
omega_precMatrix = np.linalg.inv(C)
np.savetxt("10_600_GGM_precision_matrix.csv", omega_precMatrix, delimiter=",", fmt='%s')
#print(omega_precMatrix.shape)

#find A,b,v

predictedValid = np.zeros(validateFeats.shape[0])#np.validateFeats[:, 4]

#print(validateFeats.shape, predictedValid.shape)
prec = omega_precMatrix
for valRowIdx in range(1,validateFeats.shape[0]):
    prec, nonNanIdx = marginalize(validateFeats[valRowIdx], C, omega_precMatrix)
    predictedValid[valRowIdx] = conditioning(mu_u, meanTerms, validateFeats, valRowIdx, prec, train.shape[1], nonNanIdx)
    print('Element is : ', validateFeats[valRowIdx, 4], predictedValid[valRowIdx])

predictedValid[0] = mu_u
validateFeats[0, 4] = mu_u
#print(validateFeats.shape, predictedValid.shape)
#np.savetxt("10_600_GGM_validateFeatures.csv", validateFeats, delimiter=",", fmt='%s')
print('Loss is : ', loss(validateFeats[0:, 4], predictedValid[0:]))
print(predictedValid[0])
#findAbv()