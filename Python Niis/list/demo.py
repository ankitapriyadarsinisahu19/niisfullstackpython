L=[5,8,6,3,8,7,7,12]
L1=[]
for i in L:
	if i not in L1:
		L1.append(i)
print(L1)


s="welcome"
L=[]
for i in s:
	if i not in "aeiou":
		L.append(i)
print(L)