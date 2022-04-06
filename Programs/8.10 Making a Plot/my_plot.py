'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

A simple plotting program that saves an image of a plot

Written by Cole Bardin
Term:  Winter 2020-2021
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,4*np.pi,80)
sinx = np.sin(x)

plt.plot(x,sinx,'-b')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.axis([0, 4*np.pi, -1.00, 1.00])
plt.savefig('my_plot.tif') #Submitted with this to save plot as file
#plt.show() #Use this to show plot

#