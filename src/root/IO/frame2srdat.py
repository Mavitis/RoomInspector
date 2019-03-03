
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def frame2srdat(frame, camType):

    # Local Variables: frame, srMatrix, u, amp, y, x, z, camType
    # Function calls: frame2srdat, reshape, zeros
    #% srMatrix = frame2srdat(frame, camType)
    x = frame.points3D_org[0,:]/1000.
    y = frame.points3D_org[1,:]/1000.
    z = frame.points3D_org[2,:]/1000.
    amp = frame.amplitudes
    x = np.reshape(x, (camType.width), np.array([])).conj().T
    y = np.reshape(y, (camType.width), np.array([])).conj().T
    z = np.reshape(z, (camType.width), np.array([])).conj().T
    amp = np.reshape(amp, (camType.width), np.array([])).conj().T
    u = np.zeros(1., np.dot(camType.width, camType.height))
    u[int((frame.usage))-1] = 1.
    u = np.reshape(u, (camType.width), np.array([])).conj().T
    srMatrix = np.array(np.vstack((np.hstack((z)), np.hstack((x)), np.hstack((y)), np.hstack((amp)), np.hstack((u)))))
    return [srMatrix]