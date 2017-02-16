import os
import csv
import numpy as np
from Machine_Learning_10601.python import NB

# Point to data directory here
# By default, we are pointing to '../data/'
data_dir = os.path.join('..','data')

# Read vocabulary into a list
# You will not need the vocabulary for any of the homework questions.
# It is provided for your reference.
with open(os.path.join(data_dir, 'vocabulary.csv'), 'r') as f:
    reader = csv.reader(f)
    vocabulary = list(x[0] for x in reader)

# Load numeric data files into numpy arrays
XTrain = np.genfromtxt(os.path.join(data_dir, 'XTrain.csv'), delimiter=',')
yTrain = np.genfromtxt(os.path.join(data_dir, 'yTrain.csv'), delimiter=',')
#XTrainSmall = np.genfromtxt(os.path.join(data_dir, 'XTrainSmall.csv'), delimiter=',')
#yTrainSmall = np.genfromtxt(os.path.join(data_dir, 'yTrainSmall.csv'), delimiter=',')
XTest = np.genfromtxt(os.path.join(data_dir, 'XTest.csv'), delimiter=',')
yTest = np.genfromtxt(os.path.join(data_dir, 'yTest.csv'), delimiter=',')

# TODO: Test logProd function, defined in NB.py
print('Shit is happening')
assert(np.log(6) == NB.logProd([np.log(2), np.log(3)]))

# TODO: Test NB_XGivenY function, defined in NB.py
D = NB.NB_XGivenY(XTrain, yTrain, 2, 2)

# TODO: Test NB_YPrior function, defined in NB.py
p = NB.NB_YPrior(yTrain)

# TODO: Test NB_Classify function, defined in NB.py
print(NB.NB_Classify(D, p, XTest))
# TODO: Test classificationError function, defined in NB.py

# TODO: Run experiments outlined in HW2 PDF