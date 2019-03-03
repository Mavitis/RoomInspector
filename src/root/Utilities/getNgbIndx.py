import sys
import numpy as np
import scipy
import matcompat
from sindx2mindx import sindx2mindx
#from mindx2sindx import mindx2sindx
import numpy.matlib

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def getNgbIndx(indx, width, height, nHood, woC= True, pos=None):
    np.disp('getNgbIndx ...')
    # Local Variables: c, h1, ngb, currC, rs, h2, half, indx, ce, height, width, r, pos, accelerate, currR, cs, re, ngbIndx, nHood, woC
    # Function calls: sort, mindx2sindx, false, floor, reshape, getNgbIndx, ceil, nargin, length, repmat, true, find, sindx2mindx
    #%% ngbIndx = getNgbIndx(indx, width, height, nHood, woIndx)
    #% 
    #% Computes the sequential indices (row-wise, not column-wise as default in
    #% Matlab) of an arbitrary neighborhood
    #%
    #% If no nHood is specified the default value is 3
    #% If woC = true, then current center (specified by indx) is removed, else center
    #% is kept. The default is set to true.
    #%% some default values:
    
    #to nie jest skonwertowane
    #print(woC)
    if (pos==None):
        accelerate = 0
    else:
        accelerate = 1
    
        

    #% computing the neighboring indices:
    #print 'indx', indx
    [currR, currC] = sindx2mindx(indx, width, height)
    #print 'currR, currC', currR, currC
    half = (nHood - 1.) / 2.
    h1 = np.floor(half)
    h2 = np.ceil(half)
    #print 'h1, h2', h1, h2
    if (accelerate):
        rs = currR - h1

        if (rs < 1):
            rs = 1
            
        re = currR + h2
        if (re > height):
            re = height

        cs = currC - h1
        if (cs < 1):
            cs = 1

        ce = currC + h2
        if (ce > width):
            ce = width
        #print 'values rs , re , cs, ce', rs , re , cs, ce #do tego momentu wartosci w pliku zgodne
        
        

        temp=[]
        for it in range(int(rs)-1,int(re)):
            for it2 in range(int(cs)-1,int(ce)):
                temp.append(pos[it2][it]) #zamieniono it2 z IT tylko ze wzgledu na zamiane w z h 27.12 /ANULOWANE? /10.02 zamiana wrocone
        
        
        ngbIndx=temp
        #ngbIndx = pos[(rs,re),(cs,ce)] # chyba trzeba to zamienic na piekne fory //zrobione
        #print 'ngbIndx.size, ngbIndx', len(ngbIndx), ngbIndx # zgodne
        #ngbIndx = np.reshape(ngbIndx, (1, -1))

    #else: # nie istnieje metoda mindx...

        #r = slice((currR - h1),(currR + h2))
        #r = np.extract(np.logical_or(r < 1, r > height), r)
        #c = slice[currC - h1,currC + h2]
        #c = np.extract(np.logical_or(c < 1, c > width), c)

        #ngb = np.sort(np.vstack((numpy.matlib.repmat(r, 1, c.np.size), numpy.matlib.repmat(c, 1, c.np.size))))
        #ngbIndx = mindx2sindx(ngb[0,], ngb[1,], width, height)
        #ngbIndx = unique(ngbIndx);

    
    if (woC):
        if indx==1:
            print ngbIndx
            print 'ngbIndx'
            #sys.exit("Debug break")
    #    ngbIndx = np.extract(ngbIndx == indx, ngbIndx)
    

    return ngbIndx