
import numpy as np
import scipy
import matcompat
from get_expansion import get_expansion

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def get_plane_expansion(plane):
    np.disp(('Trwa wykonywanie: get_plane_expansion'))

    # Local Variables: a, base2, scale2, s1max, s1min, area, s2min, s2max, shape, base1, s, plane, b1, b2, scale1
    # Function calls: get_plane_expansion, get_expansion
    #% plane = get_plane_expansion(plane)
    [a, s, b1, b2, s1min, s1max, s2min, s2max] = get_expansion((plane.pnts))
    plane.area = a
    plane.shape = s
    plane.base1 = b1
    plane.base2 = b2
    plane.scale1 = np.array(np.hstack((s1min, s1max)))
    plane.scale2 = np.array(np.hstack((s2min, s2max)))
    return [plane]