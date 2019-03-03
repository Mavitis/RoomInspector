
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def generate_colormap(nColor):

    # Local Variables: map, mapEntry, i, nColor, rest, step, nPerSlot
    # Function calls: zeros, mod, generate_colormap, find, floor
    #% map = generate_colormap(nColor)
    map = np.zeros(nColor, 3.)
    map[0,:] = np.array(np.hstack((0., 0., 0.5)))
    nPerSlot = np.floor(((nColor-1.)/5.))
    rest = np.mod((nColor-1.), 5.)
    mapEntry = 2.
    #%+z:
    step = 0.5 / nPerSlot
    i = 1.
    while i<=nPerSlot:
        map[int(mapEntry)-1,:] = map[int((mapEntry-1.))-1,:]+np.array(np.hstack((0., 0., step)))
        i = i+1.
        mapEntry = mapEntry+1.
        
    #%+y:
    step = 1./nPerSlot
    i = 1.
    while i<=nPerSlot:
        map[int(mapEntry)-1,:] = map[int((mapEntry-1.))-1,:]+np.array(np.hstack((0., step, 0.)))
        i = i+1.
        mapEntry = mapEntry+1.
        
    #%+x-z:
    step = 1./(nPerSlot+rest)
    i = 1.
    while i<=nPerSlot+rest:
        map[int(mapEntry)-1,:] = map[int((mapEntry-1.))-1,:]+np.array(np.hstack((step, 0., -step)))
        i = i+1.
        mapEntry = mapEntry+1.
        
    #%-y:
    step = 1./nPerSlot
    i = 1.
    while i<=nPerSlot:
        map[int(mapEntry)-1,:] = map[int((mapEntry-1.))-1,:]-np.array(np.hstack((0., step, 0.)))
        i = i+1.
        mapEntry = mapEntry+1.
        
    #%-x:
    step = 0.5/ nPerSlot
    i = 1.
    while i<=nPerSlot:
        map[int(mapEntry)-1,:] = map[int((mapEntry-1.))-1,:]-np.array(np.hstack((step, 0., 0.)))
        i = i+1.
        mapEntry = mapEntry+1.
        
    map[np.nonzero[map > 1]-1] = 1
    map[np.nonzero[map<0]-1] = 0
    return map