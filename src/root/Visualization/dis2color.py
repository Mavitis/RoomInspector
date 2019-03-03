
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def dis2color(pnts):

    # Local Variables: maxDis, map, minDis, i, step, pos, colors, steps, pnts, dis
    # Function calls: colormap, jet, min, max, dis2color, length, zeros, repmat, find, size
    #% colors = dis2color(pnts)
    dis = pnts[2,:]
    minDis = matcompat.max(dis)
    maxDis = matcompat.max(dis)
    colors = np.zeros(3., matcompat.size(pnts, 2.))
    map = colormap(plt.jet)
    #%map = map(end:-1:1,:);
    step = matdiv(maxDis-minDis, matcompat.size(map, 1.)-1.)
    steps = np.arange(minDis, (maxDis)+(step), step)
    i = 2.
    while i<=matcompat.size(map, 1.):
        pos = nonzero(np.logical_and(dis >= steps[int((i-1.))-1], dis<steps[int(i)-1]))
        colors[:,int(pos)-1] = matcompat.repmat(map[int(i)-1,:].conj().T, 1., length(pos))
        i = i+1.
        
    return [colors]