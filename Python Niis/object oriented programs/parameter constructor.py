class Demo:
	def __init__(self,x,y):
		self.x=x
		self.y=y
ob=Demo(5,7)
ob1=Demo(10,20)
print("display first object values")
print(ob.x,ob.y)
print("display second object values")
print(ob1.x,ob1.y)




#one object creation taking from keyboard input using parameter constructor:-
class Demo:
	def __init__(self,x,y):
		self.x=x
		self.y=y
print("enter two values")
ob=Demo(int(input()),int(input()))
print("display first object values")
print(ob.x,ob.y)



#initialization through method to create instance variable:-
class Demo:
	def set(self,x,y):
		self.x=x
		self.y=y
print("enter two values")
ob=Demo()
ob.set(10,20)
print("display first object values")
print(ob.x,ob.y)