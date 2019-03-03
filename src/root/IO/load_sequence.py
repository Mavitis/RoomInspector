import numpy as np
import scipy
from srdat2frame import srdat2frame
from generate_camera_data import generate_camera_data
import string
import glob



# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def load_sequence(seqName, camType, posStart=1, numOfFrames=0):

    # Local Variables: distances, fr, seqName, amplitudes, d, idx, sequence, i, camType, help, posStart, currFrame, intensities, frame, usage, x, frames, numOfFrames, seq, name
    # Function calls: disp, load_sequence, false, struct, filesep, arrayfun, generate_camera_data, load, strcmp, nargin, length, isempty, num2str, srdat2frame, strfind, true, find, dir
    #% sequence = load_sequence(seqName, camType, posStart, numOfFrames):
    #%
    #%
    #% input variables:
    #%
    #% - seqName: holds the complete path of the directory storing the sequence.
    #%   The files containing frames of the Swissranger
    #%   camera has to be named in the following way:
    #%   frame_0001.dat, frame_0002.dat, ...
    #%
    #% - posStart: determines that frame were the sequence should start
    #%    e.g. 1 for the first frame ...
    #%
    #% - numOfFrames: determines the number of frames the sequence should contain
    #% 
    #% - camType: specifies the camera used
    #%    camera types known: 'PMD_16x64', 'PMD_120x160', 'SR_176x144' 
    if seqName[int(0)-1] != '/':
        seqName = seqName + '/'
        # verification if seqName ends with '/', if not, adding
    
    if numOfFrames==0:
        onlyfiles= glob.glob(str(seqName)+'*.dat')
        numOfFrames= len(onlyfiles)
    
    
    
    np.disp('Loading sequence data ...')
    
    class my_sequence:
        frames = []
        camType
    
    sequence = my_sequence()
    
    sequence.camType = generate_camera_data(camType)
    

    seq = []
    class my_frame:
        distances = []
        intensities = []
        amplitudes = []
        points3D = []
        points3D_org = []
        usage = []
        indx8=[]
    

    frame = my_frame()
    
    #np.disp(camType)
    #np.disp(seq)
    #np.disp(frame)
    #np.disp(sequence)
    if camType =='PMD_120x160' or camType == 'PMD_16x64': #not used camera for time beeing
  #      currFrame = posStart-1.
   #     name = camType
    #    help = np.array([])
        i = 1.
      #  while i<=numOfFrames:
       #     #%distances in mm
        #                name = [seqName, 'frame', str(currFrame)]
         #               help = load(name)
#
 #                       frame.distances = 1000 * help(mslice[3:end])
#
 #                       name = mcat([seqName, mstring('frame'), num2str(currFrame), mstring('_amp')])
  #                      help = load(name)
#
 #                       frame.amplitudes = help(mslice[3:end])
#
 #                       name = mcat([seqName, mstring('frame'), num2str(currFrame), mstring('_greyimg')])
  #                      help = load(name)
#
 #                       frame.intensities = help(mslice[3:end])
#
 #                       frame.usage = mslice[1:1:(sequence.camType.height * sequence.camType.width)]
#
 #                       seq = mcat([seq, frame])
#
 #                       i = i + 1
  #                      currFrame = currFrame + 1
    elif np.logical_or(np.logical_or(camType == 'SR_176x144', camType == 'SR4_176x144'), camType == 'SR_176x144calib'):
        
        currFrame = posStart
        name = ""
        help1 = string
        fr = np.array([])
        i = 1
        while i<=numOfFrames:
            np.disp(i)
            help1 = str(currFrame)
            
            _switch_val=len(help1)
            if False: # switch 
                pass
            elif _switch_val == 1:
                help1 = '000' + help1
            elif _switch_val == 2:
                help1 = '00' + help1
            elif _switch_val == 3:
                help1 = '0' + help1
            
               
            
            name = seqName+'frame_'+help1+'.dat'
            
            #removed try catch
            fr = np.loadtxt(name,dtype=float,comments='%',delimiter='\t')
            #np.disp(np.size(fr))
            #i = i+1
            #currFrame = currFrame+1
            
            
            frame = srdat2frame(fr, sequence.camType)
            #np.savetxt('frame_distances.txt', frame.distances, delimiter=' ', newline='    ')
            #np.savetxt('frame_intensities.txt', frame.intensities, delimiter=' ', newline='    ')
            #np.savetxt('frame_amplitudes.txt', frame.amplitudes, delimiter=' ', newline='    ')
            #np.savetxt('frame_points3D_0.txt', frame.points3D[0], delimiter=' ', newline='    ')
            #np.savetxt('frame_points3D_1.txt', frame.points3D[1], delimiter=' ', newline='    ')
            #np.savetxt('frame_points3D_2.txt', frame.points3D[2], delimiter=' ', newline='    ')
            #np.savetxt('frame_points3D_3.txt', frame.points3D[3], delimiter=' ', newline='    ')
            #np.savetxt('frame_points3D_org.txt', frame.points3D_org, delimiter=' ', newline='    ')
            #np.savetxt('frame_usage.txt', frame.usage, delimiter=' ', newline='    ')

            seq = np.array(np.hstack((seq, frame)))
            currFrame = currFrame+1
            i = i+1
            
        
    else:
        np.disp('Unkown camera type!')
        
    
    sequence.frames = seq
    #np.savetxt('sequence.frames.distances', sequence.frames.distances, delimiter=' ', newline='    ')
    #np.disp(seq)
    return sequence