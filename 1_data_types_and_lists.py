from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/lexiyang/Desktop/data"
git_dir ="/Users/lexiyang/Desktop/Yi-590"
csv_file_good="sample_data_clean.csv"
csv_file_bad="sample_data_clean.csv"

# OS MODULE---------------
df = pd.read_csv(os.path.join(main_dir,csv_file_good))
df = pd.read_csv(os.path.join(main_dir,csv_file_bad))

# PYThON DATA TYPES -----------

## strings
str1 = "hello, computer"
str2 = 'hello, human'
str3 = u'eep' #unicode: universal platform text

type(str1) # type str
type(str2) # type str
type(str3) # type unicode

## numeric
int1 = 10
float1 = 20.56
long1 = 40998978766564244555550000000

## logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)

# CREATING LISTS AND TUPLES ----------------

## in brief, lists can be changed, tuples cannot
## we almost exclusively use lists

list1 = [] 
list1
list2 = [7, 8, 'a']
list2[2] # output of this is 'a'
list2[2] = 5

##tuples, cant change
tup1 = (8, 3, 19)
tup1[2] # outputs is 19
tup1[2] = 5 # The line of code shows you an error to tell you tuples cant change

## convert
list2 = list(tup1)
tup2 = tuple(list1)

## list can be append and extended
list2 =[8, 3, 19]
list2.append([3, 90]) # out: [8, 3, 19, [3, 90]]
len(list2)
list3 = [8, 3, 19]
list3.extend([6, 88]) # out: [8, 3, 19, 6, 88]
len(list3)

# CONVERTING LISTS TO SERIES AND DATAFRAME
list4 = range(100, 105) # range(n,m) -- gives a list from
                     # n to m-1
list4 # out: [100, 101, 102, 103, 104]
list5 = range(5) # range(m) -- gives list from 0 to m-1
list5 # out: [0, 1, 2, 3, 4]
list6 = ['q', 'r', 's', 't', 'u']

## list to series
s1 = Series(list4)
s2 = Series(list6)

## create DataFrame from lists OR series
list7 =  range(60, 65)
zip(list4, list6)
zip1= zip(list4, list6, list7)
df1 = DataFrame(zip1)
df1[0]

df2 = DataFrame(zip1, columns = ['two', 'apple', ':)'])
df2['two']

df3 = DataFrame(zip1, columns = [2, '2', ':)'])
df3[2] # reference column with key (int) 2
df3['2'] # reference column with key '2'
df3[3:4] # slice out row 3
df3[['2',':)']][3:4] # get column '2' and ':)' then 
                     # get row 3

## make datafrme using dict notation
df4 = DataFrame({ ':(' : list4, 9: list6})
dict1 = { ':(' : list4, 9: list6}
dict1 [':(']
