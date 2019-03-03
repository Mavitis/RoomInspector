
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def projection(fr, camType):

    # Local Variables: distances, fr, tScale, zLocal, i, camType, dLocal, yLocal, xLocal, Y, X, Z, frame
    # Function calls: reshape, zeros, projection, sqrt
    #%frame = projection(fr, camType)
    frame = fr
    X = fr.points3D[0,:]
    Y = fr.points3D[1,:]
    Z = fr.points3D[2,:]
    xLocal = np.zeros(((camType.height), (camType.width)))
    yLocal = np.zeros(((camType.height), (camType.width)))
    zLocal = np.zeros(((camType.height), (camType.width)))
    zLocal [0:np.dot(camType.height, camType.width)] = camType.focalLength
    #zLocal= camType.focalLength #change here from   zLocal [0:np.dot(camType.height, camType.width)] = camType.focalLength need verification
    
    dLocal = np.zeros(np.dot(camType.height, camType.width))
    tScale = np.zeros(np.dot(camType.height, camType.width))
    i = 2.
    while i<=camType.width:
        xLocal[:,int(i)-1] = i-1.
        i = i+1.
        
    i = 2.
    while i<=camType.height:
        yLocal[int(i)-1,:] = i-1.
        i = i+1.
         
    xLocal = np.reshape(xLocal, (1, np.dot(camType.width, camType.height)))
    yLocal = np.reshape(yLocal, (1, np.dot(camType.width, camType.height)))
    zLocal = np.reshape(zLocal, (1, np.dot(camType.width, camType.height)))
    xLocal = xLocal-camType.principalPoint[0]
    xLocal = np.dot(camType.pixelWidth, xLocal)
    yLocal = yLocal-camType.principalPoint[1]
    yLocal = np.dot(np.dot(-1., camType.pixelHeight), yLocal)
    dLocal = np.sqrt((xLocal**2.+yLocal**2.+zLocal**2.))
    #np.savetxt('dLocal.txt', dLocal[0],delimiter='\n', newline='\n')
    tScale = fr.points3D_org[2,:]/zLocal
    #np.savetxt('tScale.txt', tScale[0], delimiter='\n', newline='\n')
    frame.distances = dLocal[0]*tScale[0]
    #np.savetxt('frame.distances_from_projection.txt', frame.distances, delimiter='\n', newline='\n')
    #print frame.distances
    return frame