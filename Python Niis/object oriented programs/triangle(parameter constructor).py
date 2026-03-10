class Triangle:
	def __init__(self,base,height):
		self.base=base
		self.height=height
	def area(self):
		return 0.5*self.base*self.height
base=float(input("enter base:"))
height=float(input("enter height:"))
T=Triangle(base,height)
print("area=",T.area())
