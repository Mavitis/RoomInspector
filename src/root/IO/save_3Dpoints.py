#Currently not used
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def save_3Dpoints(points3D, filename):

    # Local Variables: points3D, n, points, fid, filename
    # Function calls: reshape, fclose, length, save_3Dpoints, fprintf, fopen
    #% save_3Dpoints(points3D, filename)
    #%
    #% points3D has to have the following structure:
    #%             | p1x p2x p3x p4x ... |
    #% points 3D = | p1y p2y p3y p4y ... |
    #%             | p1z p2z p3z p4z ... |
    points = points3D
    n = matcompat.length(points)
    #%transformation of z-values to negative values, because of the display
    #%settings of viewer (ptcvis)
    points[2,:] = np.dot(points[2,:], -1.)
    points = np.reshape(points, 1., (3.*n))
    #%points = [camType.height camType.width points];
    points = np.array(np.hstack((1., n, points)))
    fid = fopen(filename, 'w')
    fprintf(fid, '%g ', points)
    fclose(fid)
    return 