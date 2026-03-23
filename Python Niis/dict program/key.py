d={1:"A",2:"B",4:"C",3:"E"}
print(d.keys())


d={1:"A",2:"B",4:"C",3:"C"}
for i in d.keys():
	print(i,d[i])

#or

d={1:"A",2:"B",4:"C",3:"C"}
for k,v in d.items():
	print(k,v)