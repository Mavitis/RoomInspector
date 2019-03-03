
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def frame_decompostion(frame, camType):

    # Local Variables: frame, colorstep, bwDis, ni, uRest, regions, maxi, fig, ns, camType, map, imDis, scrsz, plane, regionsVec, d, i, n, p, s, points, ui, se, planes, bins
    # Function calls: figure, strel, imdilate, ismember, frame_decompostion, find, struct, reshape, imshow, mod, sort, plot_3Dpoints, colormap, get, max, main_plane_extraction, region_growing, length, edge, histc, imerode, round
    #% regions = frame_decomposition(frame)
    scrsz = plt.get(0., 'ScreenSize')
    se = strel('square', 5.)
    imDis = np.reshape((frame.points3D_org[2,:]), (camType.width), np.array([])).conj().T
    plt.figure('Position', np.array(np.hstack((1., scrsz[3]/2., scrsz[2]/2., scrsz[3]/2.))))
    plt.imshow(imDis, np.array([]))
    imDis = imerode(imdilate(imDis, se), se)
    bwDis = edge(imDis, 'canny')
    bwDis = imerode(imdilate(bwDis, se), se)
    regions = region_growing(bwDis)
    regionsVec = np.reshape(regions.conj().T, 1., np.array([]))
    bins = np.arange(-2., (matcompat.max(matcompat.max(regions)))+(1.), 1.)
    n = histc(regionsVec, bins)
    n = n[3:]
    [ns, ni] = np.sort(n, 'descend')
    uRest = frame.usage
    plane = struct('points', np.array([]), 'n', np.array(np.vstack((np.hstack((0.)), np.hstack((0.)), np.hstack((0.))))), 'd', 0.)
    planes = np.array([])
    fig = plt.figure('Position', np.array(np.hstack((1., 1., scrsz[2]/2., scrsz[3]/2.))))
    map = colormap('jet')
    i = 1.
    while i<=6.:
        if i<=length(ni):
            maxi = ni[int(i)-1]
            ui = nonzero((regionsVec == maxi))
            ui = ui[int(ismember(ui, (frame.usage)))-1]
            uRest[int(ismember[int(uRest)-1,int(ui)-1])-1] = np.array([])
            s.cell[int(i)-1] = frame.points3D_org[0:3.,int(ui)-1]
            [p, n, d] = main_plane_extraction(s.cell[int(i)-1])
            plane.points = s.cell[int(i)-1,:,int(p)-1]()
            plane.n = n
            plane.d = d
            planes = np.array(np.hstack((planes, plane)))
            ui[int(p)-1] = np.array([])
            uRest = np.array(np.hstack((uRest, ui)))
            #%fig = plot_3Dpoints(plane.points, map(mod(1 + (i-1)*5, length(map)), :), fig);
        
        
        i = i+1.
        
    i = 1.
    colorstep = np.round(matdiv(length(map), length(planes)))
    while i<=length(planes):
        fig = plot_3Dpoints((planes[int(i)-1].points), map[int(np.mod((65.-np.dot(i-1., colorstep)), length(map)))-1,:], fig)
        i = i+1.
        
    fig = plot_3Dpoints((frame.points3D_org[0:3.,int(uRest)-1]), 'k', fig)
    #% max1 = ni(1);
    #% max2 = ni(2);
    #% max3 = ni(3);
    #% max4 = ni(4);
    #% 
    #% u1 = find(regionsVec == max1);
    #% u2 = find(regionsVec == max2);
    #% u3 = find(regionsVec == max3);
    #% u4 = find(regionsVec == max4);
    #% 
    #% u1 = u1(ismember(u1, frame.usage));
    #% u2 = u2(ismember(u2, frame.usage));
    #% u3 = u3(ismember(u3, frame.usage));
    #% u4 = u4(ismember(u4, frame.usage));
    #% 
    #% uRest = frame.usage;
    #% uRest(ismember(uRest, u1)) = [];
    #% uRest(ismember(uRest, u2)) = [];
    #% uRest(ismember(uRest, u3)) = [];
    #% uRest(ismember(uRest, u4)) = [];
    #% 
    #% s1 = frame.points3D_org(1:3, u1);
    #% [p1, n1, d1] = main_plane_extraction(s1);
    #% p1Rest = 1:1:length(s1);
    #% p1Rest(ismember(p1Rest, p1)) = [];
    #% 
    #% s2 = frame.points3D_org(1:3, u2);
    #% [p2, n2, d2] = main_plane_extraction(s2);
    #% p2Rest = 1:1:length(s2);
    #% p2Rest(ismember(p2Rest, p2)) = [];
    #% 
    #% s3 = frame.points3D_org(1:3, u3);
    #% [p3, n3, d3] = main_plane_extraction(s3);
    #% p3Rest = 1:1:length(s3);
    #% p3Rest(ismember(p3Rest, p3)) = [];
    #% 
    #% s4 = frame.points3D_org(1:3, u4);
    #% [p4, n4, d4] = main_plane_extraction(s4);
    #% p4Rest = 1:1:length(s4);
    #% p4Rest(ismember(p4Rest, p4)) = [];
    #% s4 = frame.points3D_org(1:3, uRest);
    #% [p4, n4, d4] = main_plane_extraction(s4);
    #% p4Rest = 1:1:length(s4);
    #% p4Rest(ismember(p4Rest, p4)) = [];
    #% s1plane = s1(:, p1);
    #% s2plane = s2(:, p2);
    #% s3plane = s3(:, p3);
    #% s4plane = s4(:, p4);
    #% s1Rest = s1(:, p1Rest);
    #% s2Rest = s2(:, p2Rest);
    #% s3Rest = s3(:, p3Rest);
    #% s4Rest = s4(:, p4Rest);
    #% sRest = [s1(:, p1Rest) s2(:, p2Rest) s3(:, p3Rest) s4(:,p4Rest)];
    #% 
    #% fig1 = plot_3Dpoints(s1plane, 'r');
    #% fig1 = plot_3Dpoints(s1Rest, 'k', fig1);
    #% fig2 = plot_3Dpoints(s2plane, 'g');
    #% fig2 = plot_3Dpoints(s2Rest, 'k', fig2);
    #% fig3 = plot_3Dpoints(s3plane, 'b');
    #% fig3 = plot_3Dpoints(s3Rest, 'k', fig3);
    #% fig4 = plot_3Dpoints(s4plane, 'y');
    #% fig4 = plot_3Dpoints(s4Rest, 'k', fig4);
    #% 
    #% fig = plot_3Dpoints(s1plane, 'r');
    #% fig = plot_3Dpoints(s2plane, 'g', fig);
    #% fig = plot_3Dpoints(s3plane, 'b', fig);
    #% fig = plot_3Dpoints(s4plane, 'y', fig);
    #% fig = plot_3Dpoints(sRest, 'k', fig);
    #% fig = plot_3Dpoints(frame.points3D_org(1:3, u1), 'r');
    #% fig = plot_3Dpoints(frame.points3D_org(1:3, u2), 'g', fig);
    #% fig = plot_3Dpoints(frame.points3D_org(1:3, u3), 'b', fig);
    return [planes]