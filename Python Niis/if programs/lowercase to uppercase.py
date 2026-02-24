import sys
print("enter a char")
ch=input()
if len(ch)>1:
	print("one char allow")
	sys.exit()
if ch>='a' and ch<='z':
   ch=chr(ord(ch)-32)
   print(ch)