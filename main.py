import numpy as np
import unittest
from sklearn.metrics.pairwise import linear_kernel
from kernelfuzzy.fuzzyset import FuzzySet
from kernelfuzzy.memberships import *
from utils.plots import plot1D
from kernelfuzzy.kernels import cross_product_kernel, linear_kernel

def createToyFuzzyDataSet(num_rows, num_cols):

    [[FuzzySet(elements=np.random.uniform(0, 100, 2), 
               mf=gaussmf, 
               params=[np.mean(np.random.uniform(0, 100, 2)), np.std(np.random.uniform(0, 100, 2))])
      for i in range(num_rows)] for j in range(num_cols)]

def main():
    pass

if __name__ == "__main__":
    main()
