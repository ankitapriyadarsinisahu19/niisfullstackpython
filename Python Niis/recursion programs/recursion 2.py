#display 1 to 10
def show(i):
	print(i)
	if i<10:
		show(i+1)
def main():
	show(1)
main()


#display 10 to 1
def show(i):
	if i<10:
		show(i+1)
	print(i)
def main():
	show(1)
main()