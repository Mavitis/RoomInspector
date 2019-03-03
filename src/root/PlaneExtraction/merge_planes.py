
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def merge_planes(planes, method):

    # Local Variables: distances, currMin, decider, allMins, posEnd, disDecider, allMean, rest, candMins, radius, in, allNormPnts, absoluteNum, radiusDecider, nCurr, cNormPnts, nEnd, currAllMins, pnts, candidates, workingPlanes, dEnd, method, currPlane, allRadius, disCand, currCells, allDistMean, plane, allPlanes, currMean, angles, surCand, restIndx, currRadius, d, currSet, planesNew, cAllMins, indx, n, i, points, emp, planes, y, x
    # Function calls: disp, false, repmat, mat2cell, any, size, main_plane_extraction, merge_planes, min, sum, sqrt, find, realmax, pi, max, isfield, ones, isempty, median, length, cellfun, acos, strcmp, mean
    #%% planesNew = merge_planes(planes, method)
    #%
    #% approach based on region growing
    #%
    #% possible methods:
    #%  - 'mean': uses the mean of the patches
    #%  - 'median': uses the median of the patches
    #%  - 'ngbPatches': uses the nearest neighbor patches
    #%  - 'fastNgbPatches': finds quick nearest neighbor patches 
    emp = cellfun('isempty', cellarray(np.hstack((planes.pnts))))
    allPlanes = planes[int((not emp))-1]
    planesNew = np.array([])
    rest = np.array([])
    restIndx = np.array([])
    absoluteNum = length(allPlanes)
    while not isempty(allPlanes):
        #%progressbar(1 - length(allPlanes) / absoluteNum);
        
    #%progressbar(1);
    #% planesNew = [];
    #% plane = struct('pnts', [], 'n', [], 'd', 0);
    #% 
    #% currSet = [];
    #% 
    #% while(~isempty(planes))
    #%     
    #%     currSet = [];
    #%     workingPlanes = planes(1);
    #%     planes(1) = [];
    #%     
    #%     while(~isempty(workingPlanes))
    #%         
    #%         currPlane = workingPlanes(1);
    #%         currSet = [currSet currPlane.pnts];
    #%         workingPlanes(1) = [];
    #%         
    #%         if(isempty(planes))
    #%             continue;
    #%         end
    #%         
    #%         % conormality measure:
    #%         angles = acos(currPlane.n'*[planes.n]);
    #%         
    #%         % coplanarity measure:
    #%         % currMean = mean(currPlane.pnts, 2);
    #%         % planesMean = arrayfun(@(x)mean(x.pnts,2), planes, 'UniformOutput', false);
    #%         % planesMean= cell2mat(planesMean);
    #% %         currN = size(currPlane.pnts, 2);
    #% %         l = 1;
    #% %         while(l <= currN)
    #% %             
    #% %             planesCurrR12 = arrayfun(@(x)(x.pnts - repmat(currPlane.pnts(1:3,l), 1, size(x.pnts,2))), planes, 'UniformOutput', false);
    #% %             
    #% %             l = l+1;
    #% %             
    #% %         end
    #% 
    #%         r12 = zeros(3, length(planes));
    #% 
    #%         l = 1;        
    #%         while(l <= length(planes))
    #%             
    #%             k = 1;
    #%             currR12 = [];
    #%             currLength = realmax;
    #%             while(k <= size(currPlane.pnts, 2))
    #%                 
    #%                 helpR12 = planes(l).pnts - repmat(currPlane.pnts(1:3,k), 1, size(planes(l).pnts, 2));
    #%                 helpLengths = sum(helpR12.^2);
    #%                 [mi, indx] = min(helpLengths);
    #%                 
    #%                 if(mi < currLength)
    #%                     currR12 = helpR12(:, indx);
    #%                     currLength = mi;
    #%                 end
    #%                 
    #%                 k = k+1;
    #%                 
    #%             end
    #%             
    #%             r12(:,l) = currR12;
    #%             
    #%             l = l+1;
    #%             
    #%         end
    #% 
    #%         % r12 = planesMean - repmat(currMean, 1, size(planesMean, 2));
    #%         
    #%         firstTerm = abs(currPlane.n'*r12);
    #%         secondTerm = zeros(1, size(r12, 2));
    #%         for j = 1:size(r12, 2)
    #%             secondTerm(j) = abs(planes(j).n'*r12(:,j));
    #%         end
    #%         
    #%         decider = max([firstTerm; secondTerm]);
    #%         %threshold = 8 * 0.005 * currMean(3);
    #%         threshold = 30;
    #%         in = find(angles < (2/18 * pi) & decider < threshold);
    #%         
    #% %         ds = abs([planes.d] - currPlane.d);
    #% %         in = find(angles < (2/18 * pi) & ds < 40);
    #%         
    #%         workingPlanes = [workingPlanes planes(in)];
    #%         planes(in) = [];
    #%         
    #%     end
    #%     
    #%     plane.pnts = currSet;
    #%     coeff = princomp(currSet');
    #%     plane.n = coeff(:,3);
    #%     plane.d = plane.n' * mean(currSet, 2);
    #%     
    #%     planesNew = [planesNew plane];
    #%     
    #% end
    return [planesNew, rest, restIndx]