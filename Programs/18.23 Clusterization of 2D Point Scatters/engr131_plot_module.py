'''
D R E X E L   U N I V E R S I T Y
ENGR 131 Winter 2020-2021
Programming Project 2
Clusterization of 2D data:  Plot module

DO NOT EDIT THIS SCRIPT!

Use it by invoking

from engr131_plot_module import make_scatter_plot

in your script. Then you can call make_scatter_plot() to make a plot!

Cameron F Abrams cfa22@drexel.edu
'''
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as patches
# get_center() computes the geometric center of all
#    points in list S[] having cluster index i
# a point must have instance attributes 'x' and 'y'
def get_center(S,i):
    n=0
    cx=0
    cy=0
    for p in S:
        if p.c==i:
            cx+=p.x
            cy+=p.y
            n+=1
    cx/=n
    cy/=n
    return cx, cy

def get_max_radius(S,i):
    cx,cy = get_center(S,i)
    maxd = -9
    for p in S:
        if p.c == i:
            d = ((cx-p.x)**2+(cy-p.y)**2)**0.5
            if d > maxd:
                maxd=d
    return maxd

def make_scatter_plot(S,fn='my_plot.png',thresh=5.0,nc=0,include_labels=True,circle_clusters=True):
    # Generate a plot of scattered point data with
    # cluster attributes
    #
    # Parameters:
    # S   a list of 2D point class instances 
    #     with position attributes x and y, and 
    #     cluster index attribute 'c'
    # thresh: the distance threshhold used in clusterization
    # nc:  number of unique clusters
    # include_labels: plot will include numerical labels for each cluster
    # circle_clusters:  plot will include circles around each cluster
    
    color_map=cm.get_cmap('inferno')
    fig, ax = plt.subplots(figsize=(5,5))
    plt.xlim([-120, 120])
    plt.ylim([-120, 120])
    plt.xlabel('x')
    plt.ylabel('y')
    X = [p.x for p in S]
    Y = [p.y for p in S]
    # get a set of unique cluster indices
    ci = list(set([p.c for p in S]))
    # make a list of colors from the color_map
    c = [color_map((ci.index(p.c)+1)/(nc+2)) for p in S]
    plt.scatter(X, Y, c=c, s=1)
    # add cluster labels and circles
    if include_labels or circle_clusters:
        for i in ci:
            ccx, ccy = get_center(S, i)
            maxr = get_max_radius(S, i)
            if include_labels:
                plt.text(ccx+maxr*2**0.5/2, ccy+maxr*2**0.5/2, str(i), color=color_map(ci.index(i)/(nc+2)))
            if circle_clusters:
                ax.add_patch(patches.Circle((ccx,ccy),maxr+3,facecolor='none',
                    edgecolor=color_map(ci.index(i)/(nc+2)), linewidth=3, alpha=0.5))
    plt.savefig(fn, bbox_inches='tight')
    plt.close()