import numpy as np
import math

def minimize_kl():
    theta = np.linspace(1,5,10000)
    p = [1/(1 + 2*theta), theta/(1 + 2*theta), theta/(1 + 2*theta) ]
    q = [0.1,0.4,0.5]
    for i in xrange(len(p)):
        if i == 0:
            total = p[i]*np.log(p[i]/q[i],2)
        else:
            total += p[i]*np.log(p[i]/q[i],2)
            minIdx = np.argmin(total)
            
    print("Minimum KL: {}; Corresponding theta value: {}".\
    format(total[minIdx],theta[minIdx]))