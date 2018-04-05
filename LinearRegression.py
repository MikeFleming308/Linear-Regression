from __future__ import division
import matplotlib.pyplot as plt
import math

coords = [(2, 4), (3, 5), (5, 7), (7, 10), (9, 15)]
houses = [(1100, 199), (1400, 245), (1425, 319), (1550, 219), (1600, 312), (1700, 279), (1700, 255), (1875, 308), (2350, 405), (2450, 324)]
# SE of regression slope = sb1 = sqrt [ Σ(yi – ŷi)2 / (n – 2) ] / sqrt [ Σ(xi – x)2 ].
def LinearRegression(xy_list):
    # Takes a list of coordinates as tuples and returns the regression line coordinates in the same format.
    # Prints output to screen
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
    xbar = sumx / n # Mean value of the independent variable
    for x, y in xy_list:
        yhat = (m*x) + b
        SSR += (yhat - ybar)**2
        SST += (y - ybar)**2
        xSST += (x - xbar)**2
        error = y - yhat
        SSE += error**2
        ords = (x, yhat)
        reg_list.append(ords)
        print "\nx = {}, y = {}, predicted y = {}, error = {}".format(x, y, yhat, error)
    
    chk_SST = SSR + SSE
    rsquared = SSR / SST
    std_error = math.sqrt(SSE / (n-2))
    sb1 = std_error / math.sqrt(xSST)
    print "\nSlope: {}, intercept: {}".format(m, b)
    print "\nTotal Sum of Squares: {}".format(SST)
    print "\nRegression Sum of Squares: {}".format(SSR)
    print "\nSum of Errors: {}".format(SSE)
    print "\nStandard Error of Regression Slope: {}".format(sb1)

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
        
PlotLines(coords)
