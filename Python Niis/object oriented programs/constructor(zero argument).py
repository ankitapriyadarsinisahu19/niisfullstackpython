class Demo:
	def __init__(self):
		self.x=5  #assign objects value
		self.y=7  #""
ob=Demo()
print(ob.x)
print(ob.y)



#create 2 objects:- it is a wrong process
class Demo:
	def __init__(self):
		self.x=10
		self.y=20
ob=Demo()
print(ob.x)
print(ob.y)
ob1=Demo()
print(ob.x)
print(ob.y)

#solutions:-
class Demo:
	def __init__(self):
		self.x=int(input())
		self.y=int(input())
print("enter object1 two values")
ob=Demo()
print("enter object2 two values")
ob1=Demo()
print("display first object values")
print(ob.x,ob.y)
print("display second object values")
print(ob1.x,ob1.y)

#rectangle
class rectangle:
	def __init__(self,l,b):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))
r=rectangle(length,breadth)
print("area=",r.area())


