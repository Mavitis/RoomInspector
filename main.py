import sys
'''
Created on Oct 16, 2017

@author: mavitis
'''
from root.IO.load_sequence import load_sequence
from root.Preprocessing.preprocessing import preprocessing
from root.PlaneExtraction.extract_planes import extract_planes

if __name__ == '__main__':
    seq = load_sequence('kitchen/0', 'SR_176x144')
    seq = preprocessing(seq, 'all')
    
    class my_ext_plane:
        planes = []
        clusters = []
        rest = []
        restIndx = []
    
    ext_plane = my_ext_plane()
    minSize=50
    method='planarClsts'
    display = True


    for it in range(len(seq.frames)):
        fr_planes=extract_planes(seq.frames[it], seq.camType, minSize, method, display)
        print 'lol'
    
    sys.exit("Debug break")
    #ext_plane=[extract_planes(x, seq.camType, minSize, method, display) for x in seq.frames]
    #for i = 1:length(seq.frames)

    #fr_planes = extract_planes(seq.frames(i), seq.camType, minSize, method, display)

    #end
    # - zaimplementowac wywolanie, a potem ruszyc z modyfikacja extract plane
    
    pass