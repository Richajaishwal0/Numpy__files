import numpy as np
x=[[1,2,3,4,5],[1,2,3,4,5]]
arr=np.array(x) #convert the list into array
print(arr)
print(arr.ndim) #PRINT THE DIMENSION OF THE ARRAY
rn=np.array(arr,ndmin=10) #SET THE DIMENSION OF THE ARRAY
print(rn)

