import unittest
from fs.fuzzyset import *
from fs.memberships import *
from numpy.random import uniform

class TestFuzzySet(unittest.TestCase):

    def test_types(self):
        elements = uniform(1, 100)
        self.assertIs(type(elements), numpy.array)

        elements_type = type(elements[0])
        self.assertIsNotNone(elements_type)

        mf = gaussmf
        self.assertTrue(callable(mf))

        md = uniform()
        self.assertIs(type(md), numpy.array)