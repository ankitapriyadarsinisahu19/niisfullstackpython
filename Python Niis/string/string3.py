#wap take a string from keyword found of charecter number of alphabet ,lowecase ,uppercase,consonent ,vouwel,digit,spce ,symbol ,word
print("Enter a String")
s=input()
c,alp,up,lw,vw,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
	c=c+1
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up=up+1
		else:
			lw=lw+1
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			co=co+1
	elif i.isdigit():
		dg=dg+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
wd=sp+1
print("No of Char=",c)
print("No of Alphabet=",alp)
print("No of Lowercase=",lw)
print("No of Uppercase=",up)
print("No of Vowel=",vw)
print("No of Consonent=",co)
print("No of Digit=",dg)
print("No of Space=",sp)
print("No of Symbol=",sy)
print("No of Word=",wd)