
import numpy as np
import scipy
import matcompat
from scipy.signal import medfilt
from time import sleep

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def distance_adaptive_median(dis, camType):
    np.disp('distance_adaptive_median ...')

    # Local Variables: dismax, distances, dis2, dis3, dis1, u1, camType, t2, dismin, t1, u3, u2, dis
    # Function calls: medfilt2, max, min, find, distance_adaptive_median
    distances = dis
    #print len(dis),len(dis[1]), dis.size
    dis1 = medfilt(dis, np.array(np.hstack((7, 7))))
    #np.savetxt('dis1.txt', dis1, delimiter='\n', newline='\n') #sa identyczne dla obu
    dis2 = medfilt(dis, np.array(np.hstack((5, 5))))
    #np.savetxt('dis2.txt', dis2, delimiter='\n', newline='\n') #sa identyczne dla obu
    dis3 = medfilt(dis, np.array(np.hstack((3, 3))))
    #np.savetxt('dis3.txt', dis3, delimiter='\n', newline='\n') #sa identyczne dla obu
    flat_dis1=np.resize(dis1,(1,dis.size))[0]
    flat_dis2=np.resize(dis2,(1,dis.size))[0]
    flat_dis3=np.resize(dis3,(1,dis.size))[0]
    
    #% t1 = 0;
    #% t2 = 0;
    #% 
    #% if(strcmp(camType.name, 'PMD_16x64'))
    #%     t1 = 884.3;
    #%     t2 = 1768.6;
    #% elseif(strcmp(camType.name, 'PMD_120x160'))
    #%     t1 = 3000;
    #%     t2 = 6000;
    #% elseif(strcmp(camType.name, 'SR_176x144'))
    #%     t1 = 3000;
    #%     t2 = 6000;
    #% else
    #%     display('Unknown camera type.');
    #% end
    dismin = np.amin(dis)
    #print dismin
    #np.disp(dismin)
    dismax = np.amax(dis)
    #print dismax
    #np.disp(dismax)
    #% dismin = min(min(amp));
    #% dismax = max(max(amp));
    #splaszczyc distances
    t1 = dismin+(dismax-dismin)/3.
    #print t1
    t2 = dismin+2.*(dismax-dismin)/3.
    #print t2
    flat_dis=np.resize(distances,(1,dis.size))[0]
    #np.savetxt('flat_dis.txt', flat_dis, delimiter='\n', newline='\n')
    #print len(flat_dis), flat_dis.size
    u1 = np.nonzero((flat_dis<t1))[0]
    #np.savetxt('u1.txt', u1, delimiter='\n', newline='\n') #sa identyczne dla obu
    u2 = np.nonzero(np.logical_and(flat_dis >= t1, flat_dis<t2))[0]
    #np.savetxt('u2.txt', u2, delimiter='\n', newline='\n') #sa identyczne dla obu
    u3 = np.nonzero((flat_dis >= t2))[0]
    #np.savetxt('u3.txt', u3, delimiter='\n', newline='\n')#sa identyczne dla obu
    #print u1
    #% u1 = find(amp < t1);
    #% u2 = find(amp >= t1 & dis < t2);
    #% u3 = find(amp >= t2);
    flat_dis[u1] = flat_dis1[u1]
    flat_dis[u2] = flat_dis2[u2]
    flat_dis[u3] = flat_dis3[u3]
    #print len(flat_dis)
    distances =np.resize(flat_dis,(len(dis),len(dis[1]))) 
    #np.savetxt('distances_po_distadaptmed.txt', distances, delimiter='\n', newline='\n') #sa identyczne dla obu
    return distances