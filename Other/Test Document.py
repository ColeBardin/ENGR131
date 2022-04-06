import math
import matplotlib.pyplot as plt

def x(t):
    return x0 + v0*t*cos(theta)

def y(t):
    return y0 + v0*t*math.sin(theta) - 32.174*0.5*t**2

if __name__ == "__main__":
    draw()
    throw_ball()
    plt.show()
