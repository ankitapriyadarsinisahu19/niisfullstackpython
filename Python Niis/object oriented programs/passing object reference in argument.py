class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
def show():
		s=student("Ankita",1,85.50)
		return s
res=show()
print("my name=",res.name)
print("my roll=",res.roll)
print("my mark=",res.mark)