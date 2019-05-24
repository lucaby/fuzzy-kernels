"""

    Membership functions

"""

import numpy as np

def gaussmf(elems, mean, sigma):
    
    """

    Gaussian membership function for

    Input:
        elems: (Type: numpy.array) elements of the set
        mean:  (Type: real)        mean of the set
        sigma: (Type: real)        standart deviation of the set, or
               (Type: numpy.array) covariance matrix
        
    Output:
        (Type: real) membership degrees

    """
    
    # For d-dimensional sets
    if type(elems[0]) is not float:
        return np.exp(-np.transpose(elems - mean) * np.linalg.inv(sigma) * (elems - mean))

    return np.exp(-((elems - mean)**2.) / (2 * sigma**2.))