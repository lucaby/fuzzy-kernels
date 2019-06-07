"""

    Class FuzzySet

"""
class FuzzySet:

    _elements      = None  # Elements of the set 
    _elements_type = None  # Object type of elements
    _mf            = None  # Membership function
    _md            = None  # Membership degrees of each element from set
    _params        = None  # Custom parameters of any function

    def __init__(self, elements, md=None, mf=None, params=None):
        
        """

        Initializes a fuzzy set
    
        Input:
            elements: (Type: numpy.array)     elements of the set
            md:       (Type: numpy.array)     membership degrees
            mf:       (Type: Function)        membership function
            params:   (Type: List of objects) function custom parameters
        
        Output:
            (Type: Object "FuzzySet")

        """
        
        # has md, but not mf
        self._elements = elements
        self._elements_type = type(elements[0])

        if mf is None:
            self._md = md

        # has mf, md generated
        if md is None:
            self._params = params
            self._mf = mf
            self._md = self._mf(self._elements, *self._params)

    def set_md(self, md):

        """

        Set the membership values

        Input:
            md:       (Type: numpy.array)     membership degrees
            
        """

        self._md = md

    def get_set(self):
        
        """

        Returns the set

        """
        
        return self._elements

    def get_function(self):
        
        """

        Returns the membership function

        """
        
        return self._mf

    def get_pair(self):
        
        """

        Returns the pair (_elements, _md) elements and membership degree

        """

        return list(zip(self._elements,self._md))

    def get_degrees(self):

        """

        Returns the membership degrees

        """
        
        return self._md

    def show_class(self):

        """

        Print in the stdout the contents of the class, for debugging

        """
        
        print("_elements      = ", self._elements)
        print("_elements_type = ", self._elements_type)
        print("_md            = ", self._md)
        print("_mf            = ", self._mf)
        print("_params        = ", self._params)
