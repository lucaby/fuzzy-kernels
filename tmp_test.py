from fs.fuzzysets import *
from fs.kernels import *
from fs.memberships import *
from utils.plots import *
import numpy as np
from numpy.random import uniform

elements = uniform(1, 100, 100)
mf = gaussmf