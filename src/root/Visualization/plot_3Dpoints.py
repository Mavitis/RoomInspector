
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def plot_3Dpoints(pnts=None, color=None, fig=None, msize=None, marker=None, values=None):

    #% fig = plot_3Dpoints(pnts, color, fig, msize)
    #         -              -
    #        |p11 p21 p31     |
    # pnts = |p12 p22 p32 ... |
    #        |p13 p23 p33     |
    #         -              -
    #
    # color: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'jet', 'copper', 'bone'
    #
    # fig: handle for a specific figure
    #
    # msize: size of the marker of the 3D points

    if (nargin < 2):
        color = mstring('jet')
        end

        if (nargin < 3 or isempty(fig)):
            fig = figure
            axis("equal")

            set(fig, mstring('Name'), mstring('3D point cloud'))
        else:
            fig = figure(fig)
            axis(mstring('equal'))
            end

            if (nargin < 4 or isempty(msize)):
                msize = 4
                end

                if (nargin < 5):
                    marker = mstring('.')
                    end

                    if (nargin < 6):
                        values = pnts(3, mslice[:])
                        end

                        hold(mstring('on'))
                        axis(mstring('off'))
                        axis(mstring('equal'))

                        if (isempty(pnts)):
                            fig = figure(fig); print fig
                            return
                            end

                            X = pnts(1, mslice[:])
                            Y = pnts(2, mslice[:])
                            Z = -1 * pnts(3, mslice[:])
                            mi = min(values)
                            ma = max(values)

                            if (logical_or(strcmp(color, mstring('jet')), logical_or(strcmp(color, mstring('copper')), strcmp(color, mstring('bone'))))):

                                # whitebg('w');

                                #mi = 0;
                                #ma = 7500;

                                map = colormap(color)
                                if (strcmp(color, mstring('bone'))):
                                    map = map(mslice[end:-1:1], mslice[:])
                                    end

                                    steps = length(map) - 1
                                    range = (ma - mi)

                                    p = mcat([])
                                    i = 1
                                    tdown = mi
                                    tup = mi + i / steps * range
                                    while (i <= steps):


                                        p = find(values >= logical_and(tdown, values <= tup))
                                        plot3(X(p), Y(p), Z(p), marker, mstring('Color'), map(i, mslice[:]), mstring('MarkerSize'), msize)

                                        i = i + 1
                                        tdown = tup
                                        tup = mi + i / steps * range

                                        end

                                        p = find(values > tup)
                                        plot3(X(p), Y(p), Z(p), marker, mstring('Color'), map(end, mslice[:]), mstring('MarkerSize'), msize)
                                        
    #nieskonwertowana czesc
    elseif(~isstr(color))
   
# whitebg('w');
if (size(color, 1) > 1):

    i = 1
    while (i <= size(pnts, 2)):
        plot3(X(i), Y(i), Z(i), marker, mstring('Color'), color(i, mslice[:]), mstring('MarkerSize'), msize)
        i = i + 1
        end
    
    else
        plot3(X,Y,Z, marker, 'Color', color, 'MarkerSize', msize);
    end
    
else

    % whitebg('w');

    plot3(X,Y,Z, [marker color], 'MarkerSize', msize);

end

figure(fig);
hold off;