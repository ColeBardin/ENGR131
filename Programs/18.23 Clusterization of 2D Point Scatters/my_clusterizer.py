from math import sqrt
from engr131_plot_module import make_scatter_plot

class pt2d:
    def __init__(self, x=0, y=0, c=0):
        self.x = float(x)
        self.y = float(y)
        self.c = int(c)
    
    def distance(self,other):
        return sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )
    
    def in_same_cluster(self,other):
        if self.c == other.c:
            return True
        elif self.c != other.c:
            return False
    
def merge_clusters(point_list, point_i, point_j):
    j = point_j.c 
    i = point_i.c
    for point in point_list:
        if point.c == j:
            point.c = i

def clusterize(point_list=[], thresh = 5):
    N = len(point_list)
    no_dups = []
    for i in range(N):
        point_list[i].c = i
    all_clustered = False
    while all_clustered == False:
        for i in range(N):
            for j in range((i+1),N):
                if point_list[i].in_same_cluster(point_list[j]) == False:
                    if point_list[i].distance(point_list[j]) <= thresh:
                        merge_clusters(point_list, point_list[i], point_list[j])
        all_clustered = True
    for g in point_list:
        if g.c not in no_dups:
            no_dups.append(g.c)
    for k in range(len(no_dups)):
        for pt in point_list:
            if pt.c == no_dups[k]:
                pt.c = k
    return len(no_dups)

if __name__ == "__main__":
    data_file_name = input()
    thresh_val = float(input())
    plot_name = input()
    list_o_points = []
    class_points_list = []

    with open(data_file_name, 'r') as f:
        lines = f.readlines()
        for ln in lines:
            list_o_points.append(ln.split(','))
        for point in list_o_points:
            pt = point
            pt = pt2d()
            pt.x = float(point[0])
            pt.y = float(point[1])
            class_points_list.append(pt)

    num_clusters = clusterize(point_list = class_points_list, thresh = thresh_val)
    make_scatter_plot(class_points_list, plot_name, thresh_val, num_clusters)
    print('{} at threshhold {:.2f} has {} clusters.\nPlot appears in {}'.format(data_file_name, thresh_val, num_clusters, plot_name))
