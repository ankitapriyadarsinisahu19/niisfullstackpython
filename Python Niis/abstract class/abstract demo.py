from abc import *
class Demo(ABC):
	@abstractmethod
	def show(self):
		pass
class Demo1(Demo):
	def show(self):
		print("hii")
d1=Demo1()
#d1=Demo() error
d1.show()



from abc import *
class Demo(ABC):
	@abstractmethod
	def show(self):
		pass
	def __init__(self):
		print("constructor")
	def disp(self):
		print("okk")
class Demo1(Demo):
	def show(self):
		print("hii")
d1=Demo1()
#d1=Demo() error
d1.show()
d1.disp()


