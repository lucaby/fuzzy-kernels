"""

    Script for testing class methods and kernel applications

"""

from FuzzySet import FuzzySet
from Kernels import crossProductFuzzySets
import numpy as np
import skfuzzy

# Random elements for fuzzification
elements = np.random.uniform(0, 100, 4)

# Membership function "gaussmf" from "skfuzzy"
gaussmf = skfuzzy.gaussmf

# Parameters of the "gaussmf" function: mean and standard deviation
params_gaussmf = [np.mean(elements),np.std(elements)]

# Class instantiation
fuzzy = FuzzySet(elements, gaussmf, params_gaussmf)
fuzzy.ShowClass()

# Linear cross product kernel on fuzzy sets
elements = np.random.uniform(0, 100, 4)
X = FuzzySet(elements, gaussmf, params_gaussmf)
elements = np.random.uniform(0, 100, 4)
Y = FuzzySet(elements, gaussmf, params_gaussmf)

print("crossProductFuzzySets(X,Y) = ", crossProductFuzzySets(X,Y))