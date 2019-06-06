#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:51:36 2019

@author: jorgeluisguevaradiaz
"""
import unittest
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from  kernelfuzzy.kernels import *



# test with linear kernel
class TestClassicalKernel(unittest.TestCase):

    def single(self):
        X=3
        Y=4
        #self.assertEqual(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(np.array(X).reshape(1, -1),np.array(Y).reshape(1, -1))).all(),)

    def tuples(self):
        X=[3,3]
        Y=[4,4]
        #self.np.array_equal(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(np.array(X).reshape(1, -1),np.array(Y).reshape(1, -1))).all(),"Should be equal")
        
    def list_tuples(self):
        X=[[3,3],[4,4]]
        Y=[[4,3],[4,4]]
        #np.array_equal(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(X,Y)).all(),"Should be equal")
        


if __name__ == '__main__':
   
    unittest.main()  
