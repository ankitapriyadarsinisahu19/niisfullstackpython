def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=facttest(3)+facttest(4)+facttest(5)
print("3!+4!+5!",s)



def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=0
for i in range(3,6,1):
	s=s+facttest(i)
print("3!+4!+5!=",s)


