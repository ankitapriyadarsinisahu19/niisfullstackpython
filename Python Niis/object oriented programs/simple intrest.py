class si:
	def __init__(self,p,t,r):
		self.principle=p
		self.time=t
		self.rate=r
	def show(self):
		print("principle=",self.principle)
		print("time=",self.time)
		print("rate=",self.rate)
	def sical(self):
		return self.principle*self.time*self.rate/100
i1=si(1000,2,10)
i1.show()
print("simple intrest=",i1.sical())