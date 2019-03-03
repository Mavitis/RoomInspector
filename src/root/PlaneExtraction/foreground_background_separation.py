
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def foreground_background_separation(scene):

    # Local Variables: backgr, fig, ma, iMax1, nSort, mi, scene, n, iSort, t, tPos, iMax2, z, bins, foregr
    # Function calls: sort, plot_3Dpoints, min, max, find, hist, foreground_background_separation, round
    #% [foregr, backgr] = foreground_background_separation(scene)
    #%
    #% find the two z-ranges where most of the points are lying in
    #% assumption: in the background a lot of points will have a similar z-value as
    #% well as the points in the foreground -> find threshold (somewhere between the
    #% two significant z-values) which determines if a point belongs to the
    #% foreground or to the background
    mi = matcompat.max(scene[2,:])
    ma = matcompat.max(scene[2,:])
    bins = np.round(((ma-mi)/200.))
    [n, z] = plt.hist(scene[2,:], bins)
    [nSort, iSort] = np.sort(n)
    iMax1 = iSort[int(0)-1]
    iMax2 = iSort[int((0-1.))-1]
    tPos = np.round(matdiv(np.dot(iMax1, n[int(iMax1)-1])+np.dot(iMax2, n[int(iMax2)-1]), n[int(iMax1)-1]+n[int(iMax2)-1]))
    t = z[int(tPos)-1]
    foregr = scene[0:3.,nonzero((scene[2,:]<t))]
    backgr = scene[0:3.,nonzero((scene[2,:] >= t))]
    fig = plot_3Dpoints(foregr, 'b')
    fig = plot_3Dpoints(backgr, 'r', fig)
    return [foregr, backgr]