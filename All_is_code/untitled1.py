# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:30:58 2016

@author: Abhishek
Task 1):
"""

import numpy as np

# Task 1
def task1(features, theta):
    features = np.genfromtxt('features.csv',delimiter = ',')
    #print(features)
    #probabilityOfFeatures = features.mean(axis = 0)
    
    
    gOfThetaB4Log = 0
    for currentFeature in features:
        singl = np.dot(currentFeature, theta)
        gOfThetaB4Log = gOfThetaB4Log + np.e**singl
        gOfTheta = np.log(gOfThetaB4Log)
    
    result = np.array([0])*11
    for currentFeature in features:
        singl = np.dot(currentFeature, theta)
        print('singl:')
        print(singl)
        singl = singl - gOfTheta
        
        result = result + currentFeature * (np.e**singl)
    
    #print(result)
    return result


def task2(features, hwday):
    # Task 2 
    
    resultFeature = [0]*len(features[0])
    for day in hwday:
        resultFeature += features[day-29]
    resultFeature = resultFeature/len(hwday)
    #print(resultFeature)
    
    return resultFeature


#Task 3
def task3(features, theta, hwday):
    theta = np.zeros(11)
    predictedFeatures = np.zeros(11)
    for i in range(1000):
        observedFeatures = task2(features, hwday)
        predictedFeatures = task1(features, theta)
        gradient = observedFeatures - predictedFeatures
        theta = theta + gradient
    print('Predicted : -- ')
    print(predictedFeatures)
    print()    
    
    print('Theta : -- ')
    print(theta)
    

features = np.genfromtxt('features.csv',delimiter = ',')
theta = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
hwday = [31 ,31 ,38 ,43 ,47 ,50 ,54 ,57 ,61 ,64 ,71 ,74 ,80]
print('Task 1 Results : -- ')
print(task1(features, theta))
print()

print('Task 2 Results : -- ')
print(task2(features, hwday))
print()

print('Task 3 Results : -- ')
#task3(features, theta, hwday)


'''
Output for the Code 
Task 1 Results : -- 
[ 0.73442297  0.04534241  0.34159747  0.0471457   0.2123876   0.02932094
  0.28488738  0.03931849  0.05019744  0.11386287  0.83593969]

Task 2 Results : -- 
[ 0.48861538  0.38461538  0.          0.30769231  0.07692308  0.23076923
  0.          0.          0.15384615  0.53846154  0.30769231]

Task 3 Results : -- 
Predicted : -- 
[ 0.48861872  0.3841878   0.00058481  0.30726431  0.07649092  0.23034083
  0.00056329  0.00056805  0.15384791  0.53846175  0.30769034]

Theta : -- 
[ 1.98349134  2.98821319 -3.53915904  2.68743414  1.62357847  2.68726877
 -3.20857809 -3.23875744  1.25972207 -0.14196251 -1.11775955]
'''
