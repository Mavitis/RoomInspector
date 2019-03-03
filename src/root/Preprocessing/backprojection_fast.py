
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def backprojection_fast(fr, camType):
    np.disp('backprojection_fast ...')
    # Local Variables: fr, tScale, y, points3D_org, i, camType, dLocal, zLocal, xLocal, yLocal, x, z, points3D, frame
    # Function calls: zeros, ones, backprojection_fast, sqrt, reshape
    #%frame = backprojection_fast(fr, camType)
    frame = fr
    xLocal = np.zeros(((camType.width), (camType.height)))#zgodne
    
    yLocal = np.zeros(((camType.width), (camType.height)))#zgodne
    
    zLocal = np.ones(((1,(camType.height * camType.width))))*camType.focalLength#zgodne
    
    #print len(xLocal), len(yLocal), len(zLocal)
    #print camType.focalLength
    #print zLocal
 
    #zLocal[int(np.arange(camType.height*camType.width))] = camType.focalLength
    dLocal = np.zeros(1, np.dot(camType.height, camType.width))
    tScale = np.zeros(1, np.dot(camType.height, camType.width))
    i = 2
    while i<=camType.width:
        xLocal[int(i)-1,:] = i-1.
        i = i+1.
        
    i = 2
    #np.savetxt('xLocal.txt', xLocal, delimiter='\n', newline='\n')#zgodne
    while i<=camType.height:
        yLocal[:,int(i)-1] = i-1.
        i = i+1.
    #np.savetxt('yLocal.txt', yLocal, delimiter='\n', newline='\n')  #zgodne 
    xLocal = np.reshape(xLocal.conj().T, (1, np.dot(camType.width, camType.height)))
    #np.savetxt('xLocal_res.txt', xLocal, delimiter='\n', newline='\n') #zgodne 
    yLocal = np.reshape(yLocal.conj().T, (1, np.dot(camType.width, camType.height)))
    #np.savetxt('yLocal_res.txt', yLocal, delimiter='\n', newline='\n')   #zgodne 
    
    xLocal = xLocal-camType.principalPoint[0]
    xLocal = np.dot(camType.pixelWidth, xLocal)
    #np.savetxt('xLocal.txt', xLocal, delimiter='\n', newline='\n') #zgodne 
    yLocal = yLocal-camType.principalPoint[1]
    yLocal = np.dot(np.dot(-1., camType.pixelHeight), yLocal)
    #np.savetxt('yLocal.txt', yLocal, delimiter='\n', newline='\n') #zgodne 
    #print xLocal[0][13308], yLocal[0][13308], zLocal[0][13308]
    dLocal = np.sqrt((np.power(xLocal,2)+np.power(yLocal,2)+np.power(zLocal,2)))
    #np.savetxt('dLocal_backprojection.txt', dLocal, delimiter='\n', newline='\n') #zgodne
    #for x in range(0,23444):
    #    if dLocal[0][x] == 0:
    #        print x
            
   
    #np.savetxt('dLocal', dLocal)
    #print frame.distances
    #print frame.distances
    #print len(frame.distances[0])
    #print frame.distances.size
    #print dLocal.size
    tScale = frame.distances/dLocal
    x = tScale*xLocal
    #np.savetxt('x.txt', x, delimiter='\n', newline='\n') # zgodne
    y = tScale*yLocal
    #np.savetxt('y.txt', y, delimiter='\n', newline='\n') # zgodne
    z = tScale*zLocal
    #np.savetxt('z.txt', z, delimiter='\n', newline='\n') # zgodne
    frame.points3D = np.array(np.vstack((np.hstack((x)), np.hstack((y)), np.hstack((z)), np.hstack((np.ones((1, np.dot(camType.height, camType.width))))))))
    #np.savetxt('frame.points3D.txt', frame.points3D, delimiter='\n', newline='\n')
    #np.savetxt('frame.points3D[0].txt', frame.points3D[0], delimiter='\n', newline='\n') # zgodne
    #np.savetxt('frame.points3D[1].txt', frame.points3D[1], delimiter='\n', newline='\n')# zgodne
    #np.savetxt('frame.points3D[2].txt', frame.points3D[2], delimiter='\n', newline='\n')# zgodne
    #np.savetxt('frame.points3D[3].txt', frame.points3D[3], delimiter='\n', newline='\n')# zgodne
    
    frame.points3D_org = np.array(np.vstack((np.hstack((x)), np.hstack((y)), np.hstack((z)), np.hstack((np.ones((1, np.dot(camType.height, camType.width))))))))
    #np.savetxt('frame.points3D_org.txt', frame.points3D_org, delimiter='\n', newline='\n')
    #np.savetxt('frame.points3D_org[0].txt', frame.points3D_org[0], delimiter='\n', newline='\n')# zgodne
    #np.savetxt('frame.points3D_org[1].txt', frame.points3D_org[1], delimiter='\n', newline='\n')# zgodne
    #np.savetxt('frame.points3D_org[2].txt', frame.points3D_org[2], delimiter='\n', newline='\n')# zgodne
    #np.savetxt('frame.points3D_org[3].txt', frame.points3D_org[3], delimiter='\n', newline='\n')# zgodne
    
    
    return frame