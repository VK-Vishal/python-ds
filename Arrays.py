from array import *
#sequencial data which stores the homogenious data types
#we can use negative index in array

n=int(input("enter the number of elements in aray:"))
print("enter the elements:")
arr=array('i',[int(input()) for i in range(n)])
print("the elements in list:")
l=[int(input()) for i in range(n)]
a=array('i',l)
print(arr*2,a*2,sep="\n")

''''



sample=array('i',[1,2,3,4,5,6,7,8])
samplefloat=array('f',[3.2,4.3])
print(sample,samplefloat,sep="\n")
for x in sample:print(x)




the data types mentioned can be used to create the array:
 
    
Type Code	C Type	         Python Type	Description
'b'	signed char	int	         Signed integer (1 byte)
'B'	unsigned char	         int	Unsigned integer (1 byte)
'u'	wchar_t	Unicode	         Unicode character (2 or 4 bytes)
'h'	signed short	         int	Signed integer (2 bytes)
'H'	unsigned short	         int	Unsigned integer (2 bytes)
'i'	signed int	int	         Signed integer (2 or 4 bytes)
'I'	unsigned int	         int	Unsigned integer (2 or 4 bytes)
'l'	signed long	int	         Signed integer (4 bytes)
'L'	unsigned long	         int	Unsigned integer (4 bytes)
'q'	signed long long	     int	Signed integer (8 bytes)
'Q'	unsigned long long	     int	Unsigned integer (8 bytes)
'f'	float	float	         Floating point (4 bytes)
'd'	double	float	         Floating point (8 bytes)

'''
