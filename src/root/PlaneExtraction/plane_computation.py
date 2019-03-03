
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def plane_computation(pnts):

    # Local Variables: p2, p3, p1, d, coeff, n, b, a, pnts
    # Function calls: disp, princomp, plane_computation, cross, mean, norm, size
    #% [n, d] = plane_computation(pnts)
    #% 
    #% n: normal vector of E
    #%        -  -
    #%        |n1|
    #%    n = |n2|
    #%        |n3|
    #%        -  -
    #% d: distanz of E to the origin
    #% p1, p2, p3: points in E (if #pnts = 3)
    #%         -   -       -   -       -   -
    #%         |p11|       |p21|       |p31|
    #%    p1 = |p12|  p2 = |p22|  p3 = |p32|
    #%         |p13|       |p23|       |p33|
    #%         -   -       -   -       -   -
    #% 
    #% the plane is described in Hesse normal form:
    #%    ->  ->           ->
    #% E: n * x = d, where n is the normal vector of E
    pnts = pnts[0:3.,:]
    n = np.array([])
    d = 0.
    if matcompat.size(pnts, 2.)<3.:
        np.disp('Error: not enough pnts for plane computation')
        return []
    elif matcompat.size(pnts, 2.) == 3.:
        p1 = pnts[:,0]
        p2 = pnts[:,1]
        p3 = pnts[:,2]
        a = p2-p1
        b = p3-p1
        n = np.cross(a, b)
        n = matdiv(n, linalg.norm(n))
        d = np.dot(n.conj().T, p1)
        
    else:
        coeff = princomp(pnts.conj().T)
        n = coeff[:,2]
        d = np.dot(n.conj().T, np.mean(pnts, 2.))
        
    
    return [n, d]