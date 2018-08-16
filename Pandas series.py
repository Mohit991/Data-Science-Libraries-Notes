import pandas as pd
import numpy as np
# it is very smiliar to numpy array but series can be indexed by labels
labels = ['a','b','c']
mydata = [10,20,30]
arr = np.array(mydata)

# now we will create a series which looks a lot like numpy array
# print(pd.Series(data=mydata))
# output of this is:-
# 0    10
# 1    20
# 2    30
# dtype: int64
# it shows the indexes right next to the data this is where is it different from np array
# Now the main advantage of series is that you can give labels as indexes
# as
ser = pd.Series(data=mydata,index=labels)# or ser = pd.Series(mydata,labels)
print(ser)

# a    10
# b    20
# c    30
# dtype: int64

# so here the index for 10 is a, index for 20 is b and so on
#
# you can also pass a np array to a series
# as
ser1 = pd.Series(arr,labels)
print(ser1)
# a    10
# b    20
# c    30
# dtype: int32

# here we can pass dictonary as well, the keys will become indexes and vlaues will become values at those indexes
d = {'a':10,'b':20,'c':30}
# a dictionary
ser2 = pd.Series(d)
print(ser2)
# a    10
# b    20
# c    30
# dtype: int64
# with the help of series the index can be anything it is not limited to just 0,1,2 etc
print('\n\n\n')



# another way of creating a series
ser3 = pd.Series([1,2,3,5],['mohit','rajesh','raja','ram'])
print(ser3)
# mohit     1
# rajesh    2
# raja      3
# ram       5
# # dtype: int64

# 1,2,3,5 are values and mohit .. are indexes for those values


# getting information from the series
# just like python dictionary, give the index and get the value
print(ser3['mohit'])
# outout 1
print(ser3['ram'])
# output 5


# you can add 2 Series
# when 2 series are added values at same indexes are added together and all those points where index do not match in
# both the series there a NaN will pe put

sa1 = pd.Series([10,12,56],['mohit','ram','liala'])
sa2 = pd.Series([11,22,36],['jyoti','ram','neel'])
print(sa1+sa2)
# jyoti     NaN
# liala     NaN
# mohit     NaN
# neel      NaN
# ram      34.0
# dtype: float64
# only ram is added since it was same in both the series
