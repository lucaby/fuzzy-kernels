"""

    Class FuzzySet

"""

import skfuzzy
import numpy as np

class FuzzySet:

    _X      = None  # Elements of the set
    _X_type = None  # Object type of elements
    _mf     = None  # Membership function
    _md     = None  # Membership degrees of each element from set
    _params = None  # Custom parameters of any function

    def __init__(self, X, mf, params):
        
        """

        Initializes a fuzzy set
    
        Input:
            X:      (Type: numpy.array)     elements of the set
            mf:     (Type: Function)        membership function
            params: (Type: List of objects) function custom parameters
        
        Output:
            (Type: Object "FuzzySet")

        """

        self._X = X
        self._X_type = type(self._X[0])
        self._params = params
        self._mf = mf
        self._md = self._mf(self._X, *self._params)

    def GetSet(self):
        """

        Returns the set

        """
        return self._X

    def GetFunction(self):
        """

        Returns the membership function

        """
        return self._mf

    def GetDegrees(self):
        """

        Returns the membership degrees

        """
        return self._md

    def ShowClass(self):

        """

        Print in the stdout the contents of the class, for debugging

        """

        print("_X      = ", self._X)
        print("_X_type = ", self._X_type)
        print("_mf     = ", self._mf)
        print("_md     = ", self._md)
        print("_params = ", self._params)
        