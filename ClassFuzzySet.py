from sklearn.gaussian_process.kernels import RBF
import skfuzzy 
import numpy as np

class FuzzySet:

    _fuzzed_dataset = None
    _kernel_matrix  = None

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
        if function is "sigmoid":
            threshold = .5
            width = 1
            return skfuzzy.sigmf(dataset, threshold, width)

    # List of kernel methods, provided in the "sklearn" library
    def GaussKernel(self):
        rbf = RBF()
        self._kernel_matrix = rbf(self._fuzzed_dataset.reshape(-1, 1))

    # Prints all class elements, for debug
    def ShowClass(self):
        print("_fuzzed_dataset = ", self._fuzzed_dataset)
        print("_kernel_matrix = \n", self._kernel_matrix)

"""
random_dataset = np.random.uniform(0, 100, 3)
print("dataset = ", random_dataset)

fuzz1 = FuzzySet(random_dataset, "gauss")
fuzz1.GaussKernel()
fuzz1.ShowClass()
"""
