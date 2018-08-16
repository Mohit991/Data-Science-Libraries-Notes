import numpy as np
import pandas as pd
df = pd.DataFrame({'a':[1,2,3],'b':[8,7,5]})
# print(df)
#    a  b
# 0  1  8
# 1  2  7
# 2  3  5

# finding all the uniques values in a dataframe
print(df['a'].unique())
# this prints the unique values in col 'a'
# if you only want the number of unique values then
# df['a'].nunique()
# prints the number of unique values in col 'a'


# now say you have a function
def mul(x):
    return x*2
# now say you want to call this function for a column
# as
# df['a'].apply(mul)
print(df['a'].apply(mul))
# 0    2
# 1    4
# 2    6
# Name: a, dtype: int64
# all the values in that column now have been multiplied by 2
# in this manner you can use any function
# the effect will be applied to all the values in the column
# you can also apply lamda function using this as
print(df['b'].apply(lambda x: x*2))
# 0    16
# 1    14
# 2    10
# Name: b, dtype: int64
# all of the values are multiplied by 2
# this is used lamda funvtion


# removing col
# df.drop('a',axis=1,inplace=True)
# print(df)
# a has been deleted


print(df.columns)
# Index(['a', 'b'], dtype='object')
# info about all the cols and their names



# sorting the dataframe by a col
df.sort_values('a')
# now df will be sorted accoring to col a

# to see all the null values
df.isnull()
# this will return the whole matrix giving info about each point wether it is null or not
