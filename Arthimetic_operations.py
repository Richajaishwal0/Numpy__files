#1d array
import numpy as np
arr=np.array([1,2,3,4])
print(arr)
#add
varadd=arr+3
print(varadd)

arr=np.array([1,2,3,4])
arr2=np.array([1,2,3,4])
print(arr)
#add
add=arr+arr2 # add=np.add(arr,arr2)
print(add)
#subtract 
add1=arr-arr2   #add1=np.subtract(arr,arr2)
print(add1)

#multiply
add3=arr*arr2 # add3=np.multiply(arr,arr2)
print(add3)

#divide
add4=arr/arr2 # add4=np.divide(arr,arr2)
print(add4)

#modulus  # ad5=np.mod(arr,arr2),power,reciprocal
add5=arr%arr2
print(add5)
#similar to the 1d array
arr=np.array([[1,2,3,4],[1,2,3,4]])
arr1=np.array([[1,2,3,4],[1,2,3,4]])
print(arr1+arr)

#Arthimetic functions in numpy

#min,max for 1d array
import numpy as np
arr=np.array([1,2,3,4])
print(np.min(arr))

#for 2d array
arr2=np.array([[1,2,3,4],[4,5,6,7]])
print(np.min(arr2,axis=0)) #axis =0 represents the comparision between the column and axi=1 means the comparision between the row

#argmin-->find the position of the corresponding min or max terms
print(np.argmin(arr))

#sqrt
print(np.sqrt(arr))

#sine and cosine
import numpy as np
arr=np.array([1,2,3,4])
print(np.sin(arr))

#cumsum similar to the logic of the  fibonacci series
import numpy as np
arr=np.array([1,2,3,4])
print(np.cumsum(arr))
