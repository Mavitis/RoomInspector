
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def show_clusters(clusters, minSize= 0, fig, method='points', s=[], p=0, marker='.', cMap):

    # Local Variables: map, i, lo, K, l, rest, minSize, p, s, cMap, fig, X, in, marker, clusters, perm, method, ls
    # Function calls: disp, plot_3Dpoints, repmat, false, figure, trisurf, randperm, find, convhulln, nargin, length, abs, isempty, cellfun, input, show_clusters, cat, generate_colormap, strcmp, size
    #% fig = show_clusters(clusters, minSize, fig, method, s, p, marker, cMap)
    #% 
    #% methods: -'points'; 'convexhull'
    
    
    
    #do testu co to
    #axis("off")
    #axis("equal")


    #if (nargin < 3 or isempty(fig)):
    #    #fig = figure('Position', [1 1 600 600]);
    #    fig = figure
    #else:
    #    fig = figure(fig)
    #    end


    if (logical_and(strcmp(method, mstring('convexhull')), isempty(s))):
        s = input(mstring('Specific color for all hulls? \\n [default: press enter - each hull gets an other color]\\n'))
        end

        rest = []
        _in = clusters
        l = np.size(clusters, 2)#l = cellfun(mstring('size'), clusters, 2)
        
        #[ls, li] = sort(l, 'descend');
        #in = in(li);
        ls = l
        lo = np.nonzero((ls<minSize))#lo = find(ls < minSize)
        

        if lo.size!= 0: #if (not isempty(lo)):
            rest = cat(2, clusters(lo))
            

            _in(lo).lvalue = mcat([])

            if (nargin > 7):
                map = cMap
            else:
                map = generate_colormap(length(_in))
                map = abs(map)
                map(find(map > 1)).lvalue = 1
                end

                if (p):
                    perm = randperm(length(_in))
                    _in = _in(perm)
                    end

                    i = 1
                    while (i <= length(_in)):

                        if (strcmp(method, mstring('points'))):
                            fig = plot_3Dpoints(_in(i), map(i, mslice[:]), fig, 6, marker)
                        elif (strcmp(method, mstring('convexhull'))):
                            hold("on")
                            X = _in(i).cT
                            K = convhulln(X(mslice[:], mslice[1:3]))

                            if (isempty(s)):
                                trisurf(K, X(mslice[:], 1), X(mslice[:], 2), -X(mslice[:], 3), repmat(mcat([i]), 1, size(K, 1)), mstring('FaceAlpha'), 0.5)
                            else:
                                trisurf(K, X(mslice[:], 1), X(mslice[:], 2), -X(mslice[:], 3), mstring('FaceAlpha'), 0.5, mstring('FaceColor'), map(i, mslice[:]))
                                end

                            else:
                                disp(mstring('Error: unknown display method!'))
                                end

                                i = i + 1

                                end

                                if (p):
                                    map = map(perm, mslice[:])
                                    end

                                    if (not isempty(rest)):
                                        fig = plot_3Dpoints(rest, mstring('k'), fig)
                                        end



    return [fig, map]