import sklearn
import skfuzzy 
import numpy as np

class FuzzySet:

    _fuzzed_dataset = None

    # Constructor
    def __init__(self, dataset, function):
        self._fuzzed_dataset = self.Fuzzificate(dataset, function)

    # Builds a fuzzy set, using a function provided in the 
    # "skfuzzy" library
    def Fuzzificate(self, dataset, function):
        if function is "gauss":
            mi = np.mean(dataset)
            sigma = np.std(dataset)
            return skfuzzy.gaussmf(dataset, mi, sigma)

    # Prints the fuzzyfied set, aka "_fuzzed_set"
    def ShowSet(self):
        print(self._fuzzed_dataset)



"""
# List of kernel methods, provided in the "sklearn" library
#def 
#
#def GaussKernel(X, Y):
#    rbf_kernel(x.reshape(1, -1),y.reshape(1, -1))

    
random_dataset = np.random.uniform(0, 100, 100)
print(random_dataset)

fuzz = FuzzySet(random_dataset, "gauss")
fuzz.ShowSet()
# Implement cross-product from Roher's paper (Equation 11)
"""
