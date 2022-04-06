'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

Great Circle Distances between Cities on Earth

Written by Cole Bardin
Term:  Winter 2020-2021
'''
from math import pi, sqrt, sin, cos, atan2
import csv

def great_circle_distance(loc1,loc2,r=6371.0,units='degrees'):
    ''' 
        computes the great_circle_distance using the Vincenty formula
        loc1[0] is latitude of point 1 and loc1[1] is longitude of point 1
        loc2[0] is latitude of point 2 and loc2[1] is longitude of point 2
        r is the radius of the sphere (default is Earth's radius in km)
        units is 'degrees' by default; radians assumed if this is any other value
    '''
    if units == 'degrees':
        lat1 = (pi * loc1[0]) / 180
        long1 = (pi * loc1[1]) / 180
        lat2 = (pi * loc2[0]) / 180
        long2 = (pi * loc2[1]) / 180
    else:
       lat1 = loc1[0]
       long1 = loc1[1]
       lat2 = loc2[0]
       long2 = loc2[1]
    d = 0.0
    dtheta = lat2 - lat1

    d = r * atan2( (sqrt( (cos(long2)*sin(dtheta))**(2.0) + (cos(long1)*sin(long2) - sin(long1)*cos(long2)*cos(dtheta))**(2))) , (sin(long1)*sin(long2) + cos(long1)*cos(long2)*cos(dtheta)))
    return d
def main():
    ''' Grab name of CSV input file from input '''
    csvinput = input('Enter name of CSV file containing name and coordinates of selected cities:\n')
    ''' Read the reference location name and coordinates from input; convert coordinates to floats and store in a tuple '''
    my_city, my_lat_string, my_long_string = input('Enter a city name, its latitude (deg), and longitude (deg), separated by commas:\n').split(',')
    my_loc = (float(my_lat_string),float(my_long_string))

    ''' Read the CSV file into a dictionary '''
    input_cities_dict = {}
    with open(csvinput) as csvfile:
        citiesreader = csv.reader(csvfile)
        for row in citiesreader:
            input_cities_dict[row[0]]=(float(row[1]),float(row[2]))

    ''' Your code goes here '''
    for key, value in input_cities_dict.items():
        print('{}->{}: {:.2f} km'.format(my_city,key,great_circle_distance(my_loc,value)))


''' Do not edit this block '''
if __name__ == '__main__':
    main()
