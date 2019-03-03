
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def voxel_plane_patches(voxel, vList, nbrVoxel):

    # Local Variables: deviation, voxel, curr, d, ngb, cov, i, in, mi, l, n, y, nbrVoxel, ngbPnts, meanPnt, vec, normals, val, x, z, vList
    # Function calls: currIndx, eig, voxel_plane_patches, sum, find_voxel_neigbors, length, min, ismember, repmat, find, size
    #%% [normal, d deviation] = voxel_plane_patches(pnts, ngh)
    return [normals, d, deviation]