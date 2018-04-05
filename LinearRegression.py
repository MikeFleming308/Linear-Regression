from __future__ import division
import matplotlib.pyplot as plt
import math


coords = [(2, 4), (3, 5), (5, 7), (7, 10), (9, 15)]

houses = [(1100, 199), (1400, 245), (1425, 319), (1550, 219), (1600, 312), (1700, 279), (1700, 255), (1875, 308), (2350, 405), (2450, 324)]


def LinearRegression(xy_list):
    # Takes a list of coordinates as tuples and returns the regression line coordinates in the same format.
    # Prints output to screen
    xy_list.sort()
    reg_list = []
    n = len(xy_list)
    sumx, sumy, sumx2, sumxy = 0, 0, 0, 0
    SST, SSR, SSE = 0, 0, 0 # SST = Total Sum of Squares, SSR = Regression Sum of Squares, SSE = Error Sum of Squares
    for x, y in xy_list:
        sumx += x
        sumy += y
        sumx2 += x*x
        sumxy += x*y
    m = (n*sumxy - sumx * sumy) / (n*(sumx2) - (sumx)**2) # Slope
    b = (sumy - m*(sumx)) / n # Intercept
    ybar = sumy / n # Mean value of the dependent variable
    for x, y in xy_list:
        yhat = (m*x) + b
        SSR += (yhat - ybar)**2
        SST += (y - ybar)**2
        error = y - yhat
        SSE += error**2
        ords = (x, yhat)
        reg_list.append(ords)
        print "\nx = {}, y = {}, predicted y = {}, error = {}".format(x, y, yhat, error)
    chk_SST = SSR + SSE
    rsquared = SSR / SST
    std_error = math.sqrt(SSE / (n-2))
    print "\nSlope: \t\t{}".format(m)
    print "\nIntercept: \t{}".format(b)
    print "\nSSR (Regression Sum of Squares): {}".format(SSR)
    print "\nSSE (Error Sum of Squares): \t\t{}".format(SSE)
    print "\nSST (Total Sum of Squares): \t{}".format(SST)
    print "\nSSR + SSE = {} (Should equal SST above)".format(chk_SST)
    print "\nR Square: \t{}".format(rsquared)
    print "\nStandard Error: {}".format(std_error)
    print "\nObservations: {}".format(n)
    return reg_list
    
    
def PlotLines(ords_list):
    reg_ords = LinearRegression(ords_list)
    xords = [ord[0] for ord in ords_list]
    yords = [ord[1] for ord in ords_list]
    reg_yords = [ord[1] for ord in reg_ords]
    fig, ax = plt.subplots()
    ax.plot(xords, yords)
    ax.plot(xords, reg_yords)
    ax.set(xlabel='x', ylabel='y', title='Data with regression line')
    ax.grid()
    plt.show()
