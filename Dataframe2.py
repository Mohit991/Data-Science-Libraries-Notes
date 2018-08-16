import numpy as np
import pandas as pd
from numpy.random import randn
df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
print(df)
print(df>0.5)
#        w      x      y      z
# a  False  False  False  False
# b  False  False  False   True
# c   True  False  False  False
# d  False   True  False   True
# e  False   True  False  False
# you can a boolean matrix and all the vales following the condition are true while those dont follow are false
# another way of doing this is
booldf = df>0.5
# print(df[booldf]) or print(df[df>0.5])
#           w   x         y         z
# a  1.897645 NaN       NaN       NaN
# b       NaN NaN       NaN       NaN
# c       NaN NaN       NaN       NaN
# d  0.570875 NaN  0.544611       NaN
# e       NaN NaN       NaN  0.538157
# values follwing condition are shown while not following are NaN


# if you want to check in a col all the vales
print(df['w']>0.5)
# a    False
# b     True
# c    False
# d    False
# e    False
# Name: w, dtype: bool
# this shows the point where condtion is true and where false in the column w
# it is a series and it can stored in  another series


# print(df[df['w']>0.5])
#           w         x         y         z
# b  1.633548  0.525812  1.045594 -0.747829
# c  1.785836 -1.383518  1.206778 -0.427677
# this is returning all the rows whrer the values in the columns w is greater than 0.5, these rows are b and c
# print(df[df['z']<0.2])
# return all rows wheer col z is less than 0.2

result = df[df['w']>0.5]
print(result['x'])
# a   -1.996031
# b   -2.152477
# d   -1.438561
# e    0.303650
# Name: x, dtype: float64
# this does not have col c in it because of the condition and it shows rest vlaues of the col x/
# or result[['x','y']] this will show x and also y cols where the condition gets true


# now we apply multiple condition
# eg
print(df[(df['w']>0.2) & (df['x']>0.5)])
# output:           w         x         y         z
 #            b  1.549985  1.261642 -0.098391 -2.657071
 # this shows the data where vals in col w is greater than 0.2 and col x values are greater than 0.5 this condtion is only true at row b
 # you cannot use and use & and for or use |
print(df[(df['w']>0.2) | (df['x']>0.5)])
#           w         x         y         z
# a  0.004293  1.036559  1.620754 -0.701877
# b  1.067193 -1.288727 -0.946683 -0.008868
# c  1.253513  0.118487 -0.052741  0.084861
# d  0.415353 -1.198611 -0.469410 -1.310949

# Working with the index
# If you want to reset the index of the df to 0,1,2.. use
# df.reset_index()
# df.reset_index(inplace = True) if you want to actuallly change in the real frame
#



# if you want to set a column as the index
print(df)
#           w         x         y         z
# a -0.812709 -1.562430 -0.811066  2.021960
# b  0.571708 -1.444003  0.688402  1.113852
# c  0.579528 -0.131777 -0.017753  0.185579
# d  0.597454  0.237030  1.770887 -0.074432
# e -0.305055  1.207975  0.503494 -0.109132

df['name'] = ['mohit','sahu','kalia','kiara','L']
# print(df)
#           w         x         y         z   name
# a  1.528194 -0.760237 -0.691534  0.159824  mohit
# b -1.627796  0.578544 -1.211950  0.938812   sahu
# c -1.658219  0.188671  1.568613 -0.662140  kalia
# d -0.148880 -1.035327 -0.413811 -1.202153  kiara
# e  1.005741  0.661409 -1.440483 -1.713722      L
# col has been added
df.set_index('name',inplace=True)
# print(df)
#               w         x         y         z
# name
# mohit -0.746729 -0.056855 -0.477838  1.458832
# sahu   0.903026 -0.767778 -0.110969 -0.678354
# kalia  0.484551 -1.070216  0.276267 -1.820153
# kiara -0.256942 -1.519651  0.047492 -0.693186
# L      0.359305  0.371718  1.281772 -1.896644
# name has now become the new index
