import unittest
import numpy as np
from kernelfuzzy.fuzzyset import *
from kernelfuzzy.memberships import *

class TestFuzzySet(unittest.TestCase):

    def test_types(self):
        elements = np.random.uniform(1, 100)
        self.assertIs(type(elements), np.array)

        elements_type = type(elements[0])
        self.assertIsNotNone(elements_type)

        mf = gaussmf
        self.assertTrue(callable(mf))

        md = np.random.uniform()
        self.assertIs(type(md), np.array)