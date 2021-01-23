import numpy as np

"""NUMPY NOTES

The Basics
---------------------------------------------------------------------------
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)                              #Gives the dimensions of the array, (rows,columns)
print(a.ndim)                               #Gives the number of dimensions of the array
print(a.dtype.name)                         #Gives the data type
print(a.itemsize)                           #Item size
type(a)
---------------------------------------------------------------------------

Creating Arrays
---------------------------------------------------------------------------
a=np.array([(1.5,2,3), (4,5,6)])             #Creates arrays
np.zeros((6,1,3))                            #Array of 0s from (sets,rows,# of values)
np.ones((2,3,4))                             #Array of 0s from (sets,rows,# of values)
np.arange(10,30,5)                           #This is basically the range function but puts it into arrays.
                                             #np.arrange(start,end(doesn't include),step)
np.linspace(2,6,5)                           #creates and array but instead gets the number of values you want from a range


a=np.ones((2,2,3,4))                         #4d array, 2 large sets, 2 small sets which as 3 rows each and 4 values

[[[[1. 1. 1. 1.],
   [1. 1. 1. 1.],
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.],
   [1. 1. 1. 1.],
   [1. 1. 1. 1.]]]

Set 2

 [[[1. 1. 1. 1.],
   [1. 1. 1. 1.],
   [1. 1. 1. 1.]]

  [[1. 1. 1. 1.],
   [1. 1. 1. 1.],
   [1. 1. 1. 1.]]]]
---------------------------------------------------------------------------

Adding,removing, and sorting elements
---------------------------------------------------------------------------
arr = np.array([5,2,1])
arr2= np.array([1,4,6,6])
ascending=np.sort(arr)                                                   #Sorts array in ascending order
descending=-np.sort(-arr)                                                #Sorts array in descending order
np.concatenate((arr,arr2))                                               #Combines 2 arrays

Reshaping Arrays
-----------------------
a=np.arange(6)
a.reshape(2,3)                                                           #Reshapes the original to a different shape, this is a 2 by 3
np.reshape(a, newshape=(1,6),order='F')                                  #Different way to reshape, with parameters
---------------------------------------------------------------------------

How to convert a 1D array into a 2D array (how to add a new axis to an array)
---------------------------------------------------------------------------
a=np.array([1,2,3,4,5,6])
row_vector=a[np.newaxis,:]                                              #This will create a new axis (1,6) 1 row 6 values
column_vector=a[:,np.newaxis]                                           #This will create a new axis (6,1) 6 rows 1 value


#Example with newaxis. You cannot just add a and b because they have different sizes
#Creating a new axis makes it into a 2d array, which allows numpy to broadcast to the other array.
a=np.array([1,2,3,4])
b=np.array([10,20,30])
b[:,np.newaxis]+a
[[10],  +  [1,2,3,4]
 [20],
 [30],]
=
[[11 12 13 14]
 [21 22 23 24]
 [31 32 33 34]]


a=np.array([[1,3],[2,4]])                                                   #Example of matrix multiplication 
b=np.array([[3,4],[3,1]])
a@b
[[12  7]
 [18 12]]
---------------------------------------------------------------------------

Indexing and slicing
---------------------------------------------------------------------------

arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr2=arr[3:8]                                                               #[4,5,6,7,8]
arr3=arr[:4]                                                                #[1,2,3,4]
arr4=arr[4:]                                                                #[5,6,7,8,9,10]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b=np.nonzero(a<5)                                                             #(array( [0,0,0,0], array( [0,1,2,3]))  The row, column
list_of_coordinates= list(zip(b[0], b[1]))                                    (0, 0)
                                                                              (0, 1)
                                                                              (0, 2)
                                                                              (0, 3)
---------------------------------------------------------------------------   
                                                                           
Basic Operations
---------------------------------------------------------------------------
data=np.array([1,2])
one=np.array([2,3])
data+one
data-one
data*one
data/one


a=np.array([[1,2],[3,4],[5,6]])
a.sum()                     #=21                                             #Takes the sum of all values in the array

b = np.array([[1, 1], [2, 2]])
b.sum(axis=0)               #=[3 3]                                          #Takes axis 0, which is rows, adds the value each row. Adds everything going down
b.sum(axis=1)               #=[2,4]                                          #Takes axis 1, which is columns, adds the value in each column together
---------------------------------------------------------------------------

Random
---------------------------------------------------------------------------

np.random.randint(low=1, high=7, size=3)
#np.random.seed(123)                                                          #Adding the seed gives the same value from the random generator
np.random.randint(low=1, high=7, size=3)

np.random.uniform(low = 1.0, high = 2.0, size = (2, 2))
np.random.binomial(10, 0.5, 20)
print(np.random.normal(loc=0,scale=1,size=2))
---------------------------------------------------------------------------

Unique
---------------------------------------------------------------------------
a=np.array([[1,3,3],[4,5,6],[7,8,9],[1,2,3]])
print(a)
a, indices, counts = np.unique(a,axis=0,return_index=True,return_counts=True)         #index and frequency of value
---------------------------------------------------------------------------

Transpose
---------------------------------------------------------------------------

a=np.array([[1,2],[3,4],[5,6]])                                                      #Takes the columns an puts it into an array. Flips the matrix
a.T
---------------------------------------------------------------------------

Reversing an array
---------------------------------------------------------------------------
a=np.array([[1,2,3],[7,3,1],[5,1,4]])

rows=np.flip(a,axis=0)                                                     #Flips all rows in each column   
columns=np.flip(a,axis=1)                                                  #Flips all columns in each row
---------------------------------------------------------------------------

Reshaping and flattening multidimensional arrays
---------------------------------------------------------------------------
a=np.array([[1,2,3,],[4,5,6]])
b=a.ravel()                                                                 #Ravel is a view, flatten is a copy
c=a.flatten()
---------------------------------------------------------------------------

Mean Square Error
---------------------------------------------------------------------------
a=np.array([[1,2,3,],[4,5,6]])


predicted = np.array([1,42,5,8,1,2])
actual = np.array([14,123,64,23,2,1])
mean_square_error = 1/3 * np.sum(np.square(predicted-actual))
---------------------------------------------------------------------------

How to save and load NumPy objects
---------------------------------------------------------------------------
a=np.array([1,2,3,4,5,6])
np.save('One-Six',a)                                                #Saves the array
b=np.load('One-Six.npy')                                            #Loads the array

np.savetxt('One-Six.cvs',a)                                         #Save the array as a cvs or text file
np.loadtxt('One-Six.cvs')                                           #Load the array as a cvs or text file
"""

a=np.array([12,3,43])
print(a)