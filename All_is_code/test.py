# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:06:20 2016

@author: user
"""
import numpy as np
def loss(Y, prediction):   
    residual = np.abs(Y - prediction)
    return np.mean(residual**2)
    
    
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

def conditioning(mu_u, meanTerms, validateFeats, valRowIdx, prec, nonNanIdx):
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


meanTerms = np.genfromtxt('10_600_GGM_mean.csv', delimiter = ',')

mu_u = meanTerms[4]
#mu_v = meanTerms[:4]

validateFeats = np.genfromtxt('test.csv', delimiter = ',')
C = np.genfromtxt('10_600_GGM_covariance_matrix.csv', delimiter = ',')
omega_precMatrix = np.genfromtxt('10_600_GGM_precision_matrix.csv', delimiter = ',')
predictedValid = np.zeros(validateFeats.shape[0])#np.validateFeats[:, 4]

#print(validateFeats.shape, predictedValid.shape)
prec = omega_precMatrix
for valRowIdx in range(validateFeats.shape[0]):
    prec, nonNanIdx = marginalize(validateFeats[valRowIdx], C, omega_precMatrix)
    predictedValid[valRowIdx] = conditioning(mu_u, meanTerms, validateFeats, valRowIdx, prec, nonNanIdx)
    print('Element is : ', validateFeats[valRowIdx, 4], predictedValid[valRowIdx])

#predictedValid[0] = mu_u
#validateFeats[0, 4] = mu_u
#print(validateFeats.shape, predictedValid.shape)
#np.savetxt("10_600_GGM_validateFeatures.csv", validateFeats, delimiter=",", fmt='%s')
#print('Loss is : ', loss(validateFeats[0:, 4], predictedValid[0:]))
#print(predictedValid[0])
np.savetxt("10_600_GGM_test_prediction.csv", predictedValid, delimiter=",", fmt='%s')