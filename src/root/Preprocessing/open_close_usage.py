import sys
import numpy as np
import scipy as sc
import matcompat
import scipy.ndimage
import matplotlib.pyplot as plt
# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def open_close_usage(fr, camType, method):
    np.disp('open_close_usage ...')
    # Local Variables: map, fr, camType, use, method, width, usage, height, frame, se
    # Function calls: disp, strel, imopen, open_close_usage, find, imclose, zeros, reshape, strcmp
    #% frame = open_close_usage(fr, camType, method)
    frame = fr
    usage = fr.usage
    width = camType.width
    height = camType.height
    #print type(width), type(height)
    map1 = np.zeros((1, width * height))
    
    #print usage, len(usage), usage, len(map1[0])
    #np.savetxt('usage', usage)
    map1=map1[0]
    map1[usage]=1
    #print len(map1)
    #dla porownania estetycznego  .conj().T
    map1 = np.reshape(map1, (height, width))
    #plt.imshow(map1)
    #plt.show()
    #print 'map1', map1, len(map1)
    #map1 = np.reshape(map1, (width, height))
    #print 'map1', map1, len(map1)
    se = np.ones((3,3))
    #%se = strel('disk', 1);
    if method == 'open-close' :
        map1 = scipy.ndimage.morphology.binary_opening(scipy.ndimage.morphology.binary_closing(map1, structure=se), structure=se)
    elif method == 'open':
        map1 = scipy.ndimage.binary_opening(map1, structure=se)
        
    elif method == 'close-open':
        map1 = scipy.ndimage.morphology.binary_closing(scipy.ndimage.morphology.binary_opening(map1, structure=se), structure=se)
        
    elif method ==  'close':
        map1 = scipy.ndimage.binary_closing(map1, structure=se)
        
    else:
        np.disp('Error: Unknown morphological method!')
        
    #print 'map1', map1, len(map1)
    #np.savetxt('map1', map1)
    map1=map1*1   
    #print 'map1', map1, len(map1)
    
    map1 = np.reshape(map1, (1,(width*height)))
    use = np.nonzero((map1 == 1))
    frame.usage = use[1]
    #np.savetxt('frame.usage_openclose.txt', frame.usage, delimiter='\n', newline='\n')
    #print 'frame.usage', frame.usage, len(frame.usage)
    #sys.exit("Error message")
    return frame