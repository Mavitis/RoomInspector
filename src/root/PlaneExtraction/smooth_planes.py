
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def smooth_planes(planes):

    # Local Variables: i, dev, n, plane, planesSmoothed, planes, pnts
    # Function calls: length, smooth_planes
    #% planesSmoothed = smooth_planes(planes)
    n = length(planes)
    planesSmoothed = np.array([])
    plane = np.array([])
    i = 1.
    while i<=n:
        plane = planes[int(i)-1]
        dev = np.dot(plane.n.conj().T, plane.pnts)-plane.d
        plane.pnts = plane.pnts-np.dot(plane.n, dev)
        planesSmoothed = np.array(np.hstack((planesSmoothed, plane)))
        i = i+1.
        
    return [planesSmoothed]