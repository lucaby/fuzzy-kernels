"""

    Class FuzzySet

"""

import numpy as np

class FuzzySet:

    _elements      = None  # Elements of the set
    _elements_type = None  # Object type of elements
    _mf            = None  # Membership function
    _md            = None  # Membership degrees of each element from set
    _params        = None  # Custom parameters of any function

    def __init__(self, elements, mf, params):
        
        """

        Initializes a fuzzy set
    
        Input:
            elements: (Type: numpy.array)     elements of the set
            mf:       (Type: Function)        membership function
            params:   (Type: List of objects) function custom parameters
        
        Output:
            (Type: Object "FuzzySet")

        """

        self._elements = elements
        self._elements_type = type(self._elements[0])
        self._params = params
        self._mf = mf
        self._md = self._mf(self._elements, *self._params)

    def GetSet(self):
        """

        Returns the set

        """
        return self._elements

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

        print("_elements      = ", self._elements)
        print("_elements_type = ", self._elements_type)
        print("_mf            = ", self._mf)
        print("_md            = ", self._md)
        print("_params        = ", self._params)
        