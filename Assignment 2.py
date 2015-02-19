from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/lexiyang/Desktop/data"
csv_file="small_data_w_missing_duplicated.csv"

# IMPORTING DATA: SETTING MISSING VALUES (SENTINELS)

missing = ['.', 'NA', 'NULL', ' ', '-']
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)
df['consump'].head(10). apply(type)

# Drop FULL rows are duplicates
df1= df.drop_duplicates()

# Extract the FULL rows with missing Consump
df1['consump'].isnull()
rows = df1['consump'].isnull()
df1[rows]

# Check for any duplicated values on the SUBSET of panid and date
df1.duplicated(['panid','date'])
df1[df1.duplicated(['panid','date'])]
df1.duplicated(['panid', 'date'], take_last = True)
df1[df1.duplicated(['panid', 'date'], take_last = True)]

# Drop the rows where consump is missing for any duplicated values
t_b = df1.duplicated(['panid', 'date'])
b_t = df1.duplicated(['panid', 'date'], take_last = True)
unique = ~(t_b | b_t)
df2 = df1[unique]

df3 = df2.dropna()

# Take the average (mean) of variable consump.
df3.consump.mean()
