import numpy as np
import sys
import scipy
import string
from median_filtering import median_filtering
from thresholding import thresholding
from edgepoint_removing import edgepoint_removing
from open_close_usage import open_close_usage
from compute_normals import compute_normals
from root.Utilities.getNgbIndx import getNgbIndx
from svd_enhancing import svd_enhancing
from copy_NgbIndx import copy_NgbIndx


# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def preprocessing(seq=None, mode=None):
    #% sequence = preprocessing(seq, mode)
    #
    # the possible parameters for 'mode' are:
    # ---------------------------------------
    # - 'median'   : performs a distance-adaptive median filter on the
    #                distances
    #
    # - 'threshld' : applies a dynamic amplitude threshold rejecting invalid
    #                distance measurements via its amplitude value
    #
    # - 'edgerm'   : remove false measurements arising in the case of edges
    #
    # - 'open'     : applies an opening on the binary image of the usage vector
    #                holding the valid distance measurements
    #
    # - 'normals'  : computes for each point its normal using its
    #                8-neighborhood
    #
    # - 'ngb'      : stores for each point the indices of its 8-neighborhood
    #
    #
    # - 'standard' : performs the methods of 'median', 'threshld', 'open',
    #                'edgerm'
    # - 'all'      : performs all available methods

    np.disp('Preprocessing ...')

    if (mode == None):
        mode = 'standard' 
        
    else:

        #% determine the methods that should be performed:
        med = 0
        thres = 0
        edge = 0
        open = 0
        norm = 0
        ngb = 0
        svd = 0

        __switch_0__ = mode
        if 0:
            pass
        elif __switch_0__ == 'all':
            med = 1
            thres = 1
            edge = 1
            open = 1
            norm = 1
            ngb = 1
        elif __switch_0__ == 'median':
            med = 1
        elif __switch_0__ == 'threshld':
            thres = 1
        elif __switch_0__ == 'edgerm':
            edge = 1
        elif __switch_0__ == 'open':
            open = 1
        elif __switch_0__ == 'normals':
            norm = 1
            ngb = 1
        elif __switch_0__ == 'ngb':
            ngb = 1
        elif __switch_0__ == 'svd':
            thres = 1
            edge = 1
            open = 1
            svd = 1
            norm = 1
        elif __switch_0__ == 'standard':
            med = 1
            thres = 1
            edge = 1
            open = 1
        else:
            np.disp('Error: Unknown value for parameter "mode"')
        
         

    indx = []
    sequence = seq
    w = sequence.camType.width
    h = sequence.camType.height

    if (med):
        sequence.frames =[median_filtering(x, sequence.camType) for x in sequence.frames]
        #sequence.frames = cell2mat(arrayfun(lambda x: median_filtering(x, sequence.camType), sequence.frames)

    if (thres):
        sequence.frames =[thresholding(x, sequence.camType) for x in sequence.frames]
        #sequence.frames = cell2mat(arrayfun(lambda x: thresholding(x, sequence.camType), sequence.frames)

    if (edge):
        sequence.frames =[edgepoint_removing(x, sequence.camType) for x in sequence.frames]
        #sequence.frames = cell2mat(arrayfun(lambda x: edgepoint_removing(x, sequence.camType), sequence.frames, 'UniformOutput', false))

    if (open):
        sequence.frames =[open_close_usage(x, sequence.camType, 'open') for x in sequence.frames]
        #sequence.frames = cell2mat(arrayfun(lambda x: open_close_usage(x, sequence.camType, 'open'))), sequence.frames, 'UniformOutput', false))

    if (norm):#Nadal niezgodna numerycznie dev i wszystko co dalej!
        sequence.frames =[compute_normals(x, sequence.camType) for x in sequence.frames]
        
        
    if (ngb): # czy jest potrzeba ponownie, jak juz liczone w norm? Sprawdzic ale tutaj sa bledy
        i = np.arange(w*h)
        pos = np.arange(1, (w*h)+1)
        
        pos = np.reshape(pos, (w, h)).conj().T
        #pos = np.reshape(i, (w*h))
        i = np.reshape(i, (1,w*h))
        
        
        indx =[getNgbIndx(x, h, w, 3., 'true' , pos) for x in (i[0]+1)] #zamieniono kolejnosc w z h!!! ? 10.02 zamiana wrocone

        sequence.frames =[ (x, indx) for x in sequence.frames]
        

        #sequence.frames =[x.indx8.setfield(indx) for x in sequence.frames] 
        #sequence.frames = cell2mat(arrayfun(lambda x: (setfield(x, 'indx8', indx)), sequence.frames, 'Uniformoutput', false))

    if (svd):
        sequence.frames =[svd_enhancing(x, sequence.camType) for x in sequence.frames]
        #sequence.frames = cell2mat(arrayfun(lambda x: (svd_enhancing(x, sequence.camType)), sequence.frames, 'UniformOutput', false))

    #% perform selected preprocessing for each frame of the sequence:
    # f=1;
    # while(f<=length(sequence.frames))
    #     
    #     % find points with z-values == 0: Points would lie on the image plane
    #     use = find(sequence.frames(f).points3D_org(3,:) ~= 0);
    #     u = ismember(sequence.frames(f).usage, use);
    #     sequence.frames(f).usage = sequence.frames(f).usage(u);
    #     
    #     % if no point of a frame will be used (bad frame) this frame is deleted:
    #     if(length(sequence.frames(f).usage) == 0)
    #         sequence.frames(f) = [];
    #     else
    #         f=f+1;
    #     end
    # 
    # end
                                        
    return sequence
