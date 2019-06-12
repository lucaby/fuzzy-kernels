import unittest
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from  fs.kernels import *

# tests with linear kernel
class TestKernels(unittest.TestCase):

    # unique observation with unique feature
    def test_single(self):
        X = 3
        Y = 4
        #self.assertEqual(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(np.array(X).reshape(-1, 1),np.array(Y).reshape(-1, 1))).all(),)

    def test_tuples(self):# unique observation with multiple features
        X = [3,3]
        Y = [4,4]
        #self.np.array_equal(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(np.array(X).reshape(1, -1),np.array(Y).reshape(1, -1))).all(),"Should be equal")

    def test_tuples(self):  # multiple observations with unique features
        X = [[3], [4]]
        Y = [[4], [5], [7]]
        # self.np.array_equal(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue( (my_kernel( X, Y ) == linear_kernel( np.array( X ).reshape( -1, 1 ),
                                                              np.array( Y ).reshape( -1, 1 ) )).all(),
                         "Should be equal" )

    def test_list_tuples(self):#several observations with several features
        X=[[3,3], [4,4]]
        Y=[[4,3], [4,4]]
        #np.array_equal(my_kernel(X, Y),linear_kernel(X,Y), "Should be equal")
        self.assertTrue((my_kernel(X, Y) == linear_kernel(X,Y)).all(),"Should be equal")

    def test_cross_product_kernel_linear(self):
        val=1*5*0.3*0.7 + 1*6*0.3*0.8 + 2*5 * 0.4 *0.7 +2*6*0.4*0.8

        X = FuzzySet( [1, 2], md=[0.3, 0.4] )
        Y = FuzzySet( [5,  6], md=[0.7, 0.8])

        self.assertAlmostEqual( cross_product_kernel(X,Y,linear_kernel,'',linear_kernel,'') , val, places=3, msg="Should be equal" )
        self.assertAlmostEqual( cross_product_kernel(X,Y,my_kernel,'',my_kernel,'') , val,places=3, msg="Should be equal" )

if __name__ == '__main__':
   
    unittest.main()  
