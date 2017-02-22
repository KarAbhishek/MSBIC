# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:14:23 2016

@author: Abhishek
"""
import numpy as np
import matplotlib.pyplot as plt
centers = [1,3,5,7,9,11,13,15,17,19,21,23,25,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
dotprods = [10.010,10.050,9.939,9.313,7.705,4.740,0.501,-4.032,-6.795,-5.313,1.432,10.750,16.244,3.132,-0.111,-0.219,3.383,9.836,16.909,21.754,22.195,18.014,11.458,6.424,6.423,12.292,21.174,27.851,28.085,21.945,14.420,12.139,18.054,28.342,34.912]
b=np.zeros((35,35))
print(b)
for i in range(35):
   for j in range(35):   
       b[i][j] = np.exp(-1 * np.power(centers[i]-centers[j],2)/2)
       
x = np.linalg.solve(b,dotprods)        

y = np.linspace(1,50,100)
print(x)
   
sum = 0
for i, elem in enumerate( centers ):
  sum += np.exp( (-0.5)*(np.subtract(y,elem))**2 )*x[i]
   
   
plt.plot( y, sum )

plt.title("")
plt.xlabel("Y for range [1,50]")
plt.ylabel("Co-efficients of f: f is an element of span({b1,b2,…}))")
plt.show()
    