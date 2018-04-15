from __future__ import division
import matplotlib.pyplot as plt
import math

coords = [(2, 4), (3, 5), (5, 7), (7, 10), (9, 15)]
houses = [(1100, 199), (1400, 245), (1425, 319), (1550, 219), (1600, 312), (1700, 279), (1700, 255), (1875, 308), (2350, 405), (2450, 324)]
brain = [(3.385, 44.5), (0.48, 15.5), (1.35, 8.1), (465.0, 423.0), (36.33, 119.5), (27.66, 115.0), (14.83, 98.2), (1.04, 5.5), (4.19, 58.0), (0.425, 6.4), (0.101, 4.0), (0.92, 5.7), (1.0, 6.6), (0.005, 0.14), (0.06, 1.0), (3.5, 10.8), (2.0, 12.3), (1.7, 6.3), (2547.0, 4603.0), (0.023, 0.3), (187.1, 419.0), (521.0, 655.0), (0.785, 3.5), (10.0, 115.0), (3.3, 25.6), (0.2, 5.0), (1.41, 17.5), (529.0, 680.0), (207.0, 406.0), (85.0, 325.0), (0.75, 12.3), (62.0, 1320.0), (6654.0, 5712.0), (3.5, 3.9), (6.8, 179.0), (35.0, 56.0), (4.05, 17.0), (0.12, 1.0), (0.023, 0.4), (0.01, 0.25), (1.4, 12.5), (250.0, 490.0), (2.5, 12.1), (55.5, 175.0), (100.0, 157.0), (52.16, 440.0), (10.55, 179.5), (0.55, 2.4), (60.0, 81.0), (3.6, 21.0), (4.288, 39.2), (0.28, 1.9), (0.075, 1.2), (0.122, 3.0), (0.048, 0.33), (192.0, 180.0), (3.0, 25.0), (160.0, 169.0), (0.9, 2.6), (1.62, 11.4), (0.104, 2.5), (4.235, 50.4)]

def LinearRegression(xy_list):
    # Takes a list of coordinates as tuples and returns the regression line coordinates in the same format.
    # Prints output to screen
    reg_list = [] # List of coordinates for the regression line (x, predicted y)
    xy_list.sort() # Ensure the x values are arranged and read in ascending order
    n = len(xy_list) # n = number of observations
    sumx, sumy, sumx2, sumxy = 0, 0, 0, 0
    SST, SSR, SSE = 0, 0, 0 
    # SST = Total Sum of Squares = Σ(yi – ȳ)2 = SSE + SSR
    # SSR = Regression Sum of Squares = Σ(ŷi – ȳ)2
    # SSE = Error Sum of Squares = Σ(yi – ŷi)2
    xSST = 0
    for x, y in xy_list: # xi = Observed values of the independent variable; yi = Observed values of the dependent variable
        sumx += x
        sumy += y
        sumx2 += x*x
        sumxy += x*y
    m = (n*sumxy - sumx * sumy) / (n*(sumx2) - (sumx)**2) # Slope
    b = (sumy - m*(sumx)) / n # Intercept
    ybar = sumy / n # Mean value of the dependent variable
    xbar = sumx / n # Mean value of the independent variable
    for x, y in xy_list:
        yhat = (m*x) + b # ŷi = Predicted value of y for the given xi value
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
    std_error = math.sqrt(SSE / (n-2)) # Standard Error of Estimate - The standard deviation of the variation of observations around the regression line 
    sb1 = std_error / math.sqrt(xSST) # Standard Error of regression slope = sb1 = sqrt (Σ(yi – ŷi)2 /(n – 2)) / sqrt (Σ(xi – x)2)
    t = m / sb1 # t Test
    print "\nSlope: {}".format(round(m, 5))
    print "\nIntercept: \t{}".format(round(b, 5))
    print "\nSSR (Regression Sum of Squares): {}".format(round(SSR, 5))
    print "\nSSE (Error Sum of Squares): \t\t{}".format(round(SSE, 5))
    print "\nTotal Sum of Squares: {}".format(round(SST, 5))
    print "\nSSR + SSE = {} (Should equal SST above)".format(round(chk_SST, 5))
    print "\nR Square: \t{}".format(round(rsquared, 5))
    print "\nStandard Error: {}".format(round(std_error, 5))
    print "\nObservations: {}".format(n)
    print "\nStandard Error of Regression Slope: {}".format(round(sb1, 5))
    print "\nt Stat: {}".format(round(t, 5))
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
 
