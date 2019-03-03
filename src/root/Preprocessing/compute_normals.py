import sys
import numpy as np
import scipy
import matcompat
from root.PlaneExtraction.local_plane_patches import local_plane_patches

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def compute_normals(fr, camType):
    np.disp('compute_normals ...')
    # Local Variables: fr, d, notplanar, planarIndx, h, camType, planar, dev, thres_dev, w, normals, notPlanarIndx, frame
    # Function calls: std, local_plane_patches, compute_normals, ismember, find, mean
    #%% frame = compute_normals(fr, camType)
    frame = fr
    w = camType.width
    h = camType.height
    #print 'frame.3dpoints', frame.points3D.size, len(frame.points3D), len(frame.points3D[0])
    [normals, d, dev] = local_plane_patches((frame.points3D), w, h, (frame.usage), 5.)

    #%% classify if points are planar or not:
    #%thres_dev = 0.67 * mean(deviation);
    #%thres_dev = 1 * mean(deviation);
    #%planarIndx = find(deviation <= 2000); %Swissranger
    #%notPlanarIndx = find(deviation > 2000); %Swissranger
    #%planarIndx = find(deviation <= 3000); %DC_Tracking
    #%notPlanarIndx = find(deviation > 3000); %DC_Tracking
    
    #print 'dev', dev 
    # nieznaczne roznice w wartosci!
    np.savetxt('dev.txt', dev, delimiter='\n', newline='\n')
    thres_dev = 1.*np.mean(dev)+np.std(dev)
    print 'thres_dev', thres_dev 
    planarIndx = np.nonzero((dev<=thres_dev))
    notPlanarIndx = np.nonzero((dev > thres_dev))
    
    
    u = np.in1d(frame.usage, planarIndx)
    u = u*1
    temp=[]
    for it in range(len(planarIndx)):
        if u[it] == 1:
            temp.append(planarIndx[it])
    
    planarIndx=temp
    np.savetxt('planarIndx=.txt', planarIndx, delimiter='\n', newline='\n')
    #Problemy - nieznacznie rozniaca sie macierz dev,-> rozniacy sie podzial na planarIndx i not planar INDX
    
    
    u1 = np.in1d(frame.usage, notPlanarIndx)
    u1 = u1*1
    temp1=[]
    for it in range(len(notPlanarIndx)):
        if u1[it] == 1:
            temp1.append(notPlanarIndx[it])
    
    notPlanarIndx=temp1
    
    
    #notPlanarIndx = notPlanarIndx[np.in1d(frame.usage, notPlanarIndx)] 
    #do weryfikacji poprawnosc
    
    
    #%% store
    frame.normals = normals
    frame.d = d
    frame.dev = dev
    frame.planar = planarIndx
    frame.notplanar = notPlanarIndx
    return frame