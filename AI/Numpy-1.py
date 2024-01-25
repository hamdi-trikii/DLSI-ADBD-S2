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

'''*********************************************************************************************
************************************************************************************************'''
'''3. Comment inspecter la taille et la forme d'un tableau numpy ?'''
print("3. Comment inspecter la taille et la forme d'un tableau numpy ?")

# Create a 2d array with 3 rows and 4 columns
list2 = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
arr2 = np.array(list2, dtype='float')

#> array([[ 1., 2., 3., 4.],
#> [ 3., 4., 5., 6.],
#> [ 5., 6., 7., 8.]])
# shape
print("Create a 2d array with 3 rows and 4 columns:")
print(arr2)
print('Shape: ', arr2.shape)
# dtype
print('Datatype: ', arr2.dtype)
# size
print('Size: ', arr2.size)
# ndim
print('Num Dimensions: ', arr2.ndim)
#> Shape: (3, 4)
#> Datatype: float64
#> Size: 12
#> Num Dimensions: 2


'''*********************************************************************************************
************************************************************************************************'''
"""4. Comment extraire des éléments spécifiques d'un tableau ?"""
print("4. Comment extraire des éléments spécifiques d'un tableau ?")

#> array([[ 1., 2., 3., 4.],
#> [ 3., 4., 5., 6.],
#> [ 5., 6., 7., 8.]])

print(arr2[:2, :2])
#print(list2[:2, :2]) # error


# Get the boolean output by applying the condition to each element.
b = arr2 > 4
print(b)
#> array([[False, False, False, False],
#> [False, False, True, True],
#> [ True, True, True, True]], dtype=bool)

print(arr2[b])#only true values
#> array([ 5., 6., 5., 6., 7., 8.])









