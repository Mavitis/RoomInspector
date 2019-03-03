import sys
import numpy as np
import scipy
import matcompat
from root.Utilities.getNgbIndx import getNgbIndx
from root.PlaneExtraction.princomp import princomp

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def local_plane_patches(pnts, width, height, usage, neighborhood, woCenter=False):
    np.disp('local_plane_patches ...')
    # Local Variables: neighborhood, pos, height, meanPnt, pnts, roots, ngbIndx, width, score, vec, usage, deviation, currIndx, ngbPnts, d, i, woCenter, coeff, l, normals, y, x, z
    # Function calls: princomp, false, local_plane_patches, reshape, sum, getNgbIndx, nargin, length, abs, zeros, ismember, mean
    #%% [normals, deviation] = local_plane_patches(pnts, width, height, usage, neighborhood, woCenter)
    #% 
    #% compute for each point its normal using a certain neighborhood of points
    #%% initialize same values:

    #print 'pnts', pnts.size, len(pnts), len(pnts[0])
    
    deviation = np.zeros((1, height* width))
    d = np.zeros((1, height* width))
    deviation=deviation[0]
    d=d[0]   
    
    pos = np.arange(1, (len(pnts[0])+1))
    #np.savetxt('pos.txt', pos, delimiter='\n', newline='\n')
    
    #print 'pos', len (pos),
    # pos w matlabie ma 144 x 176... przed resize 1 x 25344 
    #pos to zmienna o wymaireze 1x 25344 z wartosciami od 1 do 25344. 
    pos = np.reshape(pos, (height,width)).conj().T #zmiana 27.12 zamiana width z heinght
    x = np.zeros((1, height * width))
    y = np.zeros((1, height * width))
    z = np.zeros((1, height * width))
    x=x[0]
    y=y[0]
    z=z[0]  
    #%% normal computation:
    #% Compute for each point its normal based on points of any surrounding
    #% neighborhood 
    #usage jest blednie liczone! wrocic wyzej
    i = 1
    #print 'lenusage', len(usage[0]), usage[0]
    while i<len(usage):
        currIndx = usage[int(i)]#tu musi byc od normalnego i
        #print 'currIndx', currIndx
        #sys.exit("Error message")
        #print 'usage', usage.size, usage
        #print 'currINDX', currIndx.size, currIndx
        ngbIndx = getNgbIndx(currIndx, width, height, neighborhood, woCenter, pos) #zmiana 27.12 zamiana width z heinght
        #print 'ngbIndx',ngbIndx, 'size', ngbIndx.size, 'len',  len(ngbIndx)
        #print 'ngbIndx',ngbIndx, 'size', ngbIndx.size, 'len',  len(ngbIndx)
        #np.savetxt('usage.txt', usage, delimiter='\n', newline='\n')
        u = np.in1d(ngbIndx, usage)
        u = u*1
        #print 'u',u
        #print u
        #print len(u)
        #print len(frame.usage[1])
        temp=[]
        for it in range(len(ngbIndx)):
            if u[it] == 1:
                temp.append(ngbIndx[it])
        
        ngbIndx=temp
        
        
        
        #ngbIndx = ngbIndx[np.in1d(ngbIndx, usage)]
        #print 'ngbIndx',ngbIndx
        
        #print 'ngbIndx', ngbIndx.size, len(ngbIndx), ngbIndx
        l = len(ngbIndx)
        #print 'l', l
        #porownac pnts po kolejnych wierszach/kolumnach
        temp=np.zeros((3, len(ngbIndx)))
        #print 'pnts', len(pnts), pnts.size
        #np.savetxt('pnts[0].txt', pnts[0], delimiter='\n', newline='\n')
        for it in range(0,3):
            for it2 in range(len(ngbIndx)):
                temp[it][it2]=pnts[it][ngbIndx[it2]-1]
                #temp.append(pnts[it][ngbIndx[it2]])
        
        ngbPnts=temp
        
        
        #print 'ngbPnts', len(ngbPnts), ngbPnts
        
        meanPnt = (np.sum(ngbPnts, axis=1)/l)
        #print 'meanPnt', meanPnt
        #Do tego momentu zgodnosc wartosci, mozliwe ze mean pt jest w poziomie zamiast w pionie
        
        
        
        #%ngbPnts = [ngbPnts(1,:) - meanPnt(1); ngbPnts(2,:) - meanPnt(2); ...
        #%    ngbPnts(3,:) - meanPnt(3)];
        #%cov = ngbPnts * ngbPnts';
        #%[vec, val] = eig(cov);
        #%[mi, in] = min([val(1,1) val(2,2) val(3,3)]);
        #%x(currIndx) = vec(1, in);
        #%y(currIndx) = vec(2, in);
        #%z(currIndx) = vec(3, in);
        #%deviation(currIndx) = mi; 
        #%d(currIndx) = vec(:, in)' * meanPnt;
        #% slower in computation -> question: better results? no?!
        [coeff, score, roots] = princomp(ngbPnts.conj().T)
        #print 'coeff', coeff #  zamieniona druga z trzecia kolumna 
        #print 'score', score  #[2,:] #w drugim musze sie odwolac do 2,: zeby bylo ok, jakies cujowe sortowanie
   
        
        
        
        vec = coeff[:,1] 
        #print 'vec', vec

        #print x.size 
        x[int(currIndx)-1] = vec[0] #zgodna wartosc
        #print 'x', x[int(currIndx)-1] 
        y[int(currIndx)-1] = vec[1] #zgodna wartosc
        #print 'y', y[int(currIndx)-1]
        z[int(currIndx)-1] = vec[2] #zgodna wartosc
        #print 'z', z[int(currIndx)-1]
        #print 'deviation', deviation
        
        deviation[int(currIndx)-1]=np.mean(np.abs(score[0,:])) # matlab sortuje SCORE, TA METODA NIE
        for w in range(0, 3):
            temp2=np.mean(np.abs(score[w,:]))
            if temp2 < deviation[int(currIndx)-1]:
                deviation[int(currIndx)-1]=temp2
            
        #deviation[int(currIndx)-1] = np.mean(np.abs(score[2,:])) #zgodna wartosc
        #print 'deviation[int(currIndx)-1]', deviation[int(currIndx)-1] # 
        #sys.exit("Debug break") #- do tego miejsca dociera kod! 
        d[int(currIndx)-1] = np.dot(vec.conj().T, meanPnt)
        i = i+1.
        
            
        
        

    normals = np.array(np.vstack((np.hstack((x)), np.hstack((y)), np.hstack((z)))))
    
    return [normals, d, deviation]