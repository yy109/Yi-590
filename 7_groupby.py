from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

main_dir = "/Users/lexiyang/Desktop/PPS 590/Demo/"
root = main_dir + "Online Demo Data/"

# PATHING --------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT AND STACK ---------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh'], parse_dates=[1],
    header = None) for v in paths],
    ignore_index = True)
    
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# MERGE ---------
df = pd.merge(df, df_assign)

df['date'].values[0]
type(df['date'].values[0]) # check the type of date (first line), string data does not sort numerically
df.sort(['panid','date'])

# GROUPBY aka "split, apply, combine"
## see more at http://pandas.pydata.org/pandas-docs/stable/groupby.html
grp1 = df.groupby(['assignment']) # .groupby objects for big data
grp1.mean() # existing function we can create by grp1.apply()
gd1 = grp1.groups # CAUTION! don't do this with super big data. it will crash.

## peek inside gd1 (dictionary)
gd1.keys()
gd1['C'] # gd1 is a dict, so must use keys to get data
gd1.values()[0] # gd1.values() is a list, so we can use numerical indeces
gd1.viewvalues() # see all the values of the dictionary, gd1

## iteration properties of a dictionary
[v for v in gd1.itervalues()]
gd1.values() # equivalent to above

[k for k in gd1.iterkeys()]
gd1.keys() # equivalent

[(k,v) for k,v in gd1.iteritems()] # ( ) tapule notation, you cannot edit tapules, not change
gd1

## split and apply (pooled data)
grp1['kwh'].mean()

## split and apply (panel/time series data)
grp2 = df.groupby(['assignment','date'])
gd2 = grp2.groups
gd2 # look at the dictionary (key, value) pairs
grp2['kwh'].mean() 

grp3 = df.groupby(['date','assignment'])
grp3.groups.keys()

## TESTING FOR BALANCE (OVER-TIME)
from scipy.stats import ttest_ind
from scipy.special import stdtr # never use, can be deleted

## ex using ttest_ind
a = [1, 4, 9, 2]
b = [1, 7, 8, 9]

t, p = ttest_ind(a, b, equal_var = False)


# set up data
grp = df.groupby(['assignment', 'date'])
grp.groups

# get separate sets of treatment and control values by date
trt = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'T'}
ctrl = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'C'}
keys = trt.keys()

# grp.groups.keys()[0]
# k = grp.groups.keys()[0]
# k[0]

# v=[53,158]
# type(df.kwh[v])  # series will not work
# df.kwh [[1,10,13]]
# type(df.kwh[v].values) #  array or list will work


# create dataframes of this information
tstats = DataFrame([(k, np.abs(ttest_ind(trt[k],ctrl[k], equal_var=False)[0])) for k in keys],
    columns =['date', 'tstats'])
pvals = DataFrame([(k, np.abs(ttest_ind(trt[k],ctrl[k], equal_var=False)[1])) for k in keys],
    columns =['date', 'pvals'])
t_p = pd.merge(tstats, pvals)

# (ttest_ind(trt[k],ctrl[k], equal_var=False) returns a tuple (t,p)
#(ttest_ind(trt[k],ctrl[k], equal_var=False)[0]  only wants t

## sort and reset _index
t_p.sort(['date'], inplace=True) # inplace = True to change the values
t_p = t_p.sort(['date']) # equivalent, but slow
t_p.reset_index(inplace=True, drop= True)

# comparisons!
diff = {k: (trt[k].mean() - ctrl[k].mean()) for k in keys}
tstats = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[0]) for k in keys}
pvals = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[1]) for k in keys}
t_p = {k: (tstats[k], pvals[k]) for k in keys}


# PLOTTING ----------------------
fig1 = plt.figure() #initialize plot
ax1 = fig1.add_subplot(2,1,1) # (row, columns, reference) two rows, one column, first plot
ax1.plot(t_p['tstats'])
ax1.axhline(2, color='r', linestyle ='--')
ax1.set_title('t-stats over-time')

ax2 = fig1.add_subplot(2,1,2) # (row, columns, reference) two rows, one column, second plot
ax2.plot(t_p['pvals'])
ax2.axhline( 0.05, color='r', linestyle ='--')
ax2.set_title('p-values over-time')




plt.plot?

