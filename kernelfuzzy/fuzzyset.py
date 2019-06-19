"""

    Class FuzzySet

"""

class FuzzySet:

    _elements      = None  # Elements of the set
    _elements_type = None  # Object type of elements
    _mf            = None  # Membership function
    _md            = None  # Membership degrees of each element from set
    _params        = None  # Custom parameters of any function

    def __init__(self, elements=None, md=None, mf=None, params=None):
        
        """

        Initializes a fuzzy set
    
        Input:
            elements: (Type: numpy.array) elements of the set
            md:       (Type: numpy.array) membership degrees
            mf:       (Type: callable)    membership function
            params:   (Type: list)        function custom parameters
        
        Output:
            (Type: Object "FuzzySet")

        """
        
        #FIRST TYPE: empty fuzzy set
        if elements is None and  md is None and mf is None and params is None:
            self._elements = None
            self._elements_type = None
            self._md = md = None
            self._params = params = None
            self._mf = None

        #SECOND TYPE: elements and membership degrees (md) are given but not the membership function (mf)
        if elements is not None:
            self._elements = elements
            if isinstance(self._elements, (float, int)):
                self._elements_type = type(elements)
            else:
                self._elements_type = type(elements[0])

        if elements is not None and mf is None:
            self._md=md

        # THIRD TYPE: elements and membership function (mf) are given, then the membership degrees are estimated
        if elements is not None and md is None:
            self._params = params
            self._mf = mf
            self._md = self._mf(self._elements, *self._params)

    def set_md(self, md):

        """

        Set the membership degrees

        Input:
            md: (Type: float)

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
        
        if  isinstance(self._elements,  (float, int)) and isinstance(self._md,  (float, int)):
            return list(zip(list([self._elements]),list([self._md])))
        else:
            return list(zip(self._elements,self._md))

    def get_degrees(self):
        
        """

        Returns the membership degrees

        """
        
        return self._md

    def show_class(self):

        """

        Print in the stdout the all the contents of the class, for debugging

        """

        print("_elements      = ", self._elements)   
        print("_elements_type = ", self._elements_type)   
        print("_mf            = ", self._mf)   
        print("_md            = ", self._md)   
        print("_params        = ", self._params)   
