import numpy as np
import scipy
import matcompat
import sys
import csv

def pnts2plane_classification_rgrow(fr=None, cam=None, display=0):
    np.disp('Trwa wykonywanie: pnts2plane_classification_rgrow')
    
    #% [planes, rest, patchesIndx, restIndx] = pnts2plane_classification_rgrow(fr, cam, display)
    #
    #   This function classifies points as planar or not. Afterwards the planar
    #   points are associated with a certain plane. The function is based on the
    #   paper "Geometry and Texture Recovery" of Stamos and Allen. This function
    #   does take into account the neighborhood (based on the organization
    #   within the matrix structure) of each point. Use of region growing
    #   techniques.
    #
    # pnts: set of points with the following structure
    #           | p1x p2x p3x p4x     |
    #    pnts = | p1y p2y p3y p4y ... |
    #           | p1z p2z p3z p4z     |
    # width, height: dimension of the matrix the points of 'pnts' are organized in
    # usage: specifies which of the points in 'pnts' are valid points
    # display: 1 - visualize clusters; 0 - no visulaization (optinal; default: 0)

    #% some default values:


    #doda seq jako parametr? to jest zabezpieczenie przed niewykonaniem preprocessingu, wiec mozna wstepnie olac
    #if not(hasattr(fr, 'indx8')):
    #    seq.frames = fr
    #    seq.camType = cam

    #    seq = preprocessing(seq, 'normals')
    #    fr = seq.frames
     #   end

    rest = []
    restIndx = []
    with open('fr', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(fr)
    
    normals = fr.normals
    #deviation = fr.dev;
    usage = fr.usage
    pnts = fr.points3D
    planarIndx = fr.planar
    planar = fr.planar
    restIndx = fr.notplanar
    
    temp=np.zeros((3, len(restIndx)))
    for it in range(0,3):
        for it2 in range(len(restIndx)):
            temp[it][it2]=pnts[it][restIndx[it2]-1]
                #temp.append(pnts[it][ngbIndx[it2]])
        
    rest=temp
    
    
    #rest = pnts((1,3), restIndx)

        #% start region growing:

    patchesIndx = []
    patches = []
    workingIndx=[]
    i = 1
    #print planarIndx[0]
    #print len(planarIndx[0])
    #planarIndx=planarIndx[0]
    
    
    for x in np.nditer(planarIndx):
    #while (not len(planarIndx)==0):
        
        workingIndx.append(planarIndx[x])
        #        temp=[]
        #for it in range(len(ngbIndx)):
        #    if u[it] == 1:
        #        temp.append(ngbIndx[it])
        


        #patchesIndx[i].lvalue = [] czy ok???

        for y in np.nditer(workingIndx):

            currIndx = workingIndx[0][y]
            #print 'cuurind', currIndx
            #workingIndx(y).lvalue = [] czy ok???
            patchesIndx.append(currIndx)

            # find indices of neighbors
            #ngbIndx = getNgbIndx(currIndx, width, height, 3); %Swissranger: 8-neighboorhood
            #ngbIndx = getNgbIndx(currIndx, width, height, 21); %DC_Tracking: 440-neighboorhood
            ngbIndx = fr.indx8[currIndx] # jfr.indx8 zupelnie inna wartosc, sasiedztwo 8 nie dziala
            print 'ngbIndx po sasiedztwie',ngbIndx #podaje sama siebie + os X iY zmienione
            np.savetxt('ngbIndxPNTS.txt', ngbIndx, delimiter='\n', newline='\n')
            #print 'fr.indx8',fr.indx8
            np.savetxt('fr.indx8PNTS.txt', fr.indx8[currIndx], delimiter='\n', newline='\n')
            
            # find the indices, that are unprocessed until now and refer to a planar
            # point (-> stored in 'planar')
            #ngbIndx = ngbIndx(ismember(ngbIndx, usage));
            
            
            #ngbIndx=ngbIndx[np.in1d(ngbIndx, planar)]
            u = np.in1d(ngbIndx, planar)
            u = u*1
            print 'u',u
            temp=[]
            for it in range(len(ngbIndx)):
                if u[it] == 1:
                    temp.append(ngbIndx[it])
            
            ngbIndx=temp
            
            print 'ngbIndx po planar',ngbIndx 
            
            
            
            

            if (len(ngbIndx)==0): #czy to ma sens? chyba trzeba while albo cos 
                continue
                
            
            np.savetxt('ngbIndx.txt', ngbIndx, delimiter=' ', newline='    ')
            # conormality measure:
            
            
            print 'ngbIndx' ,ngbIndx
            print 'normals.size' ,normals.shape[0]
            
            ngbNormals=np.zeros((normals.shape[0], len(ngbIndx)))
            #ngbNormals = normals[:, ngbIndx]
            
            for it in range(normals.shape[0]):
                for it2 in range(len(ngbIndx)):
                    ngbNormals[it][it2]=normals[it][ngbIndx[it2]]
            #ngbNormals=temp      
            
            currNormal = normals[:, currIndx]
            
            #print ngbNormals.shape
            print ngbNormals
            np.savetxt('currNormal.txt', currNormal, delimiter=' ', newline='    ')
            np.savetxt('ngbNormals[0].txt', ngbNormals[0], delimiter=' ', newline='    ')
            
            sys.exit("Debug break")
            print currNormal.conj().T
            angles = np.arccos(currNormal.conj().T * ngbNormals)
            # find acute angles
            f = np.nonzero((angles > (np.pi / 2)))[0]
            angles(f).lvalue = np.pi - angles(f)
            _in = np.nonzero((angles < (1 / 18 * np.pi)))[0]
            ngbIndx = ngbIndx(_in)
            
            
            
            if (len(ngbIndx)==0):
                continue

            # coplanarity measure:
        
            currPnt = pnts((0,3), currIndx)
            ngbPnts = pnts((0,3), ngbIndx)
            ngbNormals = normals[:, ngbIndx]

            r12 = ngbPnts - currPnt * np.ones((1, len(ngbPnts[2])))

            firstTerm = abs(currNormal.conj().T * r12)
            secondTerm = np.zeros(1, len(r12[2]))
            for j in len(r12[2]):
                secondTerm[j] = abs(ngbNormals[:, j] * r12[:, j])
                
                
            decider = max(firstTerm, secondTerm)
            #threshold = log(10*currPnt(3));
            #threshold = 32 * 0.05 * currPnt(3); %Swissranger
            threshold = 4 * 0.05 * currPnt(3)                            #Swissranger
            #threshold = 100; %DC_Tracking
            #threshold = 30;
            _in = np.nonzero(decider < threshold)
            

            ngbIndx = ngbIndx(_in)
            
            workingIndx = (workingIndx, ngbIndx)
            workingIndx = np.unique(workingIndx)
            workingIndx(np.in1d(workingIndx, patchesIndx(i))).lvalue = []

        

        #patches(i).lvalue = pnts([1:3], patchesIndx(i))
        patches(i).lvalue = pnts((0,3), patchesIndx(i))
        
        #planarIndx(ismember(planarIndx, patchesIndx(i))) = []     u = np.in1d(fr.usage[1], use[1])   
        w = np.in1d(planarIndx, patchesIndx(i))
        planarIndx(w).lvalue = []
        

        i = i + 1


    #% display results:

    #if (display):
    #    fig = show_clusters(patches, 50)
    #    fig = plot_3Dpoints(rest, mstring('k'), fig)
        

    planes = patches
    
    #return [clusters, rest, clusterIndx, restIndx]