"""

    Script for testing class methods and kernel applications

"""



import numpy as np
import unittest
from sklearn.metrics.pairwise import linear_kernel
from  kernelfuzzy.fuzzysets import FuzzySet
from kernelfuzzy.memberships import * 

def main():
#from kernels import crossProductFuzzySets
#from Plots import *
#from Memberships import gaussmf

# Membership function "gaussmf"

"""
# Class instantiation (1D)
elements = np.random.uniform(0, 100, 100)
mf = gaussmf
params_mf = [np.mean(elements), np.std(elements)]
fuzzy = FuzzySet(elements, mf, params_mf)
fuzzy.ShowClass()

# Linear cross product kernel on fuzzy sets (1D)
elements = np.random.uniform(0, 100, 4)
X = FuzzySet(elements, mf, params_mf)
elements = np.random.uniform(0, 100, 4)
Y = FuzzySet(elements, mf, params_mf)
print("crossProductFuzzySets(X,Y) = ", crossProductFuzzySets(X,Y))

# Plots a 1D fuzzy set
plot1D(fuzzy)
"""
# Class instantiation (2D)
covar = np.array([[1, 0], [0, 1]])
mean = np.random.uniform(0, 100, 2)
elements2D = np.random.multivariate_normal(mean, covar, 10)

mf = gaussmf
params_mf = [mean, covar]
fuzzy2 = FuzzySet(elements2D, mf, params_mf)
fuzzy2.ShowClass()
