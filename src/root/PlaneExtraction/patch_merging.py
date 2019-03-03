
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def patch_merging(patches, method):

    # Local Variables: patches, nOld, rIndx, rest, n, r, patchesMerged, method, restIndx
    # Function calls: length, patch_merging, merge_planes
    #%% planesMerged = patch_merging(patches, method)
    #%
    #% possible methods:
    #%  - 'mean': uses the mean of the patches
    #%  - 'median': uses the median of the patches
    #%  - 'ngbPatches': uses the nearest neighbor patches
    #%  - 'fastNgbPatches': finds quick nearest neighbor patches 
    nOld = 0.
    n = length(patches)
    rest = np.array([])
    restIndx = np.array([])
    patchesMerged = patches
    while nOld != n:
        [patchesMerged, r, rIndx] = merge_planes(patchesMerged, method)
        rest = np.array(np.hstack((rest, r)))
        restIndx = np.array(np.hstack((restIndx, rIndx)))
        nOld = n
        n = length(patchesMerged)
        
    return [patchesMerged, rest, restIndx]