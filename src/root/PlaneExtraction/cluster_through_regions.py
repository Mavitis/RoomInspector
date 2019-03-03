
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cluster_through_regions(fr, cam, display):

    # Local Variables: fr, imRegions, imDis, posEdges, edgesIndx, pos, display, regions, width, bwDis, edges, pnts, cam, usage, curr, height, regionsIndx, se, posCurr
    # Function calls: false, cluster_through_regions, strel, reshape, imdilate, nargin, length, edge, isempty, edge_region_growing, show_clusters, imerode, find
    #%% [regions, regionsIndx] = cluster_through_regions(fr, cam, display)
    #%
    #% points lying inside connected edges = regions are clustered
    #% usage: specify which points in 'pnts' will be used
    #% display: 1 - visualize clusters; 0 - no visulaization (optinal; default: 0)
    #%% some default settings:
    if nargin<3.:
        display = false
    
    
    pnts = fr.points3D[0:3.,:]
    width = cam.width
    height = cam.height
    usage = fr.usage
    #%% compute edge image and indices of these edges
    se = strel('square', 5.)
    imDis = np.reshape(pnts[2,:], width, np.array([])).conj().T
    #%imDis = imerode(imdilate(imDis, se), se);
    bwDis = edge(imDis, 'canny')
    bwDis = imerode(imdilate(bwDis, se), se)
    imRegions = edge_region_growing(bwDis)
    imRegions = np.reshape(imRegions.conj().T, 1., np.array([]))
    imRegions = imRegions[int(usage)-1]
    pos = np.arange(1., (length(pnts))+(1.), 1.)
    pos = pos[int(usage)-1]
    #%% find edges in image (are denoted by -2)
    posEdges = nonzero((imRegions == -2.))
    edges = pnts[:,int(pos[int(posEdges)-1])-1]
    edgesIndx = posEdges
    imRegions[int(posEdges)-1] = np.array([])
    pos[int(posEdges)-1] = np.array([])
    #%% region growing
    regions = np.array([])
    regionsIndx = np.array([])
    curr = 0.
    while not isempty(imRegions):
        curr = imRegions[0]
        posCurr = nonzero((imRegions == curr))
        regions.cell[int((length[int(regions)-1]+1.))-1] = pnts[:,int(pos[int(posCurr)-1])-1]
        regionsIndx.cell[int((length[int(regionsIndx)-1]+1.))-1] = pos[int(posCurr)-1]
        imRegions[int(posCurr)-1] = np.array([])
        pos[int(posCurr)-1] = np.array([])
        
    #%regions{length(regions)+1} = edges;
    #%regionsIndx{length(regionsIndx)+1} = posEdges;
    if display:
        show_clusters(regions, 100.)
    
    
    return [regions, regionsIndx, edges, edgesIndx]