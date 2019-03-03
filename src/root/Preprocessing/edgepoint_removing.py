import sys
import numpy as np
import scipy
import matcompat
from skimage import feature
from skimage.morphology import square
from skimage.morphology import dilation
from numpy import sqrt
from time import sleep
#import matplotlib.pyplot as plt

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def edgepoint_removing(fr, camType):
    np.disp('edgepoint_removing ...')
    # Local Variables: use, camType, fr, bw, u, usage, frame, se
    # Function calls: edgepoint_removing, strel, reshape, imdilate, edge, ismember, find
    frame = fr

    
    #test=(np.reshape(fr.distances, (camType.height, camType.width))).conj().T
    #np.savetxt('test.txt', test, delimiter='\n', newline='\n')
    #usunieta transpozycja, niekoniecznie dobra dla wyniku .conj().T
    dismax = np.amax(fr.distances)
    #print dismax
    bw = feature.canny((np.reshape(fr.distances, (camType.height, camType.width))).conj().T, sigma=np.sqrt(2),low_threshold=0.01*dismax, high_threshold=0.058*dismax)
    #np.savetxt('bw.txt', bw, delimiter='\n', newline='\n')
    #TYMCZASOWY IMPORT DLA DEBUGA!
    bw = np.loadtxt('IC.txt',dtype=float,comments='%',delimiter='\n') #TYMCZASOWY IMPORT DLA DEBUGA!
    bw=np.reshape(bw, (camType.width, camType.height)) #TYMCZASOWY IMPORT DLA DEBUGA!
    #np.savetxt('bwimport.txt', bw, delimiter='\n', newline='\n')
    
    bw = dilation(bw, square(3))
    #bw=bw.conj().T
    #plt.imshow(bw)
    #plt.show()
    bw = np.reshape(bw.conj().T,(1,camType.height*camType.width))
    use = np.nonzero((bw == 0))
    #np.savetxt('fr.usage[1].txt', fr.usage[1], delimiter='\n', newline='\n') ZGODNE
    #np.savetxt('use[1].txt', use[1], delimiter='\n', newline='\n')

  
    
    u = np.in1d(fr.usage[1], use[1])
    u = u*1
    #print u
    #print len(u)
    #print len(frame.usage[1])
    temp=[]
    for it in range(len(frame.usage[1])):
        if u[it] == 1:
            temp.append(frame.usage[1][it])
    
    frame.usage=temp
    #np.savetxt('frame.usageafter.txt', frame.usage, delimiter='\n', newline='\n')
    
    return frame
    #BRAK PELNEJ ZGODNOSCI DZIALANIA CANNEGO. POWODUJE ZMIANY DALEJ
