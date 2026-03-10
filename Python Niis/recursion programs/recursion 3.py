def sdtest(no):
	s=0
	while no!=0:
		r=no%10
		s=s+r
		no=no//10
	return s
print(sdtest(125))

s=0
def sdtest(no):
	global s
	if no!=0:
		r=no%10
		s=s+r
		no=no//10
		sdtest(no)
		return s
print(sdtest(125))