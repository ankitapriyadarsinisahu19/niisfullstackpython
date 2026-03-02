X=10
def show():
	X=30
	print(X)
	print(locals()['X'])
	print(globals()['X'])
	globals()['X']=50
	X=60
show()
print(X)
