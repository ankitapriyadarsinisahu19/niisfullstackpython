L=[10,20,30,40,50]
for i in L:
	print(i)


L=[10,20,30,40,50]
for i in range(0,len(L),1):
	print(L[i])

#adding 3 in each elements:-
L=[10,20,30,40,50]
for i in range(0,len(L),1):
	L[i]=L[i]+3
print(L)


L=[5,8,6,3,4,12]
L1=[]
for i in range(0,len(L),1):
	if L[i]%2==0:
		L1.append(L[i])
print(L1)


L=[5,8,6,3,8,7,7,12]
L1=[]
for i in L:
	L1=[i for i in L]
	print(L1)


L=[5,8,6,3,8,7,7,12]
L1=[]
for i in L:
	L1.append(i+3)
	print(L1)


L=[5,8,6,3,8,7,7,12]
L1=[]
for i in L:
	L1=[i+3 for i in L]
	print(L1)


L=[4,8,7,12,3,1]
L1=[i+3 for i in L if i%2==0]
print(L1)


L=[5,8,6,3,8,7,7,12]
i=0
while i<len(L):
	if L(i)%2==0:
		L.remove(L[i])
	else:
		i+=1
print(L)