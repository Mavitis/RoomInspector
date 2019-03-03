
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def tidyup_patches(patches):

    # Local Variables: patches, means, coeff, scores, mi, indx, values, x, threshold, patchesTidy, bins
    # Function calls: princomp, false, min, hist, abs, cellfun, find, tidyup_patches, mean
    #% patchesTidy = tidyUp_patches(patches)
    [coeff, scores] = cellfun(lambda x: princomp(x.conj().T), cellarray(np.hstack((patches.pnts))), 'UniformOutput', false)
    means = cellfun(lambda x: np.mean(np.abs(x[:,2])), scores, 'UniformOutput', false)
    means = np.array(np.hstack((means.cell[0:])))
    [bins, values] = plt.hist(means)
    [mi, indx] = matcompat.max(bins)
    threshold = values[int(indx)-1]
    patchesTidy = patches[int(nonzero((means<threshold)))-1]
    return [patchesTidy]