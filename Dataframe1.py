import numpy as np
import pandas as pd
from numpy.random import randn
df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
# print(df)
#           w         x         y         z
# a -1.748380  0.726961 -2.106587  0.306414
# b  0.071925 -1.806793 -1.044487 -0.634857
# c  2.378287 -0.482022 -1.918446 -1.178586
# d -2.594628  0.426131  0.451167  1.157179
# e  0.702336  1.703486 -0.277348 -1.497176
# here randn(5,4) generates a random numbers matrix 5x4
# a,b,c.. are indexes and w,x.. are the column indexes

print(df['w'])
# a    0.482879
# b    0.127531
# c    2.138978
# d   -0.109649
# e    0.151869
# Name: w, dtype: float64
# it grabes the column w
# this looks like a series because w actually is a series


# to get multiple columns back from the df
# print(df[['w','x']])
#           w         x
# a  0.236777 -0.405165
# b -0.449502  0.706352
# c  0.489828 -0.551525
# d  0.698066 -0.100082
# e -0.676920 -1.820698


# to create a new column in the dataframe
# say you want to column names 'z' which is the sum of values of cols w and x
# df['z'] = df['w']+df['x']
# print(df)
#           w         x         y         z
# a  1.649253  0.747862  0.127864  2.397115
# b  0.100410  1.314842 -0.826754  1.415253
# c  0.943404 -0.185446  0.413605  0.757958
# d -1.306602  0.567411  1.445374 -0.739192
# e -0.892535  0.991948  0.322156  0.099413

# new columns z has been created and this is the sum of w and x
# if you want to drop a index say e
# df.drop('e')
#
# if you want to drop a column say z
# df.drop('z',axis=1)
# print(df)
# you will see that all the drop actions do not happen inplace this means that no changes are made to actual df
# to make actual changes to the df do something as
# df.drop('e',inplace=True)
# print(df)
#           w         x         y         z
# a  1.235263 -0.352317 -0.973105  1.049507
# b  1.264185 -0.019734 -0.798366  1.375379
# c -0.796685  0.701088 -1.220385  0.345136
# d -1.486462 -1.566168 -0.655734 -2.766020
# to actaully delete a column

# df.drop('z',axis=1,inplace=True)
# print(df)
#           w         x         y
# a  0.705444  0.024958  0.559600
# b  0.210580  0.631368 -0.749145
# c  0.203702  0.126707 -1.868509
# d  0.748650  0.704325  0.653207
# e -0.119667 -0.451598 -0.618912
# df.shape()

# selecting rows in dataframe
print(df)
print(df.loc['a'])
# w    0.722023
# x    1.873156
# y    0.725773
# z   -0.863489
# Name: a, dtype: float64
print(df.loc['b'])
# w    0.169188
# x    1.849320
# y    0.570128
# z   -1.118497
# Name: b, dtype: float64
#


# Important is that this also return a series  ie rows as well as cols are series

# print(df.iloc[0]) same as df.loc[a] index start with 0 so a is 0 b is 1 and so on
# this is useful when you want the cols with numeric index


# now if you want a perticular value for the matrx
# then
print(df.loc['a','w'])
# -0.33158608257287997
# a is the row name and w is the col name it is same as saying
# df[a][w] in simple form
# you can also get the subset the of matic
print(df.loc[['a','e'],['w','z']])
#           w         z
# a  0.055911 -0.407737
# e -0.194840  1.156436

# this reutrns the values at a and e rows and w and z cols
# you pass 2 lists separated by comas first one for the rows and the other one for the columns
