"""

    Kernel functions for fuzzy and non-fuzzy sets

"""

import itertools
import numpy as np
from  kernelfuzzy.fuzzysets import FuzzySet

def crossProductFuzzySets(X, Y):
    
    """

    Calculates the Cross Product kernel between two fuzzy sets X and Y

    Input:
        X, Y: (Type: FuzzySet object)

    Output:
        (Type: real) kernel result

    """
    
    x = X.GetSet() * X.GetDegrees()
    y = Y.GetSet() * Y.GetDegrees()

    vals = list(itertools.product(*list([x,y])))
    return np.sum([np.prod(val) for val in vals])

def my_kernel(X, Y):
    
    X=np.array(X)
    Y=np.array(Y)
    return np.dot(X, Y.T)

def cross_product_kernel(X : FuzzySet, 
                         Y : FuzzySet,
                         kernel1,
                         params_k1,
                         kernel2,
                         params_k2) -> float:
    
    """

    Calculates the Cross Product kernel between two fuzzy sets X and Y

    Input:
        X, Y: (Type: FuzzySet object)

    Output:
        (Type: real) kernel result

    """
    
    x = X.GetSet() * X.GetDegrees()
    y = Y.GetSet() * Y.GetDegrees()

    vals = list(itertools.product(*list([x,y])))
    return np.sum([np.prod(val) for val in vals])





"""

TO BE IMPLEMENTED

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
"""