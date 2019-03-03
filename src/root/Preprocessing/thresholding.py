import sys
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def thresholding(fr, camType):
    np.disp('thresholding ...')

    # Local Variables: meanAmp, fr, camType, usage, threshold, frame
    # Function calls: length, thresholding, sum, find
    #%% frame = thresholding(fr, camType)
    frame = fr
    #%% thresholding on amplitudes: 
    meanAmp = np.sum(frame.amplitudes)/frame.amplitudes.size
    #print frame.amplitudes.size
    #print np.sum(frame.amplitudes)
    #print meanAmp
    #np.savetxt('meanAmp.txt', meanAmp, delimiter='\n', newline='\n')
    threshold = 1./3. * meanAmp
    #print threshold
    frame.usage = np.nonzero((frame.amplitudes >= threshold))
    #np.savetxt('thFrameUsage.txt', frame.usage, delimiter='\n', newline='\n')
    #sys.exit("Error message")
    #%% add some additional data with bad amplitudes but stable neighborhood
    #% (slow operation)
    #% dis = reshape(frame.distances, camType.width, [])';
    #% 
    #% j = 1:camType.width;
    #% j = repmat(j, 1, camType.height);
    #% j = num2cell(j);
    #% 
    #% i = 1:camType.height;
    #% i = i';
    #% i = repmat(i, 1, camType.width);
    #% i = reshape(i', 1, []);
    #% i = num2cell(i);
    #% 
    #% currD = num2cell(frame.distances);
    #% 
    #% currN = cellfun(@(x,y,d) (reshape(abs(get8region(dis,x,y) - d)', 1, [])), ...
    #%     i, j, currD, 'UniformOutput', false);
    #% 
    #% distribution = cellfun(@(x)(sqrt(sum((x-mean(x)).^2)/(length(x)-1))), currN, 'UniformOutput', false);
    #% distribution = [distribution{1:end}];
    #% 
    #% stdD = std(distribution);
    #% 
    #% add = find(frame.amplitudes < threshold & distribution < stdD/3);
    #% 
    #% dis7 = medfilt2(dis, [9 9]);
    #% dis7 = reshape(dis7', 1, []);
    #% frame.distances(add) = dis7(add);
    #% 
    #% frame.usage = [frame.usage add];
 
    return frame