
import numpy as np
import numpy.matlib
import scipy
import matcompat
from root.PlaneExtraction.princomp import princomp
from align_pnts2plane import align_pnts2plane
from scipy.spatial import ConvexHull

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def get_expansion(pnts, display=False):
    np.disp(('Trwa wykonywanie: get_expansion'))
    # Local Variables: m, s2max, b1, b2, pnts, s1max, s1min, fig, psort_i1, psort_i2, pnts2, pnts1, R2, i1, i2, c2, c, b, coeff, area, s2min, shape, n, r, k, display
    # Function calls: size, sort, princomp, align_pnts2plane, false, figure, get_expansion, max, plot, min, all, quiver, nargin, abs, convhull, eye, repmat, rectangle, mean
    #%% [area, shape, b1, b2, s1min, s1max, s2min, s2max] = get_expansion(pnts, display)
    
    #if nargin<2.:
    #    display = false
    
    
    #%% rotate plane so that it is parallel to xy-plane and main principle axis
    #%  are parallel to the x-/y-axis
    coeff = princomp(pnts[0:3.,:].conj().T)
    b1 = coeff[:,0]
    b2 = coeff[:,1]
    n = coeff[:,2]
    if np.all((n == np.array(np.vstack((np.hstack((0.)), np.hstack((0.)), np.hstack((1.))))))):
        pnts1 = pnts-numpy.matlib.repmat(np.mean(pnts, 2), 1, np.size(pnts, 2))
    else:
        pnts1 = align_pnts2plane(pnts, n, np.mean(pnts, 2.))
        
    
    try:
        k = ConvexHull(pnts1[0,:], pnts1[1,:]) #mozliwe ze metoda dziala inaczej
    except :
            k = np.arange(1, (np.size(pnts1, 2))+1)
    
    c = princomp(pnts1[0:2.,int(k)-1].conj().T)
    b = c[:,0]
    r = np.array(np.vstack((np.hstack((b[1], -b[0])), np.hstack((b[0], b[1])))))
    R2 = np.eye(4.)
    R2[0:2.,0:2.] = r
    pnts2 = np.dot(R2, pnts1)
    c2 = princomp(pnts2[0:2.,int(k)-1].conj().T)
    #%% compute the expansion along the principle axis -> area and shape feature
    [m, i1] = np.maximum(np.abs(c2[:,0]))
    [m, i2] = np.maximum(np.abs(c2[:,1]))
    psort_i1 = np.sort(pnts2[int(i1)-1,:])
    psort_i2 = np.sort(pnts2[int(i2)-1,:])
    s1min = np.maximum(np.abs(psort_i1[0]), np.abs(psort_i1[int(0)-1]))
    s1max = np.maximum(np.abs(psort_i1[0]), np.abs(psort_i1[int(0)-1]))
    s2min = np.maximum(np.abs(psort_i2[0]), np.abs(psort_i2[int(0)-1]))
    s2max = np.maximum(np.abs(psort_i2[0]), np.abs(psort_i2[int(0)-1]))
    area = np.dot(s1min+s1max, s2min+s2max)
    shape = np.min((s2min+s2max), (s1min+s1max)/np.maximum(s2min+s2max), (s1min+s1max))
    
    #%% show expansion
    #if display:
    #    fig = plt.figure('Position', np.array(np.hstack((1000., 1280., 900., 900.))))
    #    #%subplot(1,2,1);
    #    #%plot_3Dpoints(pnts, 'k', fig);
    #    #%subplot(1,2,2);
    #    plt.plot(pnts2[0,:], pnts2[1,:], '.')
    #    plt.axis(equal)
    #    plt.hold(on)
    #    plt.quiver(0., 0., c2[0,0], c2[1,0], (-s1max), 'Color', 'r')
    #    plt.quiver(0., 0., c2[0,1], c2[1,1], (-s2max), 'Color', 'g')
    #    #%rectangle('Position', [-s2max -s1max 2*s2max 2*s1max], 'Curvature', [1 1]);
        #%rectangle('Position', [-s2min -s1min 2*s2min 2*s1min], 'Curvature', [1 1]);
    #    rectangle('Position', np.array(np.hstack((psort_i2[0], psort_i1[0], s2min+s2max, s1min+s1max))))
    
    
    return [area, shape, b1, b2, s1min, s1max, s2min, s2max]