
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def get4ngb(rows, cols, x, y):

    # Local Variables: y, x, rows, cols, ngb
    # Function calls: get4ngb
    #% function ngb = get4ngb(rows,cols,x,y)
    #% x = row, y = column
    #% This function returns the cooridinates of the 4-neighbours
    #% of an element in a matrix.  The values are returned in the
    #% list ngb.  If the neighbour does not exist,- that is (x,y)
    #% corredsponds to an edge or corner of the array,
    #% the list of neighbours contains only those coordinates corresponding
    #% to real neighbours.
    #% Copyright Lars Aurdal/FFIE.
    #% Handle left edge.
    #% Handle upper left corner.
    return [ngb]