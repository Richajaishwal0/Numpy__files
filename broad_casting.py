#broad casting in numpy operations like "+","-" cant be done incase the dimnsion is not same so broadcasting is done
#there must be ex: for shape (3,1) and (1,3) there is atleast one "1" in each combination or both the corresponding element must be same ie.corresponding element
import numpy as np
# arr=np.array([1,2,3,4])
# arr2=np.array([1,2,3])
# print(arr+arr2)

arr1=np.array([1,2,3])
arr2=np.array([[1],[2],[3]])
print (arr1)
print(arr2)
print()
print(arr1+arr2)


