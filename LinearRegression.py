from __future__ import division
import matplotlib.pyplot as plt
import math

coords = [(2, 4), (3, 5), (5, 7), (7, 10), (9, 15)]
houses = [(1100, 199), (1400, 245), (1425, 319), (1550, 219), (1600, 312), (1700, 279), (1700, 255), (1875, 308), (2350, 405), (2450, 324)]


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
    print "          Regression Statistics          "
    print "-----------------------------------------"
    print "\nMultiple R:          {}".format("TBA")
    print "\nR Square:            {}".format(round(rsquared, 5))
    print "\nAdjusted R Square:   {}".format("TBA")
    print "\nStandard Error       {}".format("TBA")
    print "\nObservations:        {}".format(n)
    print "-----------------------------------------\n"
    print "---------------------------------------------------------------------------------------------------------------------------"
    print "ANOVA"
    print "{}df{}SS{}MS{}F{}Significance F".format("\t" * 3, "\t" * 3, "\t" * 3, "\t" * 3, "\t" * 3, )
    print "---------------------------------------------------------------------------------------------------------------------------"
    print "Regression{}{}{}{}{}{}".format("\t" * 3, round(SSR, 5), 3, 4, 5, 6)
    print "\nResidual{}{}{}{}{}{}".format("\t" * 3, round(SSE, 5), 3, 4, 5, 6)
    print "\nTotal{}{}{}{}{}{}".format("\t" * 3, round(SST, 5), 3, 4, 5, 6)
    print "---------------------------------------------------------------------------------------------------------------------------\n"
    print "---------------------------------------------------------------------------------------------------------------------------"
    print "{}Coefficients{}Standard Error{}tStat{}P-value{}Lower 95%{}Upper 95%".format("\t" * 3, "\t" * 3, "\t" * 3, "\t" * 3, "\t" * 3, "\t" * 3)
    print "---------------------------------------------------------------------------------------------------------------------------"
    print "Intercept{}{}{}{}".format("\t" * 2, round(b, 5), "\t" * 2, round(sb1, 5))
    print "\nSlope{}{}{}{}".format("\t" * 2, round(m, 5), "\t" * 2, round(t, 5))
    print "---------------------------------------------------------------------------------------------------------------------------"
    
    
    print "\nSlope:         {}".format(round(m, 5))
    print "\nIntercept:     {}".format(round(b, 5))
    print "\nSSR (Regression Sum of Squares): {}".format(round(SSR, 5))
    print "\nSSE (Error Sum of Squares): \t\t{}".format(round(SSE, 5))
    print "\nTotal Sum of Squares: {}".format(round(SST, 5))
    print "\nSSR + SSE = {} (Should equal SST above)".format(round(chk_SST, 5))
    
    print "\nStandard Error: {}".format(round(std_error, 5))
    
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
    
PlotLines(brain)
