
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def pnts2plane_classification_rgrowpure(fr, cam, display=0):

    # Local Variables: decider, seq, camType, rest, frames, in, threshold, pnts, patches, ngbIndx, fig, usage, currIndx, fr, workingIndx, patchesIndx, restIndx, allIndx, d, i, n, p, cam, planes, initSeedIndx, display
    # Function calls: plot_3Dpoints, ismember, plane_computation, false, main_plane_extraction, isfield, preprocessing, nargin, length, pnts2plane_classification_rgrowpure, isempty, intersect, show_clusters, unique, find
    #%% [planes, rest, patchesIndx, restIndx] = pnts2plane_classification_rgrow(fr, cam, display)
    #%
    #%   This function is an implementation of the algorithm described Olaf
    #%   Kaehler in "On Fusion of Range and Intensity Information Using
    #%   Graph-Cut for Planar Patch Segmentation
    #%% some default values:
 
    
    #doda seq jako parametr? to jest zabezpieczenie przed niewykonaniem preprocessingu, wiec mozna wstepnie olac
    #if not(hasattr(fr, 'indx8')):
    #    seq.frames = fr
    #    seq.camType = cam
    #    seq = preprocessing(seq, 'ngb')
    #    fr = seq.frames
    
    
    rest = np.array([])
    restIndx = np.array([])
    usage = fr.usage
    pnts = fr.points3D[0:3.,:]
    allIndx = usage
    threshold = 30.
    #%% start region growing:
    patchesIndx = np.array([])
    patches = np.array([])
    i = 1.
    while not isempty(allIndx):
        #% initialize seed:
        
        
    #%% display results:
    if display:
        fig = show_clusters(patches, 50.)
        fig = plot_3Dpoints(rest, 'k', fig)
    
    
    planes = patches
    rest = pnts[:,int(restIndx)-1]
    return [planes, rest, patchesIndx, restIndx]