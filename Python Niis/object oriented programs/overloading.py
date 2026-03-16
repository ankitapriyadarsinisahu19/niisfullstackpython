class Demo:
	def show(self,a):
		print("one argument show",a)
	def show(self,b):
		print("two argument show",b)
	def show(self):
		print("no argument show")  #last show is acceptable.if u want to display all shows function then u should be use default parameter.
d=Demo()
d.show()
