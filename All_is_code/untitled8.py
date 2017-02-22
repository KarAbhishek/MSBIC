# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:16:29 2016

@author: user
"""

import numpy as np 
import pylab 
import scipy.stats as stats

measurements = np.genfromtxt('sample2.csv', delimiter = '') 
print(measurements)
stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()