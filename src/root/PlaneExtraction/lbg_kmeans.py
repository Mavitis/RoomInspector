
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def lbg_kmeans(pnts):

    # Local Variables: clhelp, clI, cl, todopnts, clIndx, chelp, pnts, fig, v, ihelp, shelp
    # Function calls: lbg_kmeans, plot_3Dpoints, kmeans, pnts2clusters, isempty, show_clusters
    cl = np.array([])
    clIndx = np.array([])
    [ihelp, chelp, v] = kmeans(pnts.conj().T, 1., 'emptyaction', 'drop')
    todopnts = cellarray(np.hstack((pnts)))
    while not isempty(todopnts):
        pnts = todopnts.cell[0]
        todopnts[0] = np.array([])
        [ihelp, chelp, shelp] = kmeans(pnts.conj().T, 2., 'emptyaction', 'drop')
        [clhelp, clI] = pnts2clusters(pnts, ihelp)
        shelp
        matdiv(shelp, v)
        if matdiv(shelp[0], v)<0.05:
            cl = np.array(np.hstack((cl, clhelp[0])))
            clIndx = np.array(np.hstack((clIndx, clI[0])))
        else:
            todopnts = np.array(np.hstack((todopnts, clhelp[0])))
            
        
        if matdiv(shelp[1], v)<0.05:
            cl = np.array(np.hstack((cl, clhelp[1])))
            clIndx = np.array(np.hstack((clIndx, clI[1])))
        else:
            todopnts = np.array(np.hstack((todopnts, clhelp[1])))
            
        
        #%if(~isempty(cl))
        #%    fig = show_clusters(cl);
        #%    plot_3Dpoints([todopnts{1:end}], 'k', fig);
        #%end
        
    fig = show_clusters(cl)
    plot_3Dpoints(np.array(np.hstack((todopnts.cell[0:]))), 'k', fig)
    return [cl, clIndx]