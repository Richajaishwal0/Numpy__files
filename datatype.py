import numpy as np

var=np.array([1,2,3,4])
print("Datatype: ",var.dtype)#int32

var=np.array([1,2.0,3,4])
print("Datatype: ",var.dtype) #float32

var=np.array(["richa",2,3,4])
print("Datatype: ",var.dtype)
# U11

#type conversion m1
x=np.array([1,2,3,4],dtype=np.int8)
print("Datatype: ",x.dtype)

#type conversion m2
x1=np.array([1,2,3,4],dtype="f")
print("Datatype: ",x1.dtype)
print(x1)
print(x)

#type conversion m3 using function
x1=np.array([1,2,3,4])
new=np.float32(x1)
print("Datatype: ",x1.dtype)
print("Datatype: ",new.dtype)
print(new)
print(x1)

#type conversion m4 using 'as type'
x1=np.array([1,2,3,4])
new_1=x1.astype(float)
print(new_1)
print(x1)