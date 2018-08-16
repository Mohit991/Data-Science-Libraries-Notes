#creates Ndarray object :-
# which describes colletion of similar types
#to import
import numpy as np


# creating a numpy array
a = np.array([1,2,3])
# print(a)


# creating array of more than one dimension
b = np.array([[1,2,4],[1,4,5]])
# print(b)
# it is a 2d array with 2 rows and 3 cols


# you can also give a dtype to an array like complex eg
c = np.array([1,2,3],dtype=complex)
# print(a)
# datatype can be int float etc


# you can find the datatype of the array
print(c.dtype)


# Attributes
# 1. Shape :-
#  it returns the tuple consisting of array dimensions
print(c.shape)
# for 1d array it is (n,) where n = no of elements in 1d array

d =  np.array([[1,2,3],[4,6,7]])
print(d.shape)
# (2,3) means 2 rows and 3 columns

# you can also use this to change the shape of the array as :
d.shape = (3,2)
# print(d)
# it will now contain 3 rows and 2 cols

# you can also use reshape() to do the same
d.reshape(2,3)
# print(d)
# it will now contain 2 rows and 3 cols

# ndim will return the dimension of the array which is 1d or 2d etc
print(d.ndim)
# 2 means 2 dimension

# itemsize returns the length of each element
print(d.itemsize)
# 4 means each element takes 4 bytes. size is always in 4 bytes.




# this section will contain creating an array
# using the empty()
# arr = np.empty(shape=,dtype=)
# eg
arr = np.empty([3,2],dtype=int)
print("\n\n")
print(arr)
# arr has 3 rows and 2 cols and datatype is int, it can be float or anything else. values are not initilized
# so they have random values


# arr = np.zeros([3,2],dtype=float)
# same as empty except all values the initilized with zeros

# arr = np.ones([3,2],dtype=float)
# values initilized with ones
#


# creating np array from existing data such as a list or  anything else

a = [1,2,3,4,5]
arr1 = np.asarray(a)
# print(arr1)
# arr1 is an np array created from the list a

# arr1 = np.asarray(a,dtype=float)
# this makes arr1 same as above except datatype is now float.

# to create an array from a specific range
# x = np.arange(start=,stop=,step=,dtype=)
# eg
print("\n\n")
x = np.arange(1,20,2,int)
print(x)
#by default start = 0, step = 1 , dtype = int
# eg
x1 = np.arange(10)
print(x1)
# output : [0 1 2 3 4 5 6 7 8 9]

x2 = np.arange(5,10)
print(x2)
# it will be [0 1 2 3 4 5 6 7 8 9]


# converting a list into np array another eg
list1 = [1,2,4,5]
arr2 = np.array(list1)
# print(arr2)


# you can also generate random numbers using numpy
r = np.random.rand(5) #it will generate five random numbers
print('\n\n')
# print(r)
r1 = np.random.rand(5,5)
print(r1)
# output
# [[0.28258447 0.01857335 0.28162196 0.99149376 0.26668357]
#  [0.30660349 0.9426303  0.21829689 0.34330743 0.08826807]
#  [0.20666538 0.90341211 0.91027011 0.48074839 0.7348599 ]
#  [0.07632259 0.66949135 0.39865225 0.36804269 0.60964471]
#  [0.84971608 0.07824099 0.79132697 0.18871091 0.80766015]]

# if you want to generate a random number you can use randomint
r2 = np.random.randint(1,100) #a random number between 1 to 100
# print(r2)
r3 = np.random.randint(1,100,10)
# print(r3)
# output [53 48  8 72 27 43 34 98 81 68] ten random numbers from 1 to 100



# you can easily get max, min or sum of the elements in the array
test = np.array([1,2,3,4,5,6,7,8])
# print(test.max())
# print(test.min())
# print(test.sum())

# you can also get the index of the max, min values
# test.argmax() will return the index of the max value
# test.argmin()
