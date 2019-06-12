"""

    Membership functions

"""

import numpy as np

def gaussmf(elems, mean, sigma):
    
    """

    Gaussian membership function for

    Input:
        elems: (Type: numpy.array) elements of the set
        mean:  (Type: float)       mean of the set
        sigma: (Type: float)       standart deviation of the set, or
               (Type: numpy.array) covariance matrix
        
    Output:
        (Type: real) membership degrees

    """

    # For d-dimensional sets

    #if type(elems[0]) is not  np.float64:
    #    return np.exp(-np.transpose(elems - mean) * np.linalg.inv(sigma) * (elems - mean))

    if isinstance(sigma, np.ndarray):
        sigma=np.linalg.inv(sigma)
        values = np.einsum('ij,ij->i', np.dot((elems-mean),sigma), (elems-mean))
        values = np.exp(-values)

    if isinstance(sigma,  (float, int)):
        values = np.exp(-np.square(elems - mean)/sigma)
    return values







