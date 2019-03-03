
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def pnts2plane_classification_dac(pnts, display):

    # Local Variables: help, voxels_new, pos, in, pnts, patches, a_thresh, clusters, currIndx, in1, in2, workingIndx, d_thresh, angles, voxels, d, allIndx, center, currSet, i, coeff, n, planes, y, x, display, dis
    # Function calls: princomp, pi, false, main_plane_extraction, show_clusters, generate_voxels, nargin, length, abs, pnts2plane_classification_dac, intersect, cellfun, isempty, acos, repmat, find, cell2struct, mean
    #%% planes = pnts2plane_classification_dac(pnts)
    #%
    #% reference:
    #% Jan Weingarten et al: " A Fast and Robust 3D Feature Extraction Algorithm
    #%                         for Structured Environment Reconstuction"
    #%% some defaults:
    if nargin<2.:
        display = false
    
    
    #%% discretization of the point cloud
    voxels = generate_voxels(pnts, np.array(np.hstack((60., 60., 60.))))
    #%% segmentation
    pos = cellfun(lambda x: main_plane_extraction(x[0:3.,:]), voxels, 'UniformOutput', false)
    voxels_new = cellfun(lambda x, i: x[:,int(i)-1], voxels, pos, 'UniformOutput', false)
    voxels_new = voxels_new[int((not cellfun('isempty', voxels_new)))-1]
    #%[n, d] = cellfun(@(x)(least_square_plane_fitting(x)), voxels_new, 'UniformOutput', false);
    coeff = cellfun(lambda x: princomp(x[0:3.,:].conj().T), voxels_new, 'UniformOutput', false)
    n = cellfun(lambda x: x[:,2], coeff, 'UniformOutput', false)
    center = cellfun(lambda x: np.mean(x[0:3.,:], 2.), voxels_new, 'UniformOutput', false)
    d = cellfun(lambda x, y: np.dot(x.conj().T, y), n, center, 'UniformOutput', false)
    help = np.array(np.vstack((np.hstack((n.conj().T)), np.hstack((d.conj().T)), np.hstack((center.conj().T)), np.hstack((voxels_new.conj().T)), np.hstack((matcompat.repmat(cellarray(np.hstack((np.array(np.hstack((1., 0., 0.)))))), 1., length(d)))), np.hstack((matcompat.repmat(cellarray(np.hstack((30.))), 1., length(d)))))))
    patches = cell2struct(help, cellarray(np.hstack(('normal', 'd', 'center', 'pnts', 'color', 'radius'))), 1.).conj().T
    #%help = [n'; d'; voxels_new'];
    #%planes = cell2struct(help, {'n', 'd', 'pnts'}, 1)';
    #%
    #%planes = smooth_planes(planes);
    #%% region growing:
    a_thresh = np.dot(1./18., np.pi)
    #%d_thresh = 70; 
    allIndx = np.array(np.hstack((np.arange(1., (length(patches))+1))))
    clusters = np.array([])
    while not isempty(allIndx):
        currSet = np.array([])
        workingIndx = allIndx[0]
        allIndx[0] = np.array([])
        while not isempty(workingIndx):
            currIndx = workingIndx[0]
            currSet = np.array(np.hstack((currSet, patches[int(currIndx)-1].pnts)))
            workingIndx[0] = np.array([])
            d_thresh = np.dot(4.*0.05, np.mean((patches[int(currIndx)-1].pnts[2,:]), 2.))
            if isempty(allIndx):
                continue
            
            
            angles = acos(np.dot(patches[int(currIndx)-1].normal.conj().T, np.array(np.hstack((patches[int(allIndx)-1].normal)))))
            in1 = nonzero((angles<a_thresh))
            dis = np.abs((np.dot(patches[int(currIndx)-1].normal.conj().T, np.array(np.hstack((patches[int(allIndx)-1].center))))-matcompat.repmat(np.dot(patches[int(currIndx)-1].normal.conj().T, patches[int(currIndx)-1].center), 1., length(allIndx))))
            in2 = nonzero((dis<d_thresh))
            #%          % coplanarity measure:
            #%         currPnt = patches(currIndx).center;
            #%         currNormal = patches(currIndx).normal;
            #%         ngbPnts = [patches(allIndx).center];
            #%         ngbNormals = [patches(allIndx).normal];
            #%         
            #%         r12 = ngbPnts - currPnt * ones(1, size(ngbPnts, 2));
            #%         
            #%         firstTerm = abs(currNormal'*r12);
            #%         secondTerm = zeros(1, size(r12, 2));
            #%         for j = 1:size(r12, 2)
            #%             secondTerm(j) = abs(ngbNormals(:,j)'*r12(:,j));
            #%         end
            #%         
            #%         decider = max([firstTerm; secondTerm]);
            #%         
            #%         in2 = find(decider < d_thresh);
            in = intersect(in1, in2)
            workingIndx = np.array(np.hstack((workingIndx, allIndx[int(in)-1])))
            allIndx[int(in)-1] = np.array([])
            
        clusters = np.array(np.hstack((clusters, cellarray(np.hstack((currSet))))))
        
    planes = clusters
    #%% display results:
    if display:
        show_clusters(clusters, 25.)
    
    
    return [planes]