
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def edge_region_growing(bw, display):

    # Local Variables: pr, c, posZeros, num, ngb, bwZeros, ran, segments, pc, p, display, ngbRC, width, bw, bwOnes, fig, n, height, seed, scrsz
    # Function calls: drawnow, false, figure, get, random_positions, floor, any, nargin, length, zeros, edge_region_growing, get4ngb, mod, find, imagesc, size
    #% segments = edge_region_growing(bw)
    #%
    #% Find all regions in the image "bw" (a black/white image, where edges are shown
    #% white).
    #% A region is defined as an area inside of connected edges
    return [segments]