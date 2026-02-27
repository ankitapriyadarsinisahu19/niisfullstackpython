X=10
def show():
	X=30
	print(X)
	print(locals()['X'])
	print(globals()['X'])
	globals()['X']
	X=60
show()
print(X)
