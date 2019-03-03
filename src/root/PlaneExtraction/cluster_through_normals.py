
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cluster_through_normals(fr, cam, threshold, display):

    # Local Variables: angles, posZeroNormals, camType, pos, threshold, frames, diff, pnts, nCurr, seq, usage, clusters, fr, zeroNormals, pntsZeroNormals, normclusters, iCurr, d, indx, n, pCurr, cam, clustersIndx, display
    # Function calls: cluster_through_normals, false, isfield, show_clusters, nargin, length, preprocessing, isempty, ismember, acos, find
    #% clusters = cluster_through_normals(pnts, normals, threshold, usage, display)
    #%
    #% points with similar normals are clustered
    #% threshold: normals with an Euclidean distance smaller than the threshold value
    #%            are declared as similar
    #% usage: specify which points in 'pnts' will be used (optional; default: use
    #%        all)
    #% display: 1 - visualize clusters; 0 - no visulaization (optinal; default: 0)
    if nargin<4.:
        display = false
    
    
    if not isfield(fr, 'normals'):
        seq.frames = fr
        seq.camType = cam
        seq = preprocessing(seq, 'normals')
        fr = seq.frames
    
    
    n = fr.normals[:,int((fr.usage))-1]
    pnts = fr.points3D[0:3.,int((fr.usage))-1]
    usage = fr.usage
    pos = np.arange(1., (np.dot(cam.width, cam.height))+(1.), 1.)
    pos = pos[int(usage)-1]
    clusters = np.array([])
    normclusters = np.array([])
    diff = np.array([])
    d = np.array([])
    #% find [0;0;0] normals
    posZeroNormals = ismember(n, np.array(np.vstack((np.hstack((0.)), np.hstack((0.)), np.hstack((0.))))))
    posZeroNormals = np.logical_and(np.logical_and(posZeroNormals[0,:], posZeroNormals[1,:]), posZeroNormals[2,:])
    zeroNormals = n[:,int(posZeroNormals)-1]
    pntsZeroNormals = pnts[:,int(posZeroNormals)-1]
    n = n[:,int((not posZeroNormals))-1]
    pnts = pnts[:,int((not posZeroNormals))-1]
    pos = pos[:,int((not posZeroNormals))-1]
    while not isempty(n):
        nCurr = n[:,0]
        pCurr = pnts[:,0]
        iCurr = pos[0]
        n[:,0] = np.array([])
        pnts[:,0] = np.array([])
        pos[0] = np.array([])
        #% conormality measure:
        #% computes angle between two normals n1 and n2
        #% angle = acos(n1 * n2) (Scalar Product)
        angles = acos(np.dot(nCurr.conj().T, n))
        indx = nonzero((angles<threshold))
        #% diff = [n(1,:) - nCurr(1); n(2,:) - nCurr(2); n(3,:) - nCurr(3)];
        #% d = sum(diff.^2,1);
        #% indx = find(d < threshold);
        #% cluster points with similar normals
        clusters.cell[int((length[int(clusters)-1]+1.))-1] = np.array(np.hstack((pCurr, pnts[:,int(indx)-1])))
        clustersIndx.cell[int((length[int(clusters)-1]+1.))-1] = np.array(np.hstack((iCurr, pos[int(indx)-1])))
        normclusters.cell[int((length[int(normclusters)-1]+1.))-1] = np.array(np.hstack((nCurr, n[:,int(indx)-1])))
        #% remove clustered points from the working set
        n[:,int(indx)-1] = np.array([])
        pnts[:,int(indx)-1] = np.array([])
        pos[int(indx)-1] = np.array([])
        
    normclusters.cell[int((length[int(normclusters)-1]+1.))-1] = zeroNormals
    clusters.cell[int((length[int(clusters)-1]+1.))-1] = pntsZeroNormals
    if display:
        show_clusters(clusters, 100.)
    
    
    return [clusters, clustersIndx, normclusters]