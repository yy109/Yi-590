from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/lexiyang/Desktop/data"

# ADVANCED PATHING ---------------------------------
root = main_dir + "/cooked/"
paths = [root + v for v in os.listdir(root) if v.startswith("File")]

# IMPORT DATA -----------------------------------
list_of_dfs = [pd.read_table(v, names = ['ID', 'time', 'kwh'], sep = " ", skiprows = 6000000, nrows = 1500000) for v in paths]
len(list_of_dfs)
type(list_of_dfs)
type(list_of_dfs[0])

## ASSIGNMENT DATA --------------------------
df_assign = pd.read_csv(root + "SME and Residential allocations.csv",usecols = [0,1,2,3,4])

# STACK AND MERGE ----------------
df_stack= pd.concat(list_of_dfs, ignore_index = True)
del list_of_dfs
df = pd.merge(df_stack, df_assign)

## CLEANING DATA ------------------
df['tt'] = df['time']% 100 # extract the last two digits
df['ddd'] = (df['time']-df['time']% 100)/100
df1 = df[df['tt']>48]
#df = df[df['tt']<=48]

df[df['time'] == 45202]
df[df['time'] == 45203]

t_b = df.duplicated()
b_t = df.duplicated(take_last = True)
unique = ~(t_b | b_t) # complement where either is true
unique = ~t_b & ~b_t
unique
df= df[unique]

df['ddd'] = (df['time']-df['time']% 100)/100
