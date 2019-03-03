
import numpy as np
import scipy
import matcompat
import scipy.special
from root.Utilities.get_angle import get_angle

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def compute_feature(planes, method):

    # Local Variables: ahist, arhist, means, histopt, arearatio, shaphist, shapes, anghist, angles, planes, var, x, comb, feat, method, areas
    # Function calls: cell2mat, compute_feature, false, arrayfun, nchoosek, max, sum, min, length, ones, zeros, get_angle, exp, cellfun, realmax, histc, pi, mat2cell, strcmp, size
    #%% feat = compute_feature(planes, method)
    #%% histopt determines whether a data point contributes to its neighboring
    #% bins or not
    histopt = 'hard'
    #% histopt = 'smooth';
    feat = np.array([])
    if len(planes) == 1.:
        return []
    
    
    comb = scipy.special.binom(np.arange(1, (len(planes))+1), 2)
    comb=np.reshape(comb, (1,np.size(comb,1),2)) #comb = mat2cell(comb, np.ones(1., matcompat.size(comb, 1.)), 2.)
   
    
    
    angles = []
    
    #%% angles between all planes
   
    if method == 'angles' or method == 'all':
         #angles = cell2mat(cellfun(lambda x: get_angle((planes[x[0]].n), (planes[int(x[1])-1].n)), comb, 'UniformOutput', false)).conj().T
        for x in np.nditer(comb): 
            angles[x]=get_angle((planes[x[0]].n), (planes[x[1]].n)) 
        
        angles=angles.conj().T
        
        #np.arange cell2mat!
        if histopt =='hard':
            anghist = np.digitize(angles, np.array(np.hstack((np.arange(0., (np.pi/2.)+(np.pi/18.), np.pi/18.)))))
            anghist = anghist[0:0-1.]/np.sum(anghist)
        
        
        if histopt =='smooth':
            means = np.arange(np.pi/36., (np.pi/2.)+(np.pi/18.), np.pi/18.)
            var = np.pi/18.
            
            #anghist = cell2mat(arrayfun(lambda x: np.sum(np.exp(np.dot(-0.5, matdiv(angles-x, var)**2.))), means, 'UniformOutput', false))
            for x in np.nditer(means): 
                anghist[x]=np.sum(np.exp(-0.5* (angles-x/var)**2))
            
            
            anghist = anghist/np.sum(anghist)
        
        
        feat = np.array(np.vstack((np.hstack((feat)), np.hstack((anghist.conj().T)))))
    
    
    #%% shapes of the planes defined by ratio of the main axis
    if method=='shapes' or method=='all':
        shapes = np.array(np.hstack((planes.shape)))
        shaphist = np.array([])
        if histopt == 'hard':
            shaphist = np.digitize(shapes, np.array(np.hstack((np.arange(0., 1.2, 0.2)))))
            shaphist = shaphist[0:0-1.]/np.sum(shaphist)
        
        
        if histopt == 'smooth':
            means = np.arange(0.1, 1.2, 0.2)
            var = 0.2
            #shaphist = cell2mat(arrayfun(lambda x: np.sum(np.exp(np.dot(-0.5, matdiv(shapes-x, var)**2.))), means, 'UniformOutput', false))
            for x in np.nditer(means): 
                shaphist[x]=np.sum(np.exp(-0.5* (shapes-x/var)**2))
            
            shaphist = shaphist/np.sum(shaphist)
        
        
        feat = np.array(np.vstack((np.hstack((feat)), np.hstack((shaphist.conj().T)))))
    
    
    #%% ratio of the areas
    if method == 'arearatio' or method== 'all':
        
        arearatio=[]
        #arearatio = cell2mat(cellfun(lambda x: matdiv(matcompat.max((planes[int(x[0])-1].area), (planes[int(x[1])-1].area)), matcompat.max((planes[int(x[0])-1].area), (planes[int(x[1])-1].area))), comb, 'UniformOutput', false)).conj().T
        for x in np.nditer(comb): 
            arearatio[x]=np.min(planes[x[0].area], planes[x[1].area]) / np.max(planes(x[0].area, planes(x[1].area)))
        
        
        arhist = np.zeros(1., (len(np.array(np.hstack((np.arange(0., 1.2, 0.2)))))-1.))
        if histopt == 'hard':
            arhist = np.digitize(arearatio, np.array(np.hstack((np.arange(0., 1.2, 0.2))))) #        arhist = histc(arearatio, [0:0.2:1]);
            arhist = arhist[0:0-1.]/np.sum(arhist)
        
        
        if histopt == 'smooth':
            means = np.arange(0.1, 1.2, 0.2)
            var = 0.2
            #arhist = cell2mat(arrayfun(lambda x: np.sum(np.exp(np.dot(-0.5, matdiv(arearatio-x, var)**2.))), means, 'UniformOutput', false))
            for x in np.nditer(means): 
                arhist[x]=np.sum(np.exp(-0.5* (arearatio-x/var)**2))      
            
            arhist = arhist/np.sum(arhist)
        
        
        feat = np.array(np.vstack((np.hstack((feat)), np.hstack((arhist.conj().T)))))
    
    
    if method== 'areas' or method== 'all':
        areas = np.array(np.hstack((planes.area)))
        ahist = np.digitize(areas, np.array(np.hstack((0, (np.array(np.hstack((0.25, 0.5, np.arange(1, 4.0))))*1000)**2))))
        ahist = ahist[0:0-1]/np.sum(ahist)
        feat = np.array(np.vstack((np.hstack((feat)), np.hstack((ahist.conj().T)))))
    
    
    return [feat]