L=[10,20,30,40,50]
del L[1]
print(L)


L=[10,20,30,40,50]
L[1:3:1]=[15,17,18]
print(L)


L=[10,20,30,40,50]
L[1:1:1]=range(5)
print(L)


L=[10,20,30,40,50]
L[5:5:1]="hii"
print(L)


#insert multiple value
L=[10,20,30,40,50]
L[1:1:1]=[15,17,18]
print(L)

L=[10,20,30,40,50]
#L[2:4]="hii" (error)
L[-3:-1:1]="hii"
print(L)