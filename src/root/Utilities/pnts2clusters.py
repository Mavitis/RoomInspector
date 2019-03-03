
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def pnts2clusters(pnts, indx):

    # Local Variables: last, cl, i, indx, clIndx, p, pnts, first
    # Function calls: max, find, pnts2clusters, min
    #%% [cl, clIndx] = pnts2clusters(pnts, indx)
    cl = np.array([])
    clIndx = np.array([])
    #%% determine clusternumbers:
    first = matcompat.max(indx)
    #%first = 1;
    last = matcompat.max(indx)
    i = first
    while i<=last:
        p = nonzero((indx == i))
        cl = np.array(np.hstack((cl, cellarray(np.hstack((pnts[:,int(p)-1]))))))
        clIndx = np.array(np.hstack((clIndx, cellarray(np.hstack((p.conj().T))))))
        i = i+1.
        
    return [cl, clIndx]