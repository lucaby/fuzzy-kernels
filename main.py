#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:12:14 2019

@author: jorgeluisguevaradiaz
"""
import numpy as np
import unittest
from sklearn.metrics.pairwise import linear_kernel
from  kernelfuzzy.fuzzysets import FuzzySet
from kernelfuzzy.memberships import *
from plots import plot1D
from  kernelfuzzy.kernels import crossProductFuzzySets,cross_product_kernel, my_kernel


def createToyFuzzyDataSet(num_rows, num_cols):

    [    [ FuzzySet(elements=np.random.uniform(0, 100, 2)  , mf=gaussmf, params=[np.mean(np.random.uniform(0, 100, 2)), np.std(np.random.uniform(0, 100, 2))])
 for i in range(num_rows)] for j in range(num_cols)]



def main():



if __name__ == "__main__":
        main()

