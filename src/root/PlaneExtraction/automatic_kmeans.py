
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def automatic_kmeans(X):

    # Local Variables: CMIN, C, mindx, g3, d, cl, i, c, MIN, indx, clIndx, X, cmindx, sumd, D
    # Function calls: min, gradient, sum, kmeans, pnts2clusters, automatic_kmeans
    d = np.array([])
    indx = np.array([])
    #% for i = 1:10
    #%     [i,C,sumd,D] = kmeans(X',i);
    #%     d = [d sum(sumd)];
    #%     indx = [indx {i}];
    #% end
    [i, C, sumd, D] = kmeans(X.conj().T, 1.)
    d = np.array(np.hstack((d, np.sum(sumd))))
    indx = np.array(np.hstack((indx, cellarray(np.hstack((i))))))
    [i, C, sumd, D] = kmeans(X.conj().T, 2.)
    d = np.array(np.hstack((d, np.sum(sumd))))
    indx = np.array(np.hstack((indx, cellarray(np.hstack((i))))))
    [i, C, sumd, D] = kmeans(X.conj().T, 3.)
    d = np.array(np.hstack((d, np.sum(sumd))))
    indx = np.array(np.hstack((indx, cellarray(np.hstack((i))))))
    [i, C, sumd, D] = kmeans(X.conj().T, 4.)
    d = np.array(np.hstack((d, np.sum(sumd))))
    indx = np.array(np.hstack((indx, cellarray(np.hstack((i))))))
    g3 = np.gradient(np.gradient(np.gradient(d)))
    [MIN, mindx] = matcompat.max(g3)
    c = 5.
    while 1.:
        [i, C, sumd, D] = kmeans(X.conj().T, c)
        d = np.array(np.hstack((d, np.sum(sumd))))
        indx = np.array(np.hstack((indx, cellarray(np.hstack((i))))))
        g3 = np.gradient(np.gradient(np.gradient(d)))
        [CMIN, cmindx] = matcompat.max(g3)
        if mindx == cmindx:
            break
        
        
        mindx = cmindx
        c = c+1.
        
    [cl, clIndx] = pnts2clusters(X, indx.cell[int(mindx)-1])
    return [cl, clIndx]