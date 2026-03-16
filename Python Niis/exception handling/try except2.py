print("main start")
try:
	print(10//2)
	print("try end")
except ZeroDivisonError:
	print("caught")
print("main end")

#or
print("main start")
try:
	print(10//2)
	print("try end")
except exception:
	print("caught")
print("main end")

#or

print("main start")
try:
	print(10//2)
	print("try end")
except BaseException:
	print("caught")
print("main end")
