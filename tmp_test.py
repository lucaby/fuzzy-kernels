from fs.fuzzyset import *
from fs.kernels import *
from fs.memberships import *
from utils.plots import *
import numpy as np
from numpy.random import uniform

elements1 = uniform(1, 100, 100)
elements2 = uniform(1, 100, 100)
mf = gaussmf
params1 = [np.mean(elements1), np.std(elements1)]
params2 = [np.mean(elements2), np.std(elements2)]

fs1 = FuzzySet(elements1, mf=mf, params=params1)
fs2 = FuzzySet(elements2, mf=mf, params=params2)

fs1.show_class()
fs2.show_class()

plot1D(fs1)
plot1D(fs2)