import numpy as np
arr = np.arange(0,11)
# to add two arrays together element by element
arr1 = np.arange(11,22)
#  adding arr1 and arr
arr2 = arr1 + arr
print(arr2)
# [11 13 15 17 19 21 23 25 27 29 31]
# both arrays should have equal number of elements
# arrays will be added element by element
arr3 = arr1*arr
print(arr3)
# [  0  12  26  42  60  80 102 126 152 180 210]
# corresponding elements will be added
# arr + 10 add 10 to all arr elements
# np.sqrt(arr) to get saure root of each element
# np.sin(arr) to get sin of each element
# np.log(arr) to get log of all elemnt


n = np.array([[1,2,3],[2,3,4]])
q = np.array([[1,2,3],[2,3,4]])
print(n*q)
# multiplying 2 2d arrays
