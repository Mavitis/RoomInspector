import numpy as np
import sys
import scipy
import string
from cluster_through_regions import cluster_through_regions
from pnts2plane_classification_rgrow import pnts2plane_classification_rgrow
from pnts2plane_classification_RANSAC import pnts2plane_classification_RANSAC


# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def extract_planes(fr, cam, minSize, method, display=False):
## by Agnes Swadzba
# University Bielefeld
# Applied Informatics
# contact: aswadzba@techfak.uni-bielefeld.de
#
# [planes, clusters, rest, restIndx] = extract_planes(fr, cam, minSize, method, display)
# 
# frame: a struct consisting of distances, amplitudes, points3D, usage,
#        normals, ...
# cam: a struct for the camera consisting of focalLength, principalPoint,
#      pixelWidth, pixelHeight, ...
# minSize: specify the number points a plane has to consist of at least
# method: specify the method that will be used to form clusters of points within
#         the point cloud; 
#         possible: 
#           - 'regions' (cluster points lying inside of
#                        connected edges the socalled regions; a region image is
#                        realized through computing edges on a distances image)
#                        -> takes texture into consideration
#           - 'normals' (cluster points which have similar normals) 
#                        -> is not a very suitable method
#           - 'connectedPnts' (points are connected to their neighbors
#                              and therefore clustered into the same cluster, when the
#                              Euclidean distance in 3D between them is smaller than a
#                              certain threshold) 
#                              -> very good method
#           - 'planarClsts' (local planar patches are clustered to the
#                            same plane cluster depending on a conormality and a
#                            coplanarity measure) 
#                            -> very good method
#           - 'rGrow' is based on region growing using the information of
#                            local neighborhood. The method proposed by
#                            Olaf Khler is used to realize a rough
#                            segmentation which is refined by RANSAC
#                            (e.g. extract two walls connected via a
#                            corner)

## some default values:



    
    np.disp('Extract_planes ...')
    
 #   if (method=='histNormals' or method=='histNormals+gmd'):
 #       pntsNew = position_point_cloud(fr.points3D);
 #       fr.points3D = pntsNew;
 #   
    rest = []
    restIndx = []
    
    
    
    
                                
#     return 0
    
    if(method =='regions'):
        [clusters, clusterIndx, rest, restIndx] = cluster_through_regions(fr, cam);
#    elif(method== 'normals'):
#        # threshold = 30 = 3*pi/18 = 0.5236
#        [clusters, clusterIndx] = cluster_through_normals(fr, cam, 0.5236);
#    elif(method== 'connectedPnts'):
        # camProportion = 0.04 / 8;
#        camProportion = 1;
#        [clusters, rest, clusterIndx] = cluster_through_connectedPoints(fr);
        #clusters = cluster_through_connectedPoints_rgrow(pnts, width, height, camProportion, usage);
    elif(method== 'planarClsts'):
        [clusters, rest, clusterIndx, restIndx] = pnts2plane_classification_rgrow(fr, cam);
#    elif(method== 'rGrow'):
#        [clusters, rest, clusterIndx, restIndx] = pnts2plane_classification_rgrowpure(fr, cam);
#    elif(method== 'gmd'):
#        restIndx = 1:cam.width*cam.height;
#        restIndx(fr.usage) = [];
#        rest = fr.points3D(1:3,restIndx);
#        [clusters, clusterIndx] = cluster_through_gmd(fr.points3D(1:3,fr.usage));
#        clusterIndx = cellfun(@(x)(fr.usage(x)), clusterIndx, 'UniformOutput', false);
#    elif(method== 'histNormals'):
#        rest = [];
#        restIndx = [];
#        [clusters, clusterIndx] = cluster_through_histNormals(fr, cam);
#    elif(method== 'histNormals+gmd'):
#        rest = [];
#        restIndx = [];
#        [cl, clIndx] = cluster_through_histNormals(fr, cam);
#        clusters = [];
#        clusterIndx = [];
#        i = 1;
#        while(i <= len(cl))
#            [help, indx] = cluster_through_gmd(cl{i});
#            orgIndx = clIndx{i};
#            helpIndx = cellfun(@(x)(orgIndx(x)), indx, 'UniformOutput', false);
#            clusters = [clusters help];
#            clusterIndx = [clusterIndx helpIndx];
#            
#            i = i+1;
#
#    elif(method== 'cuefusion'))
#        [cl1, cl1Indx] = cluster_through_histNormals(fr, cam);
#        [cl2, cl2Indx] = cluster_through_regions(fr, cam);
#        
#        restIndx = 1:cam.width*cam.height;
#        clIndx = [];
#        i = 1;
#        while( i <= length(cl1Indx) )
#            
#            j = 1;
#            while( j <= length(cl2Indx) )
#            
#                interIndx = intersect(cl1Indx{i}, cl2Indx{j});
#                clIndx = [clIndx {interIndx}];
#                
#                restIndx(interIndx) = 0;
#                
#                j = j+1;
#                
#            end
#            
#            i = i+1;
#            
#        end
#        
#        clusterIndx = clIndx;
#        clusters = [];
#        
#        i = 1;
#        while( i <= length(clIndx) )
#            
#            clusters = [clusters {fr.points3D(1:3, clIndx{i})}];
#            
#            i = i+1;
#            
#        end
#        
#        restIndx(find(restIndx == 0)) = [];
#        restIndx = intersect(restIndx, fr.usage);
#        rest = fr.points3D(1:3, restIndx);
#        
#        show_clusters(clusters);
        
    else:
        np.disp('Error: Unknown clustering method! Please choose between the regions or the normals method');





#    if(display):
#        fig = figure;
#        fig = show_clusters(clusters, 0, fig, [], [], 1);
#        if(~isempty(rest))
#                fig = plot_3Dpoints(rest, 'k', fig, 0.3);
#        end
#    end
    
    inCl = clusters;
    inClIndx = clusterIndx;
    

    l = np.size(clusters, 2) #l = cellfun('size', clusters, 2);
    lo = np.nonzero((l < minSize)) #lo = find(l < minSize);
    rest = [rest, np.concatenate(clusters(lo), axis=2)] #rest = [rest cat(2, clusters{lo})];
    restIndx = [restIndx, np.concatenate(clusterIndx(lo), axis=2)] #restIndx = [restIndx cat(2, clusterIndx{lo})];
    temp=[]
    for it in range(len(lo)):  #    inCl(lo) = np.array([])
        inCl[it]=np.array([])

    for it in range(len(lo)):  #    inClIndx(lo) = np.array([])
        inClIndx[it]=np.array([])

    
    planesIndx = inClIndx
    
    ## refining the extracted planar cluster using RANSAC
    np.disp('Refining the extracted planar cluster using RANSAC');
    
    planes = [];
    i = 1;
    while i <= len(inCl):
        if planesIndx(i).size== 0:
            i = i+1;
        
        frame = fr;
        frame.usage = planesIndx(i);
        
        #[p, r, rIndx] = plane_segmentation(inCl{i},planesIndx{i});
        [cl, clIndx, p, r, rIndx] = pnts2plane_classification_RANSAC(frame, cam); 
        if p.size== 0 :
            rest = [rest. r];
            restIndx = [restIndx. rIndx];
            i = i+1;

        l = np.size(p.pnts, 2) #l = cellfun('size', {p.pnts}, 2);
        li = np.nonzero(l >= minSize);
        lo = np.nonzero(l < minSize);
        
        planes = [planes, p(li)];
        rest = [rest, r, [p(lo).pnts]];
        restIndx = [restIndx, rIndx, [p(lo).indx]];
         
        i = i+1;
        
    
    ## assign plane-id
    i=1
    while i<= len(planes) : 
        planes(i).id = i 
        i = i+1 

    
    ## displaying planes
    #if(display):
    #    fig = figure
    #    fig = show_clusters({planes.pnts}, 0, fig, [], [], 1)
    #    if(~isempty(rest)):
    #        fig = plot_3Dpoints(rest, 'k', fig, 0.3);
    #    end
    return frame