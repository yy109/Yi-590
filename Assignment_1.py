from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/lexiyang/Desktop/Yi-590"
txt_file = "/File1_small.txt"

pd.read_table(main_dir + txt_file, sep = " ") 
df = pd.read_table(main_dir + txt_file, sep = " ") 

df[60:100]
df[df.kwh>30]