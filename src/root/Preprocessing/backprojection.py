
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def backprojection(fr, camType):

    # Local Variables: distances, fr, scale, points3D_org, i, camType, j, points3D, yHelp, distLocal, v1, v2, v3, xHelp, frame
    # Function calls: reshape, backprojection, sqrt
    #%frame = backprojection(fr, camType)
    np.disp('Trwa wykonywanie: backprojection')
    frame = fr
    distances = frame.distances
    distances = np.reshape(distances, (camType.width, camType.height)).cT
    xHelp = 0
    yHelp = 0
    distLocal = 0
    scale = 0
    v1 = 0
    v2 = 0
    v3 = 0

    j = 0
    i = 0
    while (j < camType.height):

        i = 0
        while (i < camType.width):

            xHelp = (i - camType.principalPoint(1)) * camType.pixelWidth
            yHelp = (j - camType.principalPoint(2)) * camType.pixelHeight * (-1)

            distLocal = np.sqrt((camType.focalLength) ** 2 + xHelp ** 2 + yHelp ** 2)

            scale = (distances(j + 1, i + 1) / distLocal) + 1

            v1 = xHelp * scale
            v2 = yHelp * scale
            v3 = camType.focalLength * scale
            
            frame.points3D = np.array(frame.points3D, np.vstack(np.hstack(v1), np.hstack(v2), np.hstack(v3)))
            frame.points3D_org = np.array(frame.points3D_org, np.vstack(np.hstack(v1), np.hstack(v2), np.hstack(v3)))

            i = i + 1

        j = j + 1
    
    return frame