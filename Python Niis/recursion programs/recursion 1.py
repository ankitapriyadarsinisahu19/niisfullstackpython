#with global variable
i=1
def show():
	global i
	print("A")
	i=i+1
	if i<=3:
		show()
	print("B")
def main():
	print("C")
	show()
	print("D")
main()



#without global variable
def show(i):
	print("A")
	if i<5:
		show(i+1)
	print("B")
def main():
	print("C")
	show(1)
	print("D")
main()



def show(i):
	print("A",i)
	if i<3:
		show(i+1)
	print("B",i)
def main():
	print("C")
	show(1)
	print("D")
main()