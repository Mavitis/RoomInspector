import sys
import numpy as np
import scipy
import matcompat
from root.PlaneExtraction.local_plane_patches import local_plane_patches

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def copy_NgbIndx(fr, ind):
    np.disp('copy_NgbIndx ...')
    # Local Variables: fr, d, notplanar, planarIndx, h, camType, planar, dev, thres_dev, w, normals, notPlanarIndx, frame
    # Function calls: std, local_plane_patches, compute_normals, ismember, find, mean
    #%% frame = compute_normals(fr, camType)
    frame = fr
    indx8=ind
    frame.indx8 = indx8

    return frame