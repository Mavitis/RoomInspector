
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def position_point_cloud(Pnts):

    # Local Variables: Rot2, center, Pnts_new, normal, Rot1, normal_new, posEnd, T2, T1, angle1, angle2, Rot, Pnts, dEnd
    # Function calls: cos, main_plane_extraction, atan, sum, position_point_cloud, sin, size
    #% Pnts_new = position_point_cloud(Pnts)
    #% Pnts = 3 x n matrix = 3D point cloud
    #% Pnts_new = 3 x n matrix, new relocated point cloud
    #%
    #% Positions given point cloud to be parallel to the image plane.
    #% finding plane in point_cloud
    [posEnd, normal, dEnd] = main_plane_extraction(Pnts[0:3.,:])
    #%[coeff, score, roots] = princomp(Pnts(1:3,:)');
    #%normal = coeff(:,3);
    #% determine center
    center = np.sum(Pnts, 2.)/matcompat.size(Pnts, 2.)
    #%% move points with center to origin
    #%Tc = eye(4);
    #%Tc(1:3,4) = -1*center(1:3);
    #%Pnts_new = Tc * Pnts_new;
    #%Pnts_new = Pnts-repmat([center(1:3); 0], 1, size(Pnts,2));
    T1 = np.array(np.vstack((np.hstack((1., 0., 0., -center[0])), np.hstack((0., 1., 0., -center[1])), np.hstack((0., 0., 1., -center[2])), np.hstack((0., 0., 0., 1.)))))
    T2 = np.array(np.vstack((np.hstack((1., 0., 0., 0.)), np.hstack((0., 1., 0., 0.)), np.hstack((0., 0., 1., center[2])), np.hstack((0., 0., 0., 1.)))))
    #%% calculate angles for rotation
    angle1 = atan(matdiv(normal[0], normal[1]))
    Rot1 = np.array(np.vstack((np.hstack((np.cos(angle1), -np.sin(angle1), 0., 0.)), np.hstack((np.sin(angle1), np.cos(angle1), 0., 0.)), np.hstack((0., 0., 1., 0.)), np.hstack((0., 0., 0., 1.)))))
    normal_new = np.dot(Rot1, np.array(np.vstack((np.hstack((normal)), np.hstack((1.))))))
    angle2 = atan(matdiv(normal_new[1], normal[2]))
    Rot2 = np.array(np.vstack((np.hstack((1., 0., 0., 0.)), np.hstack((0., np.cos(angle2), -np.sin(angle2), 0.)), np.hstack((0., np.sin(angle2), np.cos(angle2), 0.)), np.hstack((0., 0., 0., 1.)))))
    #%% transformation matrix
    Rot = np.dot(np.dot(np.dot(T2, Rot2), Rot1), T1)
    #% Rot = [cos(angle1) -sin(angle1) 0 -center(1)*cos(angle1)+center(2)*sin(angle1); ...
    #%     cos(angle2)*sin(angle1) cos(angle2)*cos(angle1) -sin(angle2) -center(1)*cos(angle2)*sin(angle1)-center(2)*cos(angle2)*cos(angle1)+center(3)*sin(angle2); ...
    #%     sin(angle2)*sin(angle1) sin(angle2)*cos(angle1) cos(angle2) -center(1)*sin(angle2)*sin(angle1)-center(2)*sin(angle2)*cos(angle1)- center(3)*cos(angle2)+center(3); ...
    #%     0 0 0 1];
    #% rotate points in origin
    Pnts_new = np.dot(Rot, Pnts)
    #% % move points to have center on z-axis
    return [Pnts_new, Rot]