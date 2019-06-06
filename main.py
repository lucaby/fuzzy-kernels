#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:12:14 2019

@author: jorgeluisguevaradiaz
"""

from  kernelfuzzy.fuzzysets import FuzzySet
from kernelfuzzy.memberships import *
from plots import plot1D

def main():


if __name__ == "__main__":
        main()
"""
    # Linear cross product kernel on fuzzy sets (1D)
    elements = np.random.uniform(0, 100, 4)
    X = FuzzySet(elements, mf, params_mf)
    elements = np.random.uniform(0, 100, 4)
    Y = FuzzySet(elements, mf, params_mf)
    print("crossProductFuzzySets(X,Y) = ", crossProductFuzzySets(X,Y))

# Class instantiation (2D)
covar = np.array([[1, 0], [0, 1]])
mean = np.random.uniform(0, 100, 2)
elements2D = np.random.multivariate_normal(mean, covar, 10)

mf = gaussmf
params_mf = [mean, covar]
fuzzy2 = FuzzySet(elements2D, mf, params_mf)
fuzzy2.ShowClass()
 
"""

