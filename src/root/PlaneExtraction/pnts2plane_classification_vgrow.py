
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def pnts2plane_classification_vgrow(pnts, display):

    # Local Variables: decider, rest, in, absoluteNum, pnts, ngb, planarIndx, currNormal, notPlanarIndx, fig, clusters, deviation, currIndx, r12, secondTerm, in1, in2, workingIndx, d_thresh, angles, firstTerm, allIndx, currColor, a_thresh, currSet, j, thres_dev, planes, display, OP
    # Function calls: plot_3Dpoints, ismember, unique, false, abs, generate_oriented_particles, max, nargin, progressbar, pnts2plane_classification_vgrow, show_clusters, ones, isempty, intersect, zeros, acos, pi, find, size
    #%% [planes, rest] = pnts2plane_classification_rgrow(pnts, display)
    #%
    #%   The function is based on the paper "Geometry and Texture Recovery" 
    #%   of Stamos and Allen clustering arbitrary point clouds. 
    #%   Use of region growing techniques.
    #%
    #% pnts: set of points with the following structure
    #%           | p1x p2x p3x p4x     |
    #%    pnts = | p1y p2y p3y p4y ... |
    #%           | p1z p2z p3z p4z     |
    #% display: 1 - visualize clusters; 0 - no visualization (optional; default: 0)
    #%% some default values:
    if nargin<2.:
        display = false
    
    
    rest = np.array([])
    #%% generate oriented particels:
    #% [VoxelPoints, voxelWithPoint, VoxelColors, n, nbrVoxel, startingPoint] = ...
    #%     generate_voxels(pnts, [20 20 20], 'r');
    #% 
    #% OrientedParticles = calc_plane(voxelWithPoint, VoxelPoints, VoxelColors, n, ...
    #%     nbrVoxel, [20 20 20], startingPoint, 'Ransac');
    OP = generate_oriented_particles(pnts)
    #%% merging:
    #%[patchesNew, patches, rest] = cluster_merging(OrientedParticles,'Stamos');
    #% classify if points are planar or not:
    deviation = np.array(np.hstack((OP.dev)))
    #%thres_dev = 0.67 * mean(deviation);
    thres_dev = 15.
    planarIndx = nonzero((deviation<=thres_dev))
    #%Swissranger
    notPlanarIndx = nonzero((deviation > thres_dev))
    #%Swissranger
    rest = np.array(np.hstack((rest, np.array(np.hstack((OP[int(notPlanarIndx)-1].center))))))
    allIndx = planarIndx
    #%allPatches = OrientedParticles;
    #%patchesNew = [];
    clusters = cellarray([])
    absoluteNum = matcompat.size(allIndx, 2.)
    #% region growing:
    while not isempty(allIndx):
        progressbar((1.-matdiv(matcompat.size(allIndx, 2.), absoluteNum)))
        currSet = np.array([])
        currNormal = np.array([])
        currColor = np.array([])
        workingIndx = allIndx[0]
        allIndx[0] = np.array([])
        while not isempty(workingIndx):
            currIndx = workingIndx[0]
            currSet = np.array(np.hstack((currSet, OP[int(currIndx)-1].center)))
            #%currNormal = [currNormal currPatch.normal];http://www.spiegel.de/politik/ausland/0,1518,543512,00.html
            #%currColor = [currColor currPatch.color];
            #%workingPatches(randnumberworking) = [];
            workingIndx[0] = np.array([])
            if isempty(allIndx):
                continue
            
            
            #% for redundant point elimination:
            #% a_thresh = 1/18* pi;
            #% d_thresh = 2;
            #% for plane estalishing on arbitrary point clouds
            a_thresh = np.dot(3./18., np.pi)
            d_thresh = 120.
            #%Swissranger
            ngb = intersect(allIndx, (OP[int(currIndx)-1].ngb))
            if isempty(ngb):
                continue
            
            
            #% conormality measure:
            angles = acos(np.dot(OP[int(currIndx)-1].normal.conj().T, np.array(np.hstack((OP[int(ngb)-1].normal)))))
            #% find patches, which fulfill constraints:
            in1 = nonzero((angles<a_thresh))
            if isempty(in1):
                #% patchesNew = [patchesNew currPatch];
            continue
            
            ngb = ngb[int(in1)-1]
            #% coplanarity measure:        
            r12 = np.array(np.hstack((OP[int(ngb)-1].center)))-np.dot(OP[int(currIndx)-1].center, np.ones(1., matcompat.size(ngb, 2.)))
            firstTerm = np.abs(np.dot(OP[int(currIndx)-1].normal.conj().T, r12))
            secondTerm = np.zeros(1., matcompat.size(r12, 2.))
            for j in np.arange(1., (matcompat.size(r12, 2.))+1):
                secondTerm[int(j)-1] = np.abs(np.dot(OP[int(ngb[int(j)-1])-1].normal.conj().T, r12[:,int(j)-1]))
                
            decider = matcompat.max(np.array(np.vstack((np.hstack((firstTerm)), np.hstack((secondTerm))))))
            in2 = nonzero((decider<d_thresh))
            if isempty(in2):
                #% patchesNew = [patchesNew currPatch];
            continue
            
            in = ngb[int(in2)-1]
            workingIndx = np.array(np.hstack((workingIndx, in)))
            workingIndx = np.unique(workingIndx)
            allIndx[int(ismember[int(allIndx)-1,int(in)-1])-1] = np.array([])
            
        clusters = np.array(np.hstack((clusters, cellarray(np.hstack((currSet))))))
        #%patch.center = mean(currSet,2);
        #%patch.color = mean(currColor,2);
        #%coeff = princomp(currSet');
        #%patch.normal = coeff(:,3);
        #%patch.normal = mean(currNormal,2);
        #% radius = max(sqrt(sum((currSet-repmat(currPatch.center,1,size(currSet,2))).^2)));
        #%d = patch.normal' * center;
        #%patch.center = center - ((patch.normal'*center)-d)*patch.normal;
        #%radius = max(sqrt(sum((currSet-repmat(patch.center,1,size(currSet,2))).^2)));
        #%if radius < currPatch.radius
        #%    patch.radius = currPatch.radius;
        #%else
        #%    patch.radius = radius;
        #%end
        #%patchesNew = [patchesNew patch];
        
    progressbar(1.)
    #%% display results:
    if display:
        fig = show_clusters(clusters, 25.)
        fig = plot_3Dpoints(rest, 'k', fig)
    
    
    planes = clusters
    return [planes, rest]