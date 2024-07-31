import numpy as np

#Rand() (0-1)
var=np.random.rand(3)
 #generates array with 3 random values between 0 and 1 
print(var)

var1=np.random.rand(2,5)
#generates the 2d array with 2 x5 dimensions random numbers
print(var1)

#Randn(close to 0)
var2=np.random.randn(5)
#creates random 5 integer close to 0
print(var2)

#ranf(0.0,1.0)
var3=np.random.ranf(5)
#generates the  5 integers less then 1 and greater or equal to 0 
print(var3)

#randint(min,max,total_values)
var4=np.random.randint(2,5,5)
#generates the  5 integers from 2 to 5 
print(var4)