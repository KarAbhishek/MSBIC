import math
import numpy as np


def hasElement(nparray, elem):
    return set(np.where(nparray == elem)[0])

# The logProd function takes a vector of numbers in logspace
# (i.e., x[i] = log p[i]) and returns the product of those numbers in logspace
# (i.e., logProd(x) = log(product_i p[i]))
def logProd(x):
    ## Inputs ##
    # x - 1D numpy ndarray

    ## Outputs ##
    # log_product - float
    log_product = 0
    for i in x:
        log_product += i
    return log_product


# The NB_XGivenY function takes a training set XTrain and yTrain and
# Beta parameters alpha and beta, then returns a matrix containing
# MAP estimates of theta_yw for all words w and class labels y
def NB_XGivenY(XTrain, yTrain, alpha, beta):
    ## Inputs ##
    # XTrain - (n by V) numpy ndarray
    # yTrain - 1D numpy ndarray of length n
    # alpha - float
    # beta - float

    ## Outputs ##
    # D - (2 by V) numpy ndarray

    D = np.zeros([2, XTrain.shape[1]])

    for m in range(XTrain.shape[1]):
        for y_val in [0,1]:
            N__X_M1__and__Y0 = len(hasElement(XTrain[:, m], 1) & hasElement(yTrain, y_val))

            N__Y0 = len(hasElement(yTrain, y_val))
            theta_M1_0_numer = float(N__X_M1__and__Y0)+alpha-1
            theta_M1_0_denom = N__Y0+alpha-1+beta-1

            theta_M1_0 = theta_M1_0_numer/theta_M1_0_denom
            D[y_val, m] = theta_M1_0

    return D


# The NB_YPrior function takes a set of training labels yTrain and
# returns the prior probability for class label 0
def NB_YPrior(yTrain):
    ## Inputs ##
    # yTrain - 1D numpy ndarray of length n

    N__Y0 = len(hasElement(yTrain, 0))
    N__Y = yTrain.shape[0]
    fi_Y_0 = N__Y0/float(N__Y)
    ## Outputs ##
    # p - float

    #p = 0
    #return p
    return fi_Y_0

# The NB_Classify function takes a matrix of MAP estimates for theta_yw,
# the prior probability for class 0, and uses these estimates to classify
# a test set.
def NB_Classify(D, p, XTest):
    ## Inputs ##
    # D - (2 by V) numpy ndarray
    # p - float
    # XTest - (m by V) numpy ndarray

    ## Outputs ##
    # yHat - 1D numpy ndarray of length m


    yHat = np.ones(XTest.shape[0])
    for m in range(XTest.shape[0]):
        maxLogProd = float('-inf')
        for y_val in [0, 1]:
            if y_val == 0:
                fi_Y_1 = 1 - p
            else:
                fi_Y_1 = p
            #N_Y_1 = fi_Y_1 * XTest.shape[0]

            vector_log = [np.log(fi_Y_1)]

            #summation = 0

            for v in range(XTest.shape[1]):
                #summation +=
                if XTest[m, v] == 1:
                    vector_log.append(np.log(D[y_val, v]))
                else:
                    vector_log.append(np.log(1 - D[y_val, v]))
            if maxLogProd < logProd(vector_log):
                maxLogProd = logProd(vector_log)
                yHat[m] = y_val
    return yHat


# The classificationError function takes two 1D arrays of class labels
# and returns the proportion of entries that disagree
def classificationError(yHat, yTruth):
    ## Inputs ##
    # yHat - 1D numpy ndarray of length m
    # yTruth - 1D numpy ndarray of length m

    ## Outputs ##
    # error - float
    error = 0
    for idx in range(len(yHat)):
        if yHat[idx] != yTruth[idx]:
            error += 1
    error /= float(len(yHat))
    return error
