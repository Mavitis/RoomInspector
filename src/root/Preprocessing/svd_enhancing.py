import numpy as np
import scipy
import matcompat
from backprojection_fast import backprojection_fast

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def svd_enhancing(fr, camType):

    # Local Variables: disNew, fr, distances, camType, gdach, Sdach, pos, neri, S, U, V, frame, neriG
    # Function calls: max, gradient, reshape, svd, abs, zeros, diag, backprojection_fast, find, svd_enhancing, mean
    #%% frame = svd_enhancing(fr, camType)
    #%
    #% This function is based on the paper:
    #% "SwissRanger SR-3000 Range Images Enhancement by a Singular Value
    #% Decomposition Filter"
    #% from
    #% GuruPrasad M. Hedge and Cang Ye
    #%
    #% problem: normals needed to be computed => time consuming
    #%% build NERI image (Normal-Enhanced Range Image)
    neri = np.zeros((camType.height), (camType.width), 3.)
    neri[:,:,0] = np.reshape((fr.normals[0,:]), (camType.width), np.array([])).conj().T
    neri[:,:,1] = np.reshape((fr.normals[1,:]), (camType.width), np.array([])).conj().T
    neri[:,:,2] = np.reshape((fr.distances), (camType.width), np.array([])).conj().T
    neriG = np.mean(neri, 3.)
    #%% decompose NERI image and determine appropiate threshold
    [U, S, V] = plt.svd(neriG)
    Sdach = np.diag(S)/max(np.diag(S))
    gdach = np.abs(np.gradient(Sdach))
    pos = np.nonzero((gdach<0.001))
    S[int(pos[0])-1:,int(pos[0])-1:] = 0.
    #%% compose new image
    disNew = np.dot(np.dot(U, S), V.conj().T)
    frame = fr
    frame.distances = np.reshape(disNew.conj().T, 1., np.array([]))
    frame = backprojection_fast(frame, camType)
    return frame