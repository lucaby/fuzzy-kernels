"""

    Kernel functions for fuzzy and non-fuzzy sets

"""

import itertools
import numpy as np
from fs.fuzzyset import FuzzySet
from typing import Callable, List
import types

def crossProductFuzzySets(X, Y):

    """

    Calculates the Cross Product kernel between two fuzzy sets X and Y

    Input:
        X, Y: (Type: FuzzySet object)

    Output:
        (Type: real) kernel result

    """

    x = X.get_set() * X.get_degrees()
    y = Y.get_set() * Y.get_degrees()

    vals = list( itertools.product( *list( [x, y] ) ) )
    print(vals)
    return np.sum( [np.prod( val ) for val in vals] )


def my_kernel(X, Y):
    X = np.array( X )
    Y = np.array( Y )
    return np.dot( X, Y.T )


def cross_product_kernel(X: FuzzySet,
                         Y: FuzzySet,
                         kernel_elements: Callable,
                         params_kernel_elements: List,
                         kernel_degrees: Callable,
                         params_kernel_degrees: List) -> np.ndarray:
    """

    Calculates the Cross Product kernel between two fuzzy sets X and Y

    Input:
        X, Y: (Type: FuzzySet object)

    Output:
        (Type: real) kernel result

    """
    # create cross-product map
    x = X.get_pair()
    y = Y.get_pair()

    cross_product_map = list( itertools.product( *list( [x, y] ) ) )
    # iterate over the cross-product map

    x = [kernel_elements(*input_validation(val[0][0], val[1][0],params_kernel_elements)  ) for val in cross_product_map]
    y = [kernel_degrees(*input_validation( val[0][1], val[1][1],params_kernel_degrees) ) for val in cross_product_map]

    x = np.asarray([float(i) for i in x])
    y = np.asarray([float( i ) for i in y])
    return np.dot( x, y )


def input_validation(x: np.ndarray, y: np.ndarray, params: List[float]=''):
    
    """

       Argument validation to be used by sklearn methods
       By convention rows are observations and columns features

       Input:

       Output:

    """
    
    x = np.array( x )
    y = np.array( y )
    # unique observation with unique feature
    #     sum(np.array(3).shape) prints 0; sum(np.array([3]).shape) prints 1
    if sum(np.array(x).shape) == 0 or sum(np.array(x).shape) == 1 :
        x = x.reshape( -1, 1 )
        y = y.reshape( -1, 1 )

    # unique observation with multiple features:  np.array([3,3]) for example
    if x.shape[0] > 1 & len(x.shape)==1:
        x = x.reshape( 1, -1 )
        y = y.reshape( 1, -1 )

    # multiple observations with unique features
    if x.shape[0]>1 & len(x.shape)>1:
        x = x.reshape( -1, 1 )
        y = y.reshape( -1, 1 )

    arguments=[x,y]

    if type(params) is list:
        for e in params:
            arguments.append(e)
    if params!='' and type(params) is not list:
        arguments.append( params )

    return tuple(arguments)
