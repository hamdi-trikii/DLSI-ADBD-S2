import numpy as np
# Create an 1d array from a list

list1 = [0,1,2,3,4]

arr1d = np.array(list1)

# Print the array and its type
print(type(arr1d),' an ndarray(short for N-dimensional array)')
print(arr1d)

'''
#> class 'numpy.ndarray'
#> array([0, 1, 2, 3, 4])
'''

# Add 2 to each element of arr1d
print(arr1d + 2)
#> array([2, 3, 4, 5, 6])

# Create a 2d array from a list of lists
list2 = [[0,1,2], [3,4,5], [6,7,8]]
arr2d = np.array(list2)
print("arr2d:\n",arr2d)
#> array([[0, 1, 2],
#>        [3, 4, 5],
#>        [6, 7, 8]])


# Create a float 2d array
arr2d_f = np.array(list2, dtype='float')
print("arr2d_f:\n",arr2d_f)
#> array([[ 0., 1., 2.],
#> [ 3., 4., 5.],
#> [ 6., 7., 8.]])


# Convert to 'int' datatype
print("arr2d_int:\n",arr2d_f.astype('int'))
#> array([[0, 1, 2],
#> [3, 4, 5],
#> [6, 7, 8]])
# Convert to int then to str datatype
print("arr2d_str:\n",arr2d_f.astype('int').astype('str'))
#> array([['0', '1', '2'],
#> ['3', '4', '5'],
#> ['6', '7', '8']],
#> dtype='U21')


# Create a boolean array
arr2d_b = np.array([1, 0, 10], dtype='bool')
print("arr2d_bool:\n",arr2d_b)
#> array([ True, False, True], dtype=bool)
# Create an object array to hold numbers as well as strings
arr1d_obj = np.array([1, 'a'], dtype='object')
print("arr1d_obj:\n",arr1d_obj)
#> array([1, 'a'], dtype=object)


# Convert an array back to a list

print(type(arr1d_obj.tolist()))
print(arr1d_obj.tolist())
#> [1, 'a']









