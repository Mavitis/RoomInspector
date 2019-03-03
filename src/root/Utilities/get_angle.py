
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def get_angle(n1, n2):

    # Local Variables: n1, n2, angle
    # Function calls: acos, pi, get_angle
    #% angle = get_angle(n1, n2)
    angle = np.arccos(np.dot(n1.conj().T, n2))
    if angle > np.pi/2.:
        angle = np.pi-angle
    
    
    return [angle]