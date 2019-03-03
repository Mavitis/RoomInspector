
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def generate_camera_data(camType):

    # Local Variables: principalPoint, name, focalLength, camType, height, width, camera, pixelWidth, pixelHeight
    # Function calls: display, generate_camera_data, struct, strcmp
    #% cameraData = generate_camera_data(camType)
    #%
    #% camType: 'PMD_16x64', 'PMD_120x160', 'SR_176x144', 'SR_176x144calib'
     #all values are given in mm
     
    class my_camera:
        name = 0
        height = 0
        width = 0
        focalLength = 0
        principalPoint = [0, 0]
        pixelWidth = 0.0
        pixelHeight = 0.0
    camera = my_camera()
    
    if (camType == 'PMD_16x64'):
        camera.name = 'PMD_16x64'
        camera.height = 16
        camera.width = 64
        camera.focalLength = 16
        camera.principalPoint = [31.5, 7.5]
        camera.pixelWidth = 0.1553
        camera.pixelHeight = 0.2108
    elif (camType == 'PMD_120x160'):
        camera.name = 'PMD_120x160'
        camera.height = 120
        camera.width = 160
        camera.focalLength = 12
        camera.principalPoint = [79.5, 59.5]
        camera.pixelWidth = 0.04
        camera.pixelHeight = 0.04
    elif (camType == 'SR_176x144'):
        camera.name = 'SR_176x144'
        camera.height = 144
        camera.width = 176
        camera.focalLength = 8
        camera.principalPoint = [92, 60]
        #camera.principalPoint = [88 72]; %take data from calibration
        camera.pixelWidth = 0.04
        camera.pixelHeight = 0.04
    elif (camType == 'SR_176x144calib'):
        camera.name = 'SR_176x144'
        camera.height = 144
        camera.width = 176
        camera.focalLength = 8
        camera.principalPoint = [86, 70]
        camera.pixelWidth = 0.04
        camera.pixelHeight = 0.04
    elif (camType == 'SR4_176x144'):
        camera.name = 'SR4_176x144'
        camera.height = 144
        camera.width = 176
        camera.focalLength = 10
        camera.principalPoint = [88, 72]
        camera.pixelWidth = 0.04
        camera.pixelHeight = 0.04
    else:
        np.disp('Unknown camera type.')
    
    
    return camera