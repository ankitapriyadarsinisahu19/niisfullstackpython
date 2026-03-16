print("main start")
L=[10,20,30]
try:
	print(L[2]//2)
except IndexError as e:
	print("hii",e)
except ZeroDivisonError as e:
	print("bye",e)
except:
	print("handle all exception")
print("main end")