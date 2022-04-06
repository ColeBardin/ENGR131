# Assignment 1 - Go Drexel Dragons!!

import matplotlib.pyplot as plt
import math


def draw():
    # body of draw method.
    fig = plt.figure("Go Drexel Dragons!!")  # create a new figure

    # stickman player
    # add the legs
    x = [0, 0.5, 1, 2, 2]
    y = [0, 1.5,   3, 1.5, 0]
    plt.plot(x, y , 'red')

    # add the body and neck
    x = [1, 1]
    y = [3, 6]
    plt.plot(x, y, 'red')

    # add the head
    plt.plot(1, 7, marker='o',  markersize=16, markeredgecolor='red', markerfacecolor='white')

    # add the arms
    x = [-0.4, -0.5,  1, 2.5, 3.25]
    y = [  2.25,   3.75,    4.5,   5.25,   6.75 ]
    plt.plot(x, y , 'red')


    # add the ball
    plt.plot(3.25, 6.75, marker='o',  markersize=10, markeredgecolor='blue', markerfacecolor='orange')

    # add the hoop
    x = [48, 50]
    y = [10, 10]
    plt.plot(x, y , 'black', linewidth=4)
    x = [48.25, 48, 50, 49.75]
    y = [8, 10, 10, 8]
    plt.plot(x, y , 'black', linewidth=1)

    # add the hardwood floor which consists of strips of wood alternating in brown and orange
    left, right = -10, 60
    x = [left, right, right, left]
    top, bottom = 0, -2
    y = [bottom, bottom, top, top]
    for n in range(10):
        top, bottom = -2*n, -2*n-2
        y = [bottom, bottom, top, top]
        if n % 2:
            fill_color = 'brown'
        else:
            fill_color = 'orange'
        plt.fill(x, y, fill_color)

    plt.grid(True)
    plt.axis('equal')
    plt.axis([-10, 60, -10, 30])
    fig.tight_layout()


# * * * * * * * * * *  DEFINE PARAMETERS  * * * * * * * * * *
# Below, x(t) and y(t) give the trajectory of the basketball

# location of the ball at time 0, as it leaves the hand.
x0 = 3.25; y0 = 6.75


# initial speed of the ball in ft/sec as it leaves your hand
v0 = 40.0 # initial speed       <-- adjust to score

# angle theta in degrees at which ball leaves your found measured from the horizontal.
# note sin and cos expect radians so you have to convert
theta = 45.0  # in degrees      <-- adjust to score

g = 32.174   # acceleration due to gravity in feet per second squared


# Fix these stubs
def x(t):
    theta_in_radians = theta * math.pi / 180
    return x0 + v0*t*math.cos(theta_in_radians)


def y(t):
    theta_in_radians = theta * math.pi / 180
    return y0 + v0*t*math.sin(theta_in_radians) - 0.5*32.174*t**2


def throw_ball():
    score = False
    a, b = x(0), y(0)  # the previous location of the ball

    # Your for loop is here. Let n assume values from 1 to 200 in steps of 1
    for n in range(1, 201):
        # add tons of code here to finish the lab

        # control ball color here. Every tenth ball is red
        if not score:
            if not n % 10 or n ==1:
                plt.plot(a, b, marker='o', markersize=10, markeredgecolor='brown', markerfacecolor='red')
            else:
                plt.plot(a, b, marker='o', markersize=10, markeredgecolor='brown', markerfacecolor='orange')
        
        # calculate t
        t = n / 20

        # Update c, d
        c, d = x(t), y(t)  # Fix this stub

        # check if ball is beneath the floor here and break if it is
        if d < 0:
            break

        # test if the ball passes through the hoop here
        if (b >= 10) and (d < 10):
            X = a + (10-b)*(c-a)/(d-b)
            # check if 48 < X < 50 - you've scored!! Sweet!
            if X > 48 and X < 50:
                score = True
                plt.plot(X,10,marker = '*',markersize=10,markeredgecolor='red',markerfacecolor='red')
                plt.title('Drexel Dragon Player Shoots and SCORES!!')
                plt.plot([a,c],[b,d], color='red')
                
        if score:
            if y(t)<0:
                break
            else:
                if not n % 10:
                    plt.plot(49, y(t), marker='o', markersize=10, markeredgecolor='brown', markerfacecolor='red')
                else:
                    plt.plot(49, y(t), marker='o', markersize=10,markeredgecolor='brown', markerfacecolor='orange')
        
        a, b = c, d  # update (a, b) to the last known location of the ball


if __name__ == "__main__":
    print("\nGo Drexel dragons!!")
    draw()

    # Answer 1b here
    print(x(0.5), y(0.5))

    throw_ball()

    plt.show()  # plot will not appear until you call plt.show()



