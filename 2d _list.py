r=int(input("enter row"))
c=int(input("enter column"))
print("enter :")
l=[]
for i in range(r):
    x=[]
    print("enter elements of row:",(i+1))
    x=[int(input()) for i in range(c)]
    l.append(x)
        
print("the marix is:")
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()
