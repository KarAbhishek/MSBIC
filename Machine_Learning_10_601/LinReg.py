import os
import math
import numpy as np
import random
#Ramesh Oswal made me understand that numpy operators broadcast implicitly and dont need to be looped through to take effect.

def add_bias(XTrain, XTest):
    bias_Train = np.ones((1, XTrain.shape[0]))
    bias_Test = np.ones((1, XTest.shape[0]))
    XTrain = np.concatenate([bias_Train.T, XTrain], axis=1)
    XTest = np.concatenate([bias_Test.T, XTest], axis=1)
    return XTrain, XTest

def standardize(Xtrain, Xtest):
    #Xtrain_new = np.ones(shape = [Xtrain.shape[0], 1])
    #Xtest_new = np.ones(shape=[Xtest.shape[0], 1])
    for k in range(Xtrain.shape[1]):
        kth_feature = Xtrain[:, k]
        min_feat = min(kth_feature)
        max_feat = max(kth_feature)
        #Xtrain_kth_std  = np.array([(x_k-min_feat)/(max_feat-min_feat) for x_k in kth_feature])
        #Xtest_kth_std = np.array([(x_k - min_feat) / (max_feat - min_feat) for x_k in Xtest[:, k]])
        Xtrain[:, k] = (kth_feature - min_feat)/(max_feat-min_feat)
        Xtest[:, k] = (Xtest[:, k] - min_feat) / (max_feat - min_feat)

        #Xtrain_new = np.concatenate((Xtrain_new, Xtrain_kth_std.T), axis=1)
        #Xtest_new = np.concatenate((Xtest_new, Xtest_kth_std.T), axis=1)
    return Xtrain, Xtest

def  LinReg_ReadInputs(filepath):
    
    #function that reads all four of the Linear Regression csv files and outputs
    #them as such

    #Input
    #filepath : The path where all the four csv files are stored.

    #output 
    #XTrain : NxK+1 numpy matrix containing N number of K+1 dimensional training features
    #yTrain : Nx1 numpy vector containing the actual output for the training features
    #XTest  : nxK+1 numpy matrix containing n number of K+1 dimensional testing features
    #yTest  : nx1 numpy vector containing the actual output for the testing features

    XTrain = np.genfromtxt('data/LinReg_XTrain.csv', delimiter=',')

    yTrain = np.genfromtxt('data/LinReg_yTrain.csv', delimiter=',')
    XTest = np.genfromtxt('data/LinReg_XTest.csv', delimiter=',')
    yTest = np.genfromtxt('data/LinReg_yTest.csv', delimiter=',')
    XTrain, XTest = standardize(XTrain, XTest)
    XTrain, XTest = add_bias(XTrain, XTest)
    #LinReg_CalcObj(XTrain, yTrain, np.ones(XTrain.shape[1]))
    #LinReg_CalcSG(np.matrix(XTrain[1,:]), yTrain[1], np.ones(XTrain.shape[1]))
    return (XTrain, yTrain, XTest, yTest)
    
def LinReg_CalcObj(X, y, w):

    #function that outputs the value of the loss function L(w) we want to minimize.

    #Input
    #w      : numpy weight vector of appropriate dimensions - num_of_features x 1
    #AND EITHER
    #XTrain : Nx(K+1) numpy matrix containing N number of K+1 dimensional training features
    #yTrain : Nx1 numpy vector containing the actual output for the training features
    #OR
    #XTest  : nx(K+1) numpy matrix containing n number of K+1 dimensional testing features
    #yTest  : nx1 numpy vector containing the actual output for the testing features

    #Output
    #loss   : The value of the loss function we want to minimize

    lossVal = 0
    lossVal = np.square(np.dot(X, w) - y)
    #losl = [i**2 for i in lossVal.tolist()]

    return sum(lossVal)/(len(lossVal))

def LinReg_CalcSG(x, y, w):
    
    #Function that calculates and returns the stochastic gradient value using a
    #particular data point (x, y).

    #Input
    #x : 1x(K+1) dimensional feature point
    #y : Actual output for the input x
    #w : (K+1)x1 dimensional weight vector 


    #Output
    #sg : gradient of the weight vector
    
    #sg = 0
    sg = -2 * (y - np.dot(x, w)) * x
    sg = np.array(sg)[0]
    return sg

def LinReg_UpdateParams(w, sg, eta):
    
    #Function which takes in your weight vector w, the stochastic gradient
    #value sg and a learning constant eta and returns an updated weight vector w.

    #Input
    #w  : (K+   1)x1 dimensional weight vector before update
    #sg : gradient of the calculated weight vector using stochastic gradient descent
    #eta: Learning rate

    #Output
    #w  : Updated weight vector
    w -= eta * sg
    return w
    
def LinReg_SGD(XTrain, yTrain, XTest, yTest):
    
    #Stochastic Gradient Descent Algorithm function

    #Input
    #XTrain : Nx(K+1) numpy matrix containing N number of K+1 dimensional training features
    #yTrain : Nx1 numpy vector containing the actual output for the training features
    #XTest  : nx(K+1) numpy matrix containing n number of K+1 dimensional test features
    #yTest  : nx1 numpy vector containing the actual output for the test features
    
    #Output
    #w    : Updated Weight vector after completing the stochastic gradient descent
    #trainLoss : vector of training loss values at each epoch
    #testLoss : vector of test loss values at each epoch
    
    trainLoss = []
    testLoss = []
    #theta = np.zeros(fill_here)


    w = np.empty(XTrain.shape[1])
    w.fill(0.5)
    counter = 1
    for t in range(100):
        for i in range(XTrain.shape[0]):
            eta = (0.5/((counter)**(0.5)))
            #pick i from uniform dist
            #i = random.randint(0, XTrain.shape[0])
            delta_J_w = LinReg_CalcSG(np.matrix(XTrain[t, :]), yTrain[t], w)
            w = LinReg_UpdateParams(w, delta_J_w, eta)
            counter += 1

        trainLoss.append(LinReg_CalcObj(XTrain, yTrain, w))
        testLoss.append(LinReg_CalcObj(XTest, yTest, w))
    
    return (w, trainLoss, testLoss)
    
def plot():     # This function's results should be returned via gradescope and will not be evaluated in autolab.
    
    return None
    

    
if __name__ == '__main__':
    (XTrain, yTrain, XTest, yTest) = LinReg_ReadInputs('')
    print(LinReg_SGD(XTrain, yTrain, XTest, yTest))


# #theta = np.zeros(fill_here)
#     J_w = LinReg_CalcObj(x, y, w)
#     learning_rate =
#     for t in range(1, T+1):
#         #pick i from uniform dist
#         i = random.randint(0, x.shape[0])
#         delta_J_w = -2*np.dot((y[i] - np.dot(w.T,x[i, :])), x[i, :])
#
#         learning rate = gamma
#         w -= gamma * delta J(theta)