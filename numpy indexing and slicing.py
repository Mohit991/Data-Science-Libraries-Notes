import numpy as np
arr = np.arange(0,11)
# arr[8] index start from zero here as well


# print(arr[1:5])
#  just like  a python list, it will print elemnts in the array from 1 to 5 and 5 will be excluded


# print(arr[:6]) from starting to 6
# print(arr[6:]) from 6 till the end
# arr[0:6] = 10 this will make all the values from 0 to 6 in the array equal to 10
# arr[2:5] = 7 same as above just 7 this time

slice_arr = arr[0:6]
# print(slice_arr)  output [0 1 2 3 4 5]
# this is used to get a bunch of values from the array
slice_arr[:] = 10
# all values will be set to 10
# this will also change the values in the original array from where you got that arrray
print(arr)
print('\n\n\n')




# you can make a copy of the array
# as
arr_copy = arr.copy()
print(arr_copy)



# for 2D array
darr = np.array([[1,5,9],[2,6,10]])
# print(darr)

print(darr.shape)
print(darr[0][2])# this prints 9
# 0 is the row and 2 is the columns like c style
# rows and column both start from 0

# print(darr[1]) this will get you an entire row ie row number 1(index starts from zero)


print('\n\n\n')



# you may want chunk of data instead of just a row then you can again use the slice notation
print(darr[:2,1:])
# this means everything upto row 2 everythin after column 1
print(darr)
print(darr[:,:1])
# this means only the first column
print(darr[1:2,1:])
# this means the 1st row and all columns after 1  remember index start at 0


print('\n\n')



# conditional selection
arr1 = np.arange(1,11,2)
print(arr1>5)
# [False False False  True  True]
# this can be stored in another array
list1 = arr1>5
arr2 = np.array(list1)
print(arr2)
# [False False False  True  True]
# remember that arr2 will be a boolean array which means that it will only contain true or false
print(arr1[list1])
# [7 9]
# this will print the numbers that follow the condition
# you can also store all such elements into another array or list
list2 = arr1[list1]
print(list2)
# list2 will contain all the numbers from arr1 which follow the condition for list1

list3 = arr1[arr1>5]
print(list3)
# list3 again contain the same things but it is simply

