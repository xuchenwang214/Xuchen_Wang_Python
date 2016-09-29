# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 01:07:46 2016

@author: xuchenwang
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
import math

def outlier(data,tit):
    '''
    Firstly, use the formula 'upper bound = Q3+1.5*(Q3-Q1) lower bound = Q1-1.5*(Q3-Q1)'
    to caculate the upper and lower bound;
    Secondly, use loop to seperate the norm points, upper outliers and lower outliers into
    three groups(if there is any).
    Thirdly, draw the histogram for each group.
    Finally, draw a boxplot for the whole data.
    
    The parameter is data and the titil of the data.
    The function shows histogram and boxplot.    
    '''
    # Remove 'Nan' from data
    for i in range(len(data)):
        if math.isnan(data[i]):
            data.drop[data[i]]
    # Use 'describe' function in pandas. It shows some statistics include Q1 and Q3. Use them to calculate IQR.
    stati = data.describe()
    # Use 'head' function to overlook col names in the first line.
    stati.head(0)
    # Use one definition of outlier to calculate the upper and lower bounds.
    upper = stati.ix[6,0]+(stati.ix[6,0]-stati.ix[4,0])*1.5 # upper bound = Q3+1.5*(Q3-Q1)
    lower = stati.ix[4,0]-(stati.ix[6,0]-stati.ix[4,0])*1.5 # lower bound = Q1-1.5*(Q3-Q1)
    # Creat three lists to seperate three groups : norm group, data bigger than upper and data smaller than lower.
    outlierup = []
    outlierdown = []
    norm = []
    # Consider the condition that there do not exist outliers. Use logical 'up' and 'down' to indicate if there are any outliers.
    up = True
    down = True
    # Use 'for' loop to go through every data to judge if it is an outlier and add it to the corresponding group.
    for i in range(0,len(data)):
        # When we pick a single data from the Series, its type is numpy.float64 and it changes from original number slightly. 
        # So use 'float' to make it the same with origin.
        if float(data[i]) > upper:
            outlierup.append(float(data[i]))        
        elif float(data[i]) < lower:
            outlierdown.append(float(data[i]))
        else:        
            norm.append(float(data[i]))
    # Convert list to series in order to draw histogram and boxplot.  
    outlierup = Series(outlierup)
    norm = Series(norm)
    outlierdown = Series(outlierdown)
    # If there is no element in outlierup or outlierdown, change up or down to false.
    if len(outlierup) == 0:
        up = False   
    if len(outlierdown) == 0:
        down = False
            
    # Calculate the optimal bin width. Use freedom-diaconis rule as bin size. So bins = (max-min)/bin size.
    stat = norm.describe()
    iqr = stat.ix[6,0]-stat.ix[4,0]
    # freedom-diaconis rule
    h = 2*iqr/(len(norm)**(1/3))
    # If h = 0, use rice rule as the optimal bin size
    if h == 0:
        bin = int((2*(len(outlierup)**(1/3))))+1 # rice rule
        plt.figure()
        plt.hist(norm, bins=bin,label='up outliers')
        plt.title('{} upoutliers Histogram'.format(tit))
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
        
    else:
        # Since bins must be an integer, use 'round'.
        bin = int((max(norm)-min(norm))/h)+1    
        # Draw histogram.
        plt.figure() # Draw each figure seperately.
        plt.hist(norm, bins = bin) # Draw histogram with optimal bin
        plt.title('{} norm Histogram'.format(tit)) # Add an title
        plt.xlabel('Value') # Add a x-label
        plt.ylabel('Frequency') # Add a y-label
        plt.show() # Display the histogram
    
        # Use the same method as above to calculate optimal bin and draw histogram if there are any outliers.
    if up:
        statup = outlierup.describe()
        iqr = statup.ix[6,0]-statup.ix[4,0]
        h = 2*iqr/(len(outlierup)**(1/3)) #freedom-diaconis rule
        if h == 0:
            bin = int(2*(len(outlierup)**(1/3)))+1
            plt.figure()
            plt.hist(outlierup, bins=bin,label='up outliers')
            plt.title('{} upoutliers Histogram'.format(tit))
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
        else:
            bin = int((max(outlierup)-min(outlierup))/h)+1
            plt.figure()
            plt.hist(outlierup, bins=bin,label='up outliers')
            plt.title('{} upoutliers Histogram'.format(tit))
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
            
    if down:
        statdown = outlierdown.describe()
        iqr = statdown.ix[6,0]-statdown.ix[4,0]
        h = 2*iqr/(len(outlierdown)**(1/3)) #freedom-diaconis rule 
        if h == 0:
            bin = int(2*(len(outlierup)**(1/3)))+1
            plt.figure()
            plt.hist(outlierdown, bins=bin,label='up outliers')
            plt.title('{} upoutliers Histogram'.format(tit))
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
        else:
            bin = int((max(outlierdown)-min(outlierdown))/h)+1
            plt.figure()
            plt.hist(outlierdown, bins=bin,label='low outliers')
            plt.title('{} downoutliers Histogram'.format(tit))
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
      
    # Draw box plot of the whole data.
    #plt.figure()
    plt.boxplot(data)
    plt.title('{} boxplot'.format(tit))

# Procedure for the Diamond dataset.    
def main1():
    # Use function in pandas to read .csv file
    data_index = 'https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv'
    diamond = pd.read_csv(data_index)
    # Overlook the col names in the first line to extract data from the data frame
    diamond.head(0)
    # Extract the two numerical column from data frame
    carat = diamond.ix[:,1]
    price = diamond.ix[:,5]   
    # use function defined above to show diagram of each column
    outlier(carat,'carat')
    outlier(price,'price')

# Procedure for the Abalone dataset    
def main2():
    data_index = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    col_names = ['sex','length','diameter','height','whole weight','shucked weight','viscera weight','shell weight','rings']
    # Since the data in a .data file is contained in a format where the columns are separated by commas,
    # it is actually a .csv file. So use 'read_csv' to load the file, and add it column names.
    abalone = pd.read_csv(data_index,header = None,names = col_names)
    # Overlook the col names in the first line to extract data from the data frame.
    abalone.head(0)
    
    #for i in range(1,len(col_names)):
       # outlier(abalone.ix[:,i],col_names[i])
       # print(i)
    ring = abalone.ix[:,8]
    outlier(ring,'ring')

def main3():
    data_index = '/Users/xuchenwang/Desktop/census-income.data'
    col_names = ['AAGE','ACLSWKR','ADTIND','ADTOCC','AGI','AHGA','AHRSPAY','AHSCOL','AMARITL','AMJIND','AMJOCC','ARACE','AREORGN','ASEX',
                  'AUNMEM','AUNTYPE','AWKSTAT','CAPGAIN','CAPLOSS','DIVVAL','FEDTAX','FILESTAT','GRINREG','GRINST','HHDFMX','HHDREL','MARSUPWT',
                  'MIGMTR1','MIGMTR3','MIGMTR4','MIGSAME','MIGSUN','NOEMP','PARENT','PEARNVAL','PEFNTVTY','PEMNTVTY','PENATVTY','PRCITSHP','PTOTVAL',
                  'SEOTR','TAXINC']
    kdd = pd.read_csv(data_index,header = None,names = col_names)
    num_names = kdd.describe().head(0).columns
    for i in range(len(num_names)):
        outlier(kdd[num_names[i]],num_names[i])
# check    
main1()
main2()
main3()