# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:03:28 2016

@author: user

qq plot 
"""
'''
import numpy as np

measurements = np.random.normal(loc = 20, scale = 5, size=100000)

def qq_plot(data, sample_size):
    qq = np.ones([sample_size, 2])
    np.random.shuffle(data)
    qq[:, 0] = np.sort(data[0:sample_size])
    qq[:, 1] = np.sort(np.random.normal(size = sample_size))
    return qq

print(qq_plot(measurements, 1000))
for sing in measurements:
    yList = 
plot()
'''
#data is a list of y-values sampled from a lognormal distribution
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

data = np.genfromtxt('sample.csv', delimiter='')
d = getattr(stats, 'norm')
param = d.fit(data)
fig = plt.figure()
ax = fig.add_subplot(111)
fig = stats.probplot(data, dist=stats.norm, sparams=param, plot=plt, fit=False)
#These next 3 lines just demonstrate that some plot features
#can be changed independent of the probplot function.
ax.set_title("")
ax.set_xlabel("Quantiles", fontsize=20, fontweight='bold')
ax.set_ylabel("Ordered Values", fontsize=20, fontweight='bold')
plt.show()