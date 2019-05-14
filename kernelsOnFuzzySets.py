#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:19:01 2019

@author: jorgeluisguevaradiaz
"""
import itertools
import numpy 
from  sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import polynomial_kernel
from sklearn.metrics.pairwise import rbf_kernel

#----KERNEL ON SETS
def crossProductSets(A,B,kernel, *args):
    '''
    A={1,2,3}
    B={3,4}
    print(kernelOnSets(A,B,linear_kernel))
    print(kernelOnSets(A,B,polynomial_kernel,1))
    
    '''
    params=flatten(args)
    vals=list(itertools.product(*list([A,B])))
    
    return np.sum([kernel(np.array(i).reshape(-1, 1),
            np.array(j).reshape(-1, 1),
            params)for i,j in vals])

    
#----KERNEL ON FUZZYSETS

#TODO: see how to reuse code from scikit learn
def crossProductLinear(X,Y):
    x=X._elements*X._membershipDegrees
    y=Y._elements*Y._membershipDegrees
    #all the posible combinations
    vals=list(itertools.product(*list([x,y])))
    return numpy.sum([numpy.prod(val) for val in vals])



#Util functions
def flatten(*args):
        output = []
        for arg in args:
            if hasattr(arg, '__iter__'):
                output.extend(flatten(*arg))
            else:
                output.append(arg)
        return output       

