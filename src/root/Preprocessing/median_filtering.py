
import numpy as np
import scipy
import matcompat
from distance_adaptive_median import distance_adaptive_median
from backprojection_fast import backprojection_fast

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def median_filtering(fr, camType):
    np.disp('median_filtering ...')

    # Local Variables: camType, frame, fr, distances
    # Function calls: median_filtering, distance_adaptive_median, backprojection_fast, reshape
    #% frame = median_filtering(fr, camType)
    frame = fr
    #np.savetxt('frame.distances_input.txt', frame.distances)
    #np.disp(np.size(frame.distances))
    distances = np.reshape((frame.distances), (camType.height, camType.width)) #tutaj zamienione heigyht z weight i dziala! resazy odwrotnie? 
    distances = distances.conj().T
    #np.savetxt('distances.txt', distances, delimiter='\n', newline='\n')
    #%amplitudes = reshape(frame.amplitudes, camType.width, camType.height);
    #%amplitudes = amplitudes';
    #%intensities = reshape(frame.intensities, camType.width, camType.height);
    #%intensities = intensities';
    #%amplitudes = reshape(frame.amplitudes, camType.width, camType.height);
    #%amplitudes = amplitudes';
    #%intensities = medfilt2(intensities, [3 3]);
    #%amplitudes = medfilt2(amplitudes, [3 3]);
    #%distances = medfilt2(distances, [3 3]);
    distances = distance_adaptive_median(distances, camType)
    #%distances = amplitude_adaptive_median(distances, amplitudes, camType);
    #%frame.intensities = reshape(intensities', 1, camType.width*camType.height);
    #%frame.amplitudes = reshape(amplitudes', 1, camType.width*camType.height);
    frame.distances = np.reshape(distances.conj().T, (1, camType.width * camType.height))
    #print frame.distances[0]
    #np.savetxt('frame.distances.txt', frame.distances[0])
    frame = backprojection_fast(frame, camType)
    return frame