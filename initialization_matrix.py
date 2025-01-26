import numpy as np
zeroarray=np.zeros((3,3,2))#3D array of 3x3x2
print(zeroarray)
print()
onearr=np.ones((3,3,2),dtype='int32')#dtype='int32' is used to specify the data type of the array
#u can also use dtype='int64' or dtype='float32' or dtype='float64'
print(onearr)
print()
anyarr=np.full((2,3,2),14)#full() is used to create an array of specified shape and fill it with the specified value
print(anyarr)

