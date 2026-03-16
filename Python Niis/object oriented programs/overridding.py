class p:
	def property(self):
		print("land,money,car")
	def marry(self):
		print("sita")
class c(p):
	def marry(self):
		print("gita")
ob=c()
ob.property()
ob.marry()



class p:
	def property(self):
		print("land,money,car")
	def marry(self):
		print("sita")
class c(p):
	def marry(self):
		super().marry()
		print("gita")
ob=c()
ob.property()
ob.marry()