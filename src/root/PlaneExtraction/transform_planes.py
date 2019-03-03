
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def transform_planes(planes, m):

    # Local Variables: d, i, coeff, m, n, planesMoved, planes, pnts
    # Function calls: princomp, transform_planes, length, ones, size, mean
    #% planesMoved = transform_planes(planes, m)
    planesMoved = planes
    n = length(planes)
    i = 1.
    while i<=n:
        pnts = np.array(np.vstack((np.hstack((planes[int(i)-1].pnts)), np.hstack((np.ones(1., matcompat.size((planes[int(i)-1].pnts), 2.)))))))
        pnts = np.dot(m, pnts)
        planesMoved[int(i)-1].pnts = pnts[0:3.,:]
        coeff = princomp(pnts.conj().T)
        planesMoved[int(i)-1].n = coeff[0:3.,2]
        planesMoved[int(i)-1].d = np.dot(planesMoved[int(i)-1].n.conj().T, np.mean((planesMoved[int(i)-1].pnts), 2.))
        i = i+1.
        
    return [planesMoved]