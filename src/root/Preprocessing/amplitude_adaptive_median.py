
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def amplitude_adaptive_median(dis, amp, camType):

    # Local Variables: distances, dis2, dis3, maxAmp, dis1, minAmp, u1, camType, t2, u3, t1, range, amp, u2, dis
    # Function calls: medfilt2, max, amplitude_adaptive_median, find, min
    distances = dis
    dis1 = medfilt2(dis, np.array(np.hstack((7., 7.))))
    dis2 = medfilt2(dis, np.array(np.hstack((5., 5.))))
    dis3 = medfilt2(dis, np.array(np.hstack((3., 3.))))
    t1 = 0.
    t2 = 0.
    minAmp = matcompat.max(matcompat.max(amp))
    maxAmp = matcompat.max(matcompat.max(amp))
    range = maxAmp-minAmp
    t1 = minAmp+np.dot(1./3., range)
    t2 = minAmp+np.dot(2./3., range)
    u1 = nonzero((dis<t1))
    u2 = nonzero(np.logical_and(dis >= t1, dis<t2))
    u3 = nonzero((dis >= t2))
    distances[int(u1)-1] = dis1[int(u1)-1]
    distances[int(u2)-1] = dis2[int(u2)-1]
    distances[int(u3)-1] = dis3[int(u3)-1]
    return [distances]