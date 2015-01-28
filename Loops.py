from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/lexiyang/Desktop/data"
git_dir ="/Users/lexiyang/Desktop/Yi-590"
csv_file="sample_data_clean.csv"

# FOR LOOPS -----------------------
df = pd.read_csv(os.path.join(main_dir,csv_file))
list1 = range(10,15)
list2 = ['a', 'b', 'c']
list3 = [1, 'a', True]

## iterating over elements (for loops)
for v in list1:
    v
    
for v in list2:
    print(v)
    
for v in list3:
    print(v,type(v))
    
for sweet in list3:
    print(sweet,type(sweet),'haha')

list1 # is all int
list4 = [] # empty list 
list5 = []
for v in list1:
    v2 = v**2
    list4.extend([v2]) # accepts only 'list' obj
    list5.apend(v2) # appends whatever obj as is 

[v**2 for v in list1]
list6 = [ v**2 <144 for v in list1] # used for int

## iterating using enumerate
list7 = [ [i, float(v)/2] for i, v in enumerate(list1)]

# ITERATE THROUGH A SERIES -------------------
s1 = df['consump']
[v > 2 for v in s1]
[[i, float(v)*.3] for i, v in s1.iteritems()]

# ITERATE THROUGH A DATAFRAME -------------------
[v for v in df]
[df[v] for v in df]  
[[i, v] for i, v in df.iteritems()]