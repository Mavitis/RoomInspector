import sys
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def sindx2mindx(num, width, height):

    # Local Variables: column, width, height, num, row
    # Function calls: mod, floor, sindx2mindx
    #% [row, column] = sindx2mindx(num, width, height)
    #num ma z dupy wartosc
    #print 'index', num
    row = np.floor(((num-1)/width+1))
    column = np.mod((num-1), width)+1.
    #print 'sind2mindx', row, column
    return [row, column]
    