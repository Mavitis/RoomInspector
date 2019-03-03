
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cluster_through_histNormals(fr, cam, display):

    # Local Variables: n_x, n_y, seq, angle_z, camType, angle_x, frames, n_z, planarIndx, clusterIndx, usage, clusters, u_y, u_x, angle_y, deviation, fr, u_xyz, edges, u_xy, u_z, Y, X, Z, i, XYZ, bin_z, thres_dev, cam, x, display, bin_y, bin_x
    # Function calls: std, asin, false, abs, isfield, pnts2clusters, sqrt, show_clusters, nargin, length, preprocessing, intersect, cellfun, histc, pi, find, cluster_through_histNormals, mean
    #%% [clusters, clusterIndx] = cluster_through_histNormals(fr, cam, display)
    #%% some defaults:
    if nargin<3.:
        display = false
    
    
    if not isfield(fr, 'normals'):
        seq.frames = fr
        seq.camType = cam
        seq = preprocessing(seq, 'normals')
        fr = seq.frames
    
    
    deviation = fr.dev
    thres_dev = 1.*np.mean(deviation)+np.std(deviation)
    planarIndx = nonzero((deviation<=thres_dev))
    fr.usage = intersect((fr.usage), planarIndx)
    #%plot_3Dpoints(fr.points3D(:, fr.usage)); drawnow;
    #%% compute angles along the three axis X, Y, Z:
    X = fr.normals[0,int((fr.usage))-1]
    Y = fr.normals[1,int((fr.usage))-1]
    Z = fr.normals[2,int((fr.usage))-1]
    XYZ = np.sqrt((X**2.+Y**2.+Z**2.))
    angle_x = np.abs(asin((X/XYZ)))
    angle_y = np.abs(asin((Y/XYZ)))
    angle_z = np.abs(asin((Z/XYZ)))
    #%angle = max([angle_x; angle_y; angle_z]);
    #%% compute histograms over these angles:
    edges = np.array(np.hstack((np.arange(0., (np.pi/2.-matdiv(np.pi, 4.5))+(matdiv(np.pi, 4.5)), matdiv(np.pi, 4.5)))))
    [n_x, bin_x] = histc(angle_x, edges)
    [n_y, bin_y] = histc(angle_y, edges)
    [n_z, bin_z] = histc(angle_z, edges)
    #%[n, bin] = histc(angle, [min(angle):(max(angle)-min(angle))/10:max(angle)]);
    #%bar(n);
    u_x = pnts2clusters((fr.usage), bin_x)
    u_y = pnts2clusters((fr.usage), bin_y)
    u_z = pnts2clusters((fr.usage), bin_z)
    #%u = pnts2clusters(fr.usage, bin);
    #%% compute clusters of points, which fall in the same bins of the three
    #%  histograms.
    u_xy = np.array([])
    i = 1.
    while i<=length(u_x):
        u_xy = np.array(np.hstack((u_xy, cellfun(lambda x: intersect(u_x.cell[int(i)-1], x), u_y, 'UniformOutput', false))))
        i = i+1.
        
    u_xy[int(cellfun[int('isempty')-1,int(u_xy)-1])-1] = np.array([])
    u_xyz = np.array([])
    i = 1.
    while i<=length(u_xy):
        u_xyz = np.array(np.hstack((u_xyz, cellfun(lambda x: intersect(u_xy.cell[int(i)-1], x), u_z, 'UniformOutput', false))))
        i = i+1.
        
    u_xyz[int(cellfun[int('isempty')-1,int(u_xyz)-1])-1] = np.array([])
    clusterIndx = u_xyz
    #%clusterIndx = u;
    clusters = cellfun(lambda x: fr.points3D[0:3.,int(x)-1], clusterIndx, 'UniformOutput', false)
    if display:
        show_clusters(clusters, 0., np.array([]), np.array([]), 1.)
    
    
    return [clusters, clusterIndx]