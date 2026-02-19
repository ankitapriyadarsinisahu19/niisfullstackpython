print(2**3**2)
print(10*3//4)
a=10
print(id(a))
print(a)
b=10
print(id(b))
print(b)
print(id(10))


a=10
a=b
print(id(a),id(b))
print(a,b)


a=10
print(id(a),a)
a=20
print(id(a),a)


#swapping 2 variable using 3rd variable
a=10
b=20
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)


#swapping 2 variable without using 3rd variable
a=10
b=20
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)

#using another method
a=10
b=20
a,b=b,a
print(a,b)


a=10
b=2.5
c="hii"
print(a,b,c)
a,b,c=10,2.5,"hii"
print(a,b,c)
a=10,2.5,"hii"
print(a)
print(type(a))

#swapping 3 no left to right with 4 th variable

a=10
b=20
c=30
print("before swapping a=",a,"b=",b,"c=",c)
t=c
c=b
b=a
a=t
print("after swapping a=",a,"b=",b,"c=",c)

#add 2 no without using + operator
a=10
b=20
c=a--b
print(c)

print(10<40<20)
print(3!=4)

print("e" in "hello")
print("e" not in "hlo")
print("e" not in "hello")

#identity operator
a=10
b=10
print(a is b)
print(a is c)
print(a is not c)
print(a==b)
print(a!=b)


a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)
print(a!=b)





#swapping
a=20
b=30
print("before swapping a=",a,"b=",b)
t=b
b=a
a=t
print("after swapping a=",a,"b=",b)

#swapping without 3rd variable
a=10
b=20
print("before swapping a=",a,"b=",b)
a=a+b
print("a=",a)
b=a-b
print("b=",b)
a=a-b
print("a=",a)
print("after swapping a=",a,"b=",b)



a=5
b=9
c=20
print("before swapping a=",a,"b=",b,"c=",c)
t=a
print("a=",a)
a=b
print("b=",b)
b=c
print("c=",c)
c=t
print("after swapping a=",a,"b=",b,"c=",c)


#swapping
a=8
b=7
c=10
a=c,b=b,c
print("a=",a,"b=",b,"c=",c)



a=1
b=5
c=2
a=b
b=c
c=a
print("a=",a,"b=",b,"c=",c)