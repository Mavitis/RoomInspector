
import numpy as np
import scipy
import matcompat
import root.Preprocessing.projection as pro

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def srdat2frame(srMatrix, camType):

    # Local Variables: amplitudes, points3D_org, points3D, frame, srMatrix, amp, y, x, z, camType
    # Function calls: reshape, ones, srdat2frame, struct, projection
    class my_frame:
        distances = []
        intensities = []
        amplitudes = []
        points3D = []
        points3D_org = []
        usage = []
        indx8= []
    frame = my_frame()

    z = 1000.*srMatrix[0:camType.height,:]
    
    #np.disp(np.size(z,0))
    #np.disp(np.size(z,1))
    #%z = z(:,end:-1:1);
    w = np.size(z,0)*(np.size(z,1))
    #np.disp(w)
    z = np.reshape(z, (1, w))
    #np.savetxt('z.txt', z, delimiter=' ', newline='    ')
    x = 1000.*srMatrix[int(camType.height+1.)-1:2*camType.height,:]
    #%x = x(:,end:-1:1);
    w = np.size(x,0)*(np.size(x,1))
    #np.disp(w)
    x = np.reshape(x, (1, w))
    y = 1000.*srMatrix[int(2.*camType.height+1.)-1:3*camType.height,:]
    #%y = y(:,end:-1:1);
    w = np.size(y,0)*(np.size(y,1))
    #np.disp(w)
    y = np.reshape(y, (1, w))
    amp = srMatrix[int(3.*camType.height+1.)-1:4*camType.height,:]
    #np.savetxt('amp.txt', amp, delimiter=' ', newline='    ')
    w = np.size(amp,0)*(np.size(amp,1))
    #np.disp(w)
    amp = np.reshape(amp, (1, w))
    #np.savetxt('amp2.txt', amp, delimiter=' ', newline='    ')

    frame.amplitudes = amp
    #np.disp(amp)
    #% The Swissranger delivers the data in a right handed coordinate system
    #% with the first pixel being in the top-left corner. (-> positive x-values
    #% to the left)
    #% I prefer a left handed system with positive x-values to the right,
    #% therefore the sign of the x-values have to be switched.
    #% Warning: As MatLab uses a right-handed system the data has to be mirrored
    #% again in plot_3Dpoints for displaying
    frame.points3D = np.array(np.vstack((np.hstack((-x)), np.hstack((y)), np.hstack((z)), np.hstack((np.ones(w, dtype=np.int))))))
    frame.points3D_org = frame.points3D
    #% if(size(srMatrix,1) > 4*camType.height)
    #%     u = srMatrix((4*camType.height+1):(5*camType.height),:);
    #%     u = reshape(u',1,[]);
    #%     frame.usage = find(u == 1);
    #% else 
    #%     frame.usage = 1:1:(camType.width*camType.height);
    #% end
    #% 
    #% if(size(srMatrix,1) > 5*camType.height)
    #%     nX = srMatrix((5*camType.height+1):(6*camType.height),:);
    #%     nX = reshape(nX',1,[]);
    #%     nY = srMatrix((6*camType.height+1):(7*camType.height),:);
    #%     nY = reshape(nY',1,[]);
    #%     nZ = srMatrix((7*camType.height+1):(8*camType.height),:);
    #%     nZ = reshape(nZ',1,[]);
    #%     frame.normals = [nX; nY; nZ];
    #%     frame.planar = frame.usage;
    #%     frame.notplanar = find(u == 0);
    #%     
    #%     i = 1 : camType.width*camType.height;
    #%     pos = reshape(i, camType.width, [])';
    #%     i = mat2cell(i, 1, ones(1, camType.width*camType.height));
    #%     indx = cellfun(@(x)(getNgbIndx(x, camType.width, camType.height, 3, true, pos)), i, 'UniformOutput', false);
    #%     frame = setfield(frame, 'indx8', indx);
    #%     
    #% end
    frame = pro.projection(frame, camType)
    #np.disp(frame.amplitudes)
    #np.disp(amp)
    return frame