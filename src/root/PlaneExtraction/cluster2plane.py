
import numpy as np
import scipy
import matcompat
from root.PlaneExtraction.princomp import princomp

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cluster2plane(cl, indx):
    np.disp(('Trwa wykonywanie: cluster2plane'))
    # Local Variables: d, cl, coeff, normal, help, l, rest, indx, planes, y, x, out, restIndx
    # Function calls: disp, princomp, false, cluster2plane, isempty, cellfun, iscell, find, cell2struct, mean
    #%% plane = cluster2plane(cl,indx)
    #if not iscell(cl):
    #    np.disp('Error: Parameter "cl" has to be a cell array')
    #    return []
    
    
    rest = np.array([])
    restIndx = np.array([])
    
    l= np.size(cl, 2) #l = cellfun('size', cl, 2.)
    out = np.nonzero(l < 3) #out = nonzero((l<3.))
    
    for x in np.nditer(out): #if not isempty(out):
        rest = cl.cell[int(out)-1]
        restIndx = indx.cell[int(out)-1]
    
    
    
    
    coeff =[princomp(x.conj().T) for x in cl] #coeff = cellfun(lambda x: princomp(x), cl, 'UniformOutput', false)
    normal =[x[:,2] for x in coeff] #normal = cellfun(lambda x: x[:,2], coeff, 'UniformOutput', false)
    
    
    #d = cellfun(lambda x, y: np.dot(x.conj().T, np.mean(y, 2.)), normal, cl, 'UniformOutput', false)
    tempx=[x.conj().T for x in normal]
    tempy=[np.mean(y, 2.) for y in cl]
    d=[tempx,tempy]
    
    
    #help = np.array(np.vstack((np.hstack((cl)), np.hstack((indx)), np.hstack((normal)), np.hstack((d)))))
    
    
    class my_planes:
        pnts = []
        indx = []
        n = []
        d = []


    planes = my_planes()
    
    
    planes.pnts=cl
    planes.indx=indx
    planes.n=normal
    planes.d=d
    
    return [planes, rest, restIndx]