#capitalize
s="ram Is a Good Boy"
s=s.capitalize()
print(s)


#title
s="ram Is a Good Boy"
s=s.title()
print(s)



#upper
s="ram Is a Good Boy"
s=s.upper()
print(s)



#lower
s="ram Is a Good Boy"
s=s.lower()
print(s)



#casefold
s="ram Is a Good Boy"
s=s.casefold()
print(s)



#swapcase
s="ram Is a Good Boy"
s=s.swapcase()
print(s)


#lstrip
s="   ram Is a Good Boy"
print(len(s))
s=s.lstrip()
print(len(s))



#rstrip
s="ram Is a Good Boy    "
print(len(s))
s=s.rstrip()
print(len(s))




#strip
s="     ram Is a Good Boy     "
print(len(s))
s=s.strip()
print(len(s))


s="welcome"
print(s.center(10,"*"))
print(s.ljust(10,"*"))
print(s.rjust(10,"*"))


#count
s="welcome"
print(s.count("e"))
print(s.count("welcome"))


#index
s="welcome"
print(s.index("e",0,7))
print(s.index("c",2,6))


#rindex





#find & rfind
s="welcome"
print(s.find("e"))
print(s.find("e"))
print(s.rfind("e"))



#startswith
s="ram is a good boy"
print(s.startswith("ram",0))
print(s.startswith("ram",4))


#endswith
s="ram is a good boy"
print(s.endswith("boy",4))
print(s.endswith("boy",6))

#split
s="ram is a good boy"
L=(s.split("o"))
print(L)
L=(s.split("a"))
print(L)
L=(s.split())
print(L)


#join
s="ram is a good boy"
L=s.split()
s1=" ".join(L)
print(L)
print(s1)


#replace
s="ram is a good boy"
s=s.replace("good","x")
print(s)


#encode & decode
s="ram"
b=s.encode()
print(b)
s1=b.decode()
print(s1)