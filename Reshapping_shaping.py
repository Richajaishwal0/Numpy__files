#shape and re shapping in numy
import numpy as np
arr=np.array([[1,2,3,4],[1,2,3,4]])
print(arr)
print()
print(arr.shape)

#reshapping from one dimension to another
import numpy as np
arr=np.array([1,2,3,4])
x=arr.reshape(2,2)  #(first,second) where first is the no of rows of new array and the second is the no of element in one row ===the multiplication of first and second must be the dimension of the array
print(x)
print(x.shape)
print(x.ndim)
print()
#three dimension
arr1=np.array([1,2,3,4,5,6,7,8,9,2,4,5])
x1=arr1.reshape(2,3,2)  #(first,second,third) where first is the no of rows of new array and the second is the no of element in one row ===the multiplication of first and second must be the dimension of the array
print(x1)
print(x1.shape)
print(x1.ndim)

#three dimension to one dimension
arr1=np.array([[[1, 2],[3, 4],[5, 6]],[[7, 8],[9, 2],[4 ,5]]])
x1=arr1.reshape(-1)  # USE -1
print(x1.shape)
print(x1.ndim)
