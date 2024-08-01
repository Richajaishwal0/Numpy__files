#indexing and slicing in numpy similar to list
import numpy as np
arr1=np.array([1,2,3])
print(arr1[2])
print(arr1[1:])

arr2=np.array([[1,2,3],[1,2,3]])
print(arr2[0,1])
print(arr2[0,0:2])

arr3=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(arr3[0,0,0])
print(arr3[0,1,0:2:2])
