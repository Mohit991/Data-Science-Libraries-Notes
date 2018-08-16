import pandas as pd
import numpy as np
d = {'A':[3,2,np.nan],'B':[3,np.nan,6],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
#      A    B  C
# 0  3.0  3.0  1
# 1  2.0  NaN  2
# 2  NaN  6.0  3
# this is the output
# often when we use pandas and we find that in actual world data many values are null there
# or many data is missing
# df.dropna(inplace=True)
# print(df)
#      A    B  C
# 0  3.0  3.0  1
# it will drop all rows with any single nan values
# if you want to drop all the columns which have any null values simply just  set axis = 1
# df.dropna(axis=1,inplace=True)
# print(d   C
# 0  1
# 1  2
# 2  3



# you can also make sure that not all rows with any nan values are dropped
# but all the rows with a number of nan values are dropped for that
# you can use thresh
# df.dropna(thresh=2,inplace=True)
# print(df)
#      A    B  C
# 0  3.0  3.0  1
# 1  2.0  NaN  2
# 2  NaN  6.0  3

# df.dropna(thresh=3,inplace=True)
# print(df)
#    A    B  C
# 0  3.0  3.0  1

# thresh = values where value is the min number of data points each row must have
# if it is 3 means each row must min have 3 data points rest can be null or nan values


# to fill nan values
# df.fillna(value="fill value",inplace=True)
# print(df)
#             A           B  C
# 0           3           3  1
# 1           2  fill value  2
# 2  fill value           6  3

# at the place of nan values there is now "fill value" or you can also set a numerical value
# often you want to fill the average value at the missing data
df['A'].fillna(value=df['A'].mean(),inplace=True)
# print(df)
#      A    B  C
# 0  3.0  3.0  1
# 1  2.0  NaN  2
# 2  2.5  6.0  3
# now the col A missing values ie nan values will have value equal to all values in the cols

