import os
import Machine_Learning_10_601.LinReg as linr
import Machine_Learning_10_601.LogReg as logr
import numpy as np

#code for linear regression
XTrain, yTrain, XTest, yTest = linr.LinReg_ReadInputs(os.path.join("..","data"))
print(linr.LinReg_CalcObj(XTrain, yTrain, np.array([1 for i in range(len(XTrain[0]))]) ))
# # print linr.LinReg_CalcSG(XTrain[0], yTrain[0], np.array([np.random.randint(0,10) for i in range(len(XTrain[0]))]) )
# XTrain, yTrain, XTest, yTest = logr.LogReg_ReadInputs(os.path.join("..","data"))
# w, trainLoss, testLoss = linr.LinReg_SGD(XTrain, yTrain, XTest, yTest)
# print w
# print trainLoss
# print logr.LogReg_CalcObj(XTrain,yTrain,[0.5 for i in range(len(XTrain[0]))])
#code for logistic regression
# XTrain, yTrain, XTest, yTest = logr.LogReg_ReadInputs(os.path.join("..","data"))