class square:
	def __init__(self,side_length):
		self.side_length=side_length
	def show(self):
		print("side_length=",self.side_length)
	def area(self):
		return self.side_length**2
	def perimeter(self):
		return 4*self.side_length
side_length=int(input("enter sides:"))
s=square(side_length)
print("area=",s.area())
print("perimeter=",s.perimeter())