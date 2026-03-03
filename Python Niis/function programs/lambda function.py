res=lambda x:x*x
print(res(3))


#check even odd 
check=lambda n:"even" if n%2==0 else "odd"
print(check(10))
print(check(5))


#calculate simple intrest
show=lambda p,t,r :p*t*r/100
print(show(4000,2,3))


numbers=[1,2,3,4,5]
result=list(map(lambda x: x*2,numbers))
print(result)


#lambda with filter:-
numbers=[1,2,3,4,5,6]
even=list(filter(lambda x: x%2==0,numbers))
print("even")

#reduce
from functools import reduce
numbers=[1,2,3,4]
result=reduce(lambda a,b:a+b,numbers)
print(result)