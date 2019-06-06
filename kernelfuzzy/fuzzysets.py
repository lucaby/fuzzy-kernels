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
        #types of fuzzy sets (unfortunately python does not support several constructors)
        #FIRST TYPE: elements and membership degrees (md) are given but not the membership function (mf)
        self._elements = elements
        self._elements_type = type(elements[0])

        if mf is None:
            self._md=md

        # SECOND TYPE: elements and membership function (mf) are given, then the membership degrees are estimated

        if md is None:
            self._params = params
            self._mf = mf
            self._md = self._mf(self._elements, *self._params)

    def set_membership_degrees(self,membership_degrees):
        self._md=membership_degrees

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

        print("elements      = ", self._elements)
        print("type of elements = ", self._elements_type)
        print("membership degrees            = ", self._md)

        if self._mf is not None:
            print("membership function           = ", self._mf)
            print("with parameters       = ", self._params)
