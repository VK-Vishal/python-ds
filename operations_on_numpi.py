import numpy as np
arr=np.array([list(range(1,6)),list(range(6,11)),list(range(11,16))])
print(arr)#print array
print(arr.ndim)#no of dimensions
print(arr.shape)#no of rows and columns
print(arr.size)#no of elements
print(arr.itemsize)#no of bytes required to store one element
print(arr.dtype)#data type
print(arr.data)#memory location
print(arr.ctypes)#c type array
print(arr.strides)#no of bytes to jump to get to the next element
print(arr[1,3])#print specific element
print(arr[1,:])#print specific row
print(arr[1,1::2])#print specific elements
print(arr[1,::-1])#print specific elements in reverse order

print(arr[:,2])#print specific column
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i,j],end=" ")
    print()
