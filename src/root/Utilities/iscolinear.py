
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def iscolinear(p1, p2, p3):

    # Local Variables: p2, p3, c, b, theta1, theta2, beta, p1, bool, a, alpha, gamma
    # Function calls: false, sum, sqrt, nargin, iscolinear, acos, pi, true, size
    #% function bool = test_colinearity(p1, p2, p3)
    return [bool]