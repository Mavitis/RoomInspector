
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def align_pnts2plane(pnts, normal, center):

    # Local Variables: center, normal, Rot1, T2, normal_new, Rot2, newPnts, T1, angle1, angle2, Rot, pnts
    # Function calls: cos, atan, ones, align_pnts2plane, sin, size
    #%% [newPnts, Rot] = align_pnts2plane(pnts, normal, center)
    if np.size(pnts, 1.) == 3.:
        pnts = np.array(np.vstack((np.hstack((pnts)), np.hstack((np.ones(1., matcompat.size(pnts, 2.)))))))
    
    
    #%% move points with center to origin
    #%Tc = eye(4);
    #%Tc(1:3,4) = -1*center(1:3);
    #%Pnts_new = Tc * Pnts_new;
    #%Pnts_new = Pnts-repmat([center(1:3); 0], 1, size(Pnts,2));
    T1 = np.array(np.vstack((np.hstack((1., 0., 0., -center[0])), np.hstack((0., 1., 0., -center[1])), np.hstack((0., 0., 1., -center[2])), np.hstack((0., 0., 0., 1.)))))
    T2 = np.array(np.vstack((np.hstack((1., 0., 0., 0.)), np.hstack((0., 1., 0., 0.)), np.hstack((0., 0., 1., center[2])), np.hstack((0., 0., 0., 1.)))))
    #%% calculate angles for rotation
    angle1 = np.arctan(normal[0]/normal[1]) #pewnie trzeba divide przez elementy 1 do 1?
    Rot1 = np.array(np.vstack((np.hstack((np.cos(angle1), -np.sin(angle1), 0., 0.)), np.hstack((np.sin(angle1), np.cos(angle1), 0., 0.)), np.hstack((0., 0., 1., 0.)), np.hstack((0., 0., 0., 1.)))))
    normal_new = np.dot(Rot1, np.array(np.vstack((np.hstack((normal)), np.hstack((1.))))))
    angle2 = np.arctan(normal_new[1]/normal[2])
    Rot2 = np.array(np.vstack((np.hstack((1., 0., 0., 0.)), np.hstack((0., np.cos(angle2), -np.sin(angle2), 0.)), np.hstack((0., np.sin(angle2), np.cos(angle2), 0.)), np.hstack((0., 0., 0., 1.)))))
    #%% transformation matrix
    Rot = np.dot(np.dot(Rot2, Rot1), T1)
    #% Rot = [cos(angle1) -sin(angle1) 0 -center(1)*cos(angle1)+center(2)*sin(angle1); ...
    #%     cos(angle2)*sin(angle1) cos(angle2)*cos(angle1) -sin(angle2) -center(1)*cos(angle2)*sin(angle1)-center(2)*cos(angle2)*cos(angle1)+center(3)*sin(angle2); ...
    #%     sin(angle2)*sin(angle1) sin(angle2)*cos(angle1) cos(angle2) -center(1)*sin(angle2)*sin(angle1)-center(2)*sin(angle2)*cos(angle1)- center(3)*cos(angle2)+center(3); ...
    #%     0 0 0 1];
    #% rotate points in origin
    newPnts = np.dot(Rot, pnts)
    return [newPnts, Rot]