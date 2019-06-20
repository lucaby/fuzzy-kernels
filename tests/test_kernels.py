import unittest
import numpy as np
from sklearn.metrics import pairwise
from kernelfuzzy.fuzzyset import FuzzySet 
from kernelfuzzy import kernels

# tests with linear kernel
class TestKernels(unittest.TestCase):

    # unique observation with unique feature
    def test_single(self):
        X = 3
        Y = 4
        #self.assertEqual(kernels.linear_kernel(X, Y), pairwise.linear_kernel(X, Y), "Should be equal")
        self.assertTrue((kernels.linear_kernel(X, Y) == pairwise.linear_kernel(np.array(X).reshape(-1, 1),np.array(Y).reshape(-1, 1))).all(),)

    # unique observation with multiple features
    def test_tuples_multiple(self):
        X = [3,3]
        Y = [4,4]
        #self.np.array_equal(kernels.linear_kernel(X, Y), pairwise.linear_kernel(X, Y), "Should be equal")
        self.assertTrue((kernels.linear_kernel(X, Y) == pairwise.linear_kernel(np.array(X).reshape(1, -1),np.array(Y).reshape(1, -1))).all(),"Should be equal")

    # multiple observations with unique features
    def test_tuples_unique(self):  
        X = [[3], [4]]
        Y = [[4], [5], [7]]
        # self.np.array_equal(kernels.linear_kernel(X, Y), pairwise.linear_kernel(X, Y), "Should be equal")
        self.assertTrue((kernels.linear_kernel(X, Y) == 
                         pairwise.linear_kernel(np.array(X).reshape(-1, 1), np.array(Y).reshape(-1, 1))).all(),
                         "Should be equal" )

    # several observations with several features
    def test_list_tuples(self):
        X=[[3,3], [4,4]]
        Y=[[4,3], [4,4]]
        #np.array_equal(kernels.linear_kernel(X, Y), pairwise.linear_kernel(X,Y), "Should be equal")
        self.assertTrue((kernels.linear_kernel(X, Y) == pairwise.linear_kernel(X,Y)).all(),"Should be equal")

    # comparison between sklearn method "linear_kernel" with the kernelfuzzy "linear_kernel"
    def test_cross_product_kernel_linear(self):
        val=1*5*0.3*0.7 + 1*6*0.3*0.8 + 2*5 * 0.4 *0.7 +2*6*0.4*0.8

        X = FuzzySet([1, 2],  md = [0.3, 0.4])
        Y = FuzzySet([5,  6], md = [0.7, 0.8])

        self.assertAlmostEqual(kernels.cross_product_kernel(X, Y, kernels.linear_kernel, '', kernels.linear_kernel, ''), val, places=3, msg="Should be equal" )
        self.assertAlmostEqual(kernels.cross_product_kernel(X, Y, pairwise.linear_kernel, '', pairwise.linear_kernel, ''), val, places=3, msg="Should be equal" )

if __name__ == '__main__':
   
    unittest.main()  
