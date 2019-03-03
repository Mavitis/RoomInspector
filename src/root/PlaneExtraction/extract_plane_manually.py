
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def extract_plane_manually(pnts):

    # Local Variables: normal, pntsIndx, initPlane, pInfo, i, coeff, initIndx, indx, d, dcm_obj, center, plane, fig, w, score, pnts, points
    # Function calls: disp, plot_3Dpoints, princomp, set, datacursormode, figure, getCursorInfo, extract_plane_manually, close, mean, input, waitforbuttonpress, size
    pntsIndx = np.array(np.hstack((np.arange(1., (matcompat.size(pnts, 2.))+1))))
    fig = plt.figure
    fig = plot_3Dpoints(pnts, 'k', fig, 0.3)
    dcm_obj = datacursormode(fig)
    np.disp('Select 4 points determing the corners of the plane.')
    input('Press enter if ready.')
    initIndx = np.array([])
    i = 1.
    while i<=4.:
        set(dcm_obj, 'Enable', 'on')
        plt.figure(fig)
        w = waitforbuttonpress
        pInfo = getCursorInfo(dcm_obj)
        initIndx = np.array(np.hstack((initIndx, pInfo.DataIndex)))
        fig = plot_3Dpoints(pnts[0:3.,int((pInfo.DataIndex))-1], 'r', fig)
        i = i+1.
        
    initPlane.points = pnts[0:3.,int(initIndx)-1]
    initPlane.indx = initIndx
    [coeff, score] = princomp(initPlane.points.conj().T)
    initPlane.normal = coeff[:,2]
    initPlane.d = np.dot(initPlane.normal.conj().T, np.mean((initPlane.points), 2.))
    initPlane.points = initPlane.points-np.dot(initPlane.normal, score[:,2].conj().T)
    initPlane.center = np.mean((initPlane.points), 2.)
    plane = initPlane
    plt.close(fig)
    #%initPlane.radius = max(sqrt(sum( ...
    #%    (initPlane.points - repmat(initPlane.center,1,size(initPlane.points,2))).^2)));
    #%indx = compute_pntsINrect(pnts, initPlane);
    #%
    #%clf(fig);
    #%fig = plot_3Dpoints(pnts(1:3,:), 'k', fig, 0.3);
    #%fig = plot_3Dpoints(pnts(1:3,indx), 'y', fig);
    #% dev = initPlane.normal'*pnts - initPlane.d;
    #% projPnts = pnts - initPlane.normal * dev;
    #%
    #% dis = sqrt(sum((projPnts - repmat(initPlane.center, 1, size(projPnts,2))).^2));
    #% 
    #% planeIndx = find(dis <= initPlane.radius & abs(dev) < 100);
    #% restIndx = pntsIndx;
    #% restIndx(planeIndx) = [];
    #% 
    #% clf(fig);
    #% fig = plot_3Dpoints(pnts(:,restIndx), 'k', fig, 0.3);
    #% fig = plot_3Dpoints(pnts(:, planeIndx), 'y', fig);
    #% 
    #% disp('Click on all points which should be removed.');
    #% disp('If you are ready enter press a key!');
    #% 
    #% rmvIndx = [];
    #% while(1)
    #%     
    #%     set(dcm_obj, 'Enable', 'on');
    #%     figure(fig);
    #%     
    #%     w = waitforbuttonpress;
    #%     
    #%     if(w) break; end
    #%     
    #%     pInfo = getCursorInfo(dcm_obj);
    #%     
    #%     rmvIndx = [rmvIndx pInfo.DataIndex];
    #%     fig = plot_3Dpoints(pnts(:,pInfo.DataIndex), 'c', fig);
    #%     
    #% end
    #% 
    #% rmvIndx
    return [plane]