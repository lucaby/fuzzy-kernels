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

    #if type(elems[0]) is not  np.float64:
    #    return np.exp(-np.transpose(elems - mean) * np.linalg.inv(sigma) * (elems - mean))

    if isinstance(sigma, np.ndarray):
        sigma=np.linalg.inv(sigma)

    if isinstance(sigma,  (float, int)):
        sigma=1/sigma

    return np.exp(-np.transpose(elems - mean) * sigma * (elems - mean))






