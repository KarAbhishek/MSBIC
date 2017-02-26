# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:16:15 2016

@author: user
"""

import numpy as np

import matplotlib.pyplot as plt

data = np.genfromtxt('sample.csv', delimiter='')

sorted_data = np.sort(data)

yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
# Generate some data.
x = sorted_data
y = 1-yvals

plt.loglog(x,y, basex=10, basey=10)
plt.show()