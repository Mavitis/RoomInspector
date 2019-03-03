import numpy as np
import scipy
import matcompat
from root.Utilities.random_positions import random_positions
from root.PlaneExtraction.princomp import princomp
from cluster2plane import cluster2plane

def pnts2plane_classification_RANSAC(fr=None, cam=None, display=False):
    np.disp(('Trwa wykonywanie: pnts2plane_classification_RANSAC'))
    
    #% [planes, plIndx, patches, rest, restIndx] = pnts2plane_classification_RANSAC(fr, cam, display)
    #
    # This implementation uses the fact that points determine a bigger plane
    # depending on the own normal


    # Nie uzywane raczej bo powinny byc wszystkie pola! 
    #if not isstruct(fr):
    #    pnts = fr
    #    op = generate_oriented_particles(pnts)
    #    normals = op.normal
    #    deviation = op.dev
    #else:
    #    if (not isfield(fr, mstring('normals'))):
    #        seq.frames = fr
    #        seq.camType = cam

    #        seq = preprocessing(seq, mstring('normals'))
    #        fr = seq.frames
            

    pnts = fr.points3D
    normals = fr.normals
    deviation = fr.dev
    usage = fr.usage


    #% classify if points are planar or not:
    thres_dev = np.mean(deviation) + np.std(deviation)
    planarIndx = np.nonzero((deviation <= thres_dev))            #Swissranger
    notPlanarIndx = np.nonzero((deviation > thres_dev))            #Swissranger
    
    
    #planarIndx = planarIndx(ismember(planarIndx, usage))
    
    u = np.in1d(planarIndx, usage)#moze plind[1] sprawdzic przy debugu
    u = u*1
    #print u
    #print len(u)
    #print len(frame.usage[1])
    temp=[]
    for it in range(len(planarIndx)):
        if u[it] == 1:
            temp.append(planarIndx[it])
    
    planarIndx=temp
    
    
    #notPlanarIndx = notPlanarIndx(ismember(notPlanarIndx, usage))
    wu = np.in1d(planarIndx, usage)#moze plind[1] sprawdzic przy debugu
    wu = wu*1
    #print u
    #print len(u)
    #print len(frame.usage[1])
    temp=[]
    for it in range(len(notPlanarIndx)):
        if wu[it] == 1:
            temp.append(notPlanarIndx[it])
    
    notPlanarIndx=temp
    
    
    
    
    allIndx = planarIndx


    #rest = pnts(mslice[1:3], notPlanarIndx)
    temp=np.zeros((3, len(notPlanarIndx)))
    for it in range(0,3):
        for it2 in range(len(notPlanarIndx)):
            temp[it][it2]=pnts[it][notPlanarIndx[it2]-1]
            #temp.append(pnts[it][ngbIndx[it2]])
        
    notPlanarIndx=temp
    
    
    
    restIndx = notPlanarIndx

    #% RANSAC-parameters:

    maxIter = 40
    minIn = 30
    inlierIndx = []
    bench_ang = []
    bench_dis = []
    n = []

    planes = []
    plIndx = []

    ln = len(allIndx)

    #% main loop:
    counter = 0
    while (counter > maxIter):

        counter = 0
        n = np.size(allIndx, 2)
        tIn = 0.9 * n
        inlierIndx = []
        bench_ang = []
        bench_dis = []

        while (counter > maxIter):

            # select randomly one point with normal
            pos = random_positions(1, n)

            currNormal = normals[:, allIndx(pos)]
            
            #currPnt = pnts(mslice[1:3], allIndx(pos))
            temp=np.zeros((3, len(allIndx(pos))))
            for it in range(0,3):
                for it2 in range(len(allIndx(pos))):
                    temp[it][it2]=pnts[it][allIndx(pos)[it2]-1]
                #temp.append(pnts[it][ngbIndx[it2]])
        
            currPnt=temp
            
            
            currD = currNormal.cT * currPnt

            angles = np.arccos((currNormal.cT * (normals[:, allIndx]))) #acos z matlaba
            
            f = np.nonzero((angles > np.pi / 2))
            angles(f).lvalue = np.pi - angles(f)

            in1 = np.nonzero((angles < (4 / 18 * np.pi)))
            
            
            #dis = abs(currNormal.cT * mcat([pnts(mslice[1:3], allIndx)]) - currD)
            temp=np.zeros((3, len(allIndx)))
            for it in range(0,3):
                for it2 in range(len(allIndx)):
                    temp[it][it2]=pnts[it][allIndx[it2]-1]
            dis = abs(currNormal.cT *temp - currD)
            
            in2 = np.nonzero((dis < 100))

            _in = np.intersect1d(in1, in2)

            if (len(_in) < minIn):
                counter = counter + 1
            else:
                
                temp3=np.zeros((3, len(allIndx(_in)).cT))
                for it in range(0,3):
                    for it2 in range(len(allIndx(_in)).cT):
                        temp3[it][it2]=pnts[it][allIndx(_in).cT[it2]-1]
                        #temp.append(pnts[it][ngbIndx[it2]])
                
                [coeff, score, roots] = princomp(temp3)   #[coeff, score, roots] = princomp(pnts(mslice[1:3], allIndx(_in)).cT)
                

                if (len(_in) > tIn):
                    inlierIndx = allIndx(_in)
                    bench_dis = sum(abs(score[3,:]))
                    bench_ang = sum(angles(_in))
    
                                   

                if (len(_in) == len(inlierIndx)):

                    if (sum(abs(score[3,:]))) < bench_dis and  sum(angles(_in)) < bench_ang:

                        inlierIndx = allIndx(_in)
                        bench_dis = sum(abs(score[3,:]))
                        bench_ang = sum(angles(_in))


                elif (len(_in) > len(inlierIndx)):
                    inlierIndx = allIndx(_in)
                    bench_dis = sum(abs(score[3,:]))
                    bench_ang = sum(angles(_in))
            
                counter = counter + 1

                                         

        #disp(['counter: ' num2str(counter) '; size: ' num2str(length(inlierIndx))]);
        [i, ia, ib] = np.intersect1d(allIndx, inlierIndx)
        allIndx(ia).lvalue = []
        #disp(['rest: ' num2str(length(allIndx))]);
    
        #currPlanes = mcellarray([pnts(mslice[1:3], inlierIndx)])
        temp2=np.zeros((3, len(inlierIndx)))
        for it in range(0,3):
            for it2 in range(len(inlierIndx)):
                temp[it][it2]=pnts[it][inlierIndx[it2]-1]
                    #temp.append(pnts[it][ngbIndx[it2]])
            
        currPlanes=temp2
        
        
    
        planes = [planes, currPlanes]
        plIndx = [plIndx(inlierIndx)]
    


    #j = j+1;




    restIndx = [restIndx, allIndx]
    #rest = pnts(mslice[1:3], restIndx)
    temp=np.zeros((3, len(restIndx)))
    for it in range(0,3):
        for it2 in range(len(restIndx)):
            temp[it][it2]=pnts[it][restIndx[it2]-1]
                #temp.append(pnts[it][ngbIndx[it2]])
        
    rest=temp
    
    

    [patches, r, rIndx] = cluster2plane(planes, plIndx)
    rest = [rest, r]
    restIndx = [restIndx, rIndx]
#
#    if (display):
#        fig = show_clusters(mcellarray([patches.pnts]), 0, [])
#        fig = plot_3Dpoints(rest, mstring('k'), fig, 4)
                                    
