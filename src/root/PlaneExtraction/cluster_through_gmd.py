
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cluster_through_gmd(pnts, display, gmdata):

    # Local Variables: clStd, cl, pnts, score, clusterIndx, slog, cl_set, clusters, log1, sgrad, clIndx, thresh, stdtest, cl_indx, log, obj, center, idx, i, coeff, gmdata, grad, display
    # Function calls: princomp, false, cluster, pnts2clusters, gmdistribution, nargin, cluster_through_gmd, abs, show_clusters, mean, true, size
    #%% clusters = cluster_through_gmd(pnts)
    #%  
    #% This function fits an increasing number of gaussian mixture distribution
    #% to the 3D point data until the log-likelihood falls below 0.8 or starts
    #% to increase again
    return [clusters, clusterIndx, clStd]