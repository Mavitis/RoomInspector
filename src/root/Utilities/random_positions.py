
import numpy as np
import scipy
import matcompat
import random


# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def random_positions(numOfPos, maxNum):

    # Local Variables: l, c, maxNum, pos, numOfPos
    # Function calls: rand, random_positions, find, length, unique, round
    #% pos random_positions(numOfPos, maxNum)
    np.disp(('Trwa wykonywanie: random_positions(numOfPos, maxNum)'))

    pos = []
    while(len(pos) < numOfPos):
        l = len(pos)
        c = 1
        while(c <= (numOfPos-l)):
            pos.append(round(random.uniform(0, 1)*maxNum))
            c=c+1
            
        pos = np.unique(pos);
        np.delete(pos,0) #pos(find(pos == 0)) = []; - po co?
        #pos(find(pos > maxNum)) = [];-po co? 
    
    
    
    return pos