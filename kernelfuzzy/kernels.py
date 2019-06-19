"""

    Kernel functions for fuzzy and non-fuzzy sets

"""

import itertools
import numpy as np
import types
from kernelfuzzy.fuzzyset import FuzzySet
from typing import Callable, List

def linear_kernel(X, Y):
    
    """

    Calculates the linear kernel of two fuzzy sets
    
    Input:
        X: (Type: FuzzySet)
        Y: (Type: FuzzySet) 

    Output:
        (Type: real) kernel result

    """
    
    X = np.array(X)
    Y = np.array(Y)

    return np.dot(X, Y.T)

def cross_product_kernel(X: FuzzySet,
                         Y: FuzzySet,
                         kernel_elements: Callable,
                         params_kernel_elements: List,
                         kernel_degrees: Callable,
                         params_kernel_degrees: List) -> np.ndarray:
    """

    Calculates the Cross Product kernel between two fuzzy sets X and Y

    Input:
        X:                      (Type: FuzzySet)
        Y:                      (Type: FuzzySet)
        kernel_elements:        (Type: Callable)
        params_kernel_elements: (Type: List)
        kernel_degrees:         (Type: Callable)
        params_kernel_degrees:  (Type: List)

    Output:
        (Type: numpy.ndarray) kernel result

    """

    # create cross-product map
    x = X.get_pair()
    y = Y.get_pair()

    cross_product_map = list(itertools.product(*list([x, y])))
    
    # iterate over the cross-product map
    x = [kernel_elements(*input_validation(val[0][0], val[1][0], params_kernel_elements)) for val in cross_product_map]
    y = [kernel_degrees(*input_validation(val[0][1], val[1][1], params_kernel_degrees)) for val in cross_product_map]

    x = np.asarray([float(i) for i in x])
    y = np.asarray([float(i) for i in y])
    return np.dot(x, y)


def input_validation(x: np.ndarray, y: np.ndarray, params: List[float]=''):
    
    """

    Argument validation to be used by sklearn methods.
    By convention rows are observations and columns features.

    Input:
        x:      (Type: np.ndarray)
        y:      (Type: np.ndarray)
        params: (Type: list)

    Output:
        (Type: tuple)

    """
    
    x = np.array(x)
    y = np.array(y)
    
    # unique observation with unique feature
    #     sum(np.array(3).shape) prints 0; sum(np.array([3]).shape) prints 1
    if sum(np.array(x).shape) == 0 or sum(np.array(x).shape) == 1 :
        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)

    # unique observation with multiple features:  np.array([3,3]) for example
    if x.shape[0] > 1 & len(x.shape)==1:
        x = x.reshape(1, -1)
        y = y.reshape(1, -1)

    # multiple observations with unique features
    if x.shape[0]>1 & len(x.shape)>1:
        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)

    arguments=[x,y]

    if type(params) is list:
        for e in params:
            arguments.append(e)
    if params != '' and type(params) is not list:
        arguments.append(params)

    return tuple(arguments)


def gram_matrix_cross_product_kernel(X, Y,
                                     kernel_elements: Callable,
                                     params_kernel_elements: List,
                                     kernel_degrees: Callable,
                                     params_kernel_degrees: List):
    
    '''

    Calculates the Gram matrix of the Cross Product between two fuzzy sets

    Input:
        X:                      (Type: FuzzySet)
        Y:                      (Type: FuzzySet)
        kernel_elements:        (Type: Callable)
        params_kernel_elements: (Type: List)
        kernel_degrees:         (Type: Callable)
        params_kernel_degrees:  (Type: List)

    Output:
        (Type: numpy.ndarray) kernel matrix

    '''

    gram_matrix = np.zeros((X.shape[0], Y.shape[0]))
    for i, tuple_x in enumerate(X):
        for j, tuple_y in enumerate(Y):
            tuple_x = tuple_x
            tuple_y = tuple_y
            # dot-product like operation between tuple of fuzzy sets
            value = 0
            for x, y, in zip(tuple_x, tuple_y):
                value = value + cross_product_kernel(x, y, kernel_elements, params_kernel_elements, kernel_degrees,
                                                     params_kernel_degrees)
            gram_matrix[i, j] = value
    return gram_matrix