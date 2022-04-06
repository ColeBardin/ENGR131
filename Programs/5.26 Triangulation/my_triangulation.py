'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

Programming Assignment 1

Written by: Cole Bardin
Term:  Winter 2020-2021
'''
from math import sqrt

def triangulate ( point1, point2, point3, dist1, dist2 ):
    unknown_point = ( None, None )
    
    #defining x1,y1 and x2,y2 and x3,y3
    x1 = float(point1[0])
    y1 = float(point1[1])
    x2 = float(point2[0])
    y2 = float(point2[1])
    x3 = float(point3[0])
    y3 = float(point3[1])

    #define values a and b from equation sheet
    a = (((dist1*dist1) - (dist2*dist2) - ((x1*x1 + y1*y1) - (x2*x2 + y2*y2)))/(2 * (y2-y1)))
    b = (-1.0) * ((x2 - x1)/(y2-y1))
    
    #recreating the x equation used local variables
    c = 1.0 / (2.0 * (1.0 + b*b))
    d = x1 - b * (a - y1)
    e = (b * (a - y1)) - x1
    f = 1.0 + b * b
    g = x1*x1 - dist1*dist1 + (y1 - a)*(y1 - a)

    #find x and y value using + for the +-
    #unknown point (xp, yp)
    xp = c * (2.0*d + sqrt(4.0 * e * e - 4.0*f*g))
    yp = (a + b * xp)
    
    #find x and y value using - for +-
    #unkown point (xn,yn)
    xn = c * (2.0*d - sqrt(4.0 * e * e - 4.0*f*g))
    yn = (a + b * xn)

    #find distance from third point to (xp,yp)
    dist3p = sqrt((x3 - xp)*(x3 - xp) + (y3 - yp)*(y3 - yp))
    
    #find distance from third point to (xn,yn)
    dist3n = sqrt((x3 - xn)*(x3 - xn) + (y3 - yn)*(y3 - yn))
    
    #choosing closest unknown point
    if dist3p > dist3n:
        unknown_point = (xn,yn)
    elif dist3p < dist3n:
        unknown_point = (xp,yp)
    elif dist3p == dist3n:
        unknown_point = 0
    return unknown_point
   
if __name__ == '__main__':
    point1 = (-5.0,-3.0)
    point2 = (3.0,6.0)
    point3 = (8.5,-4.0)
    dist1 = 11.5
    dist2 = 13
    ukp = triangulate(point1,point2,point3,dist1,dist2)
    if len(ukp)==0:
        print('No solution found.')
    else:
        print('Unknown point located at {0[0]:.2f},{0[1]:.2f}'.format(ukp))
        
