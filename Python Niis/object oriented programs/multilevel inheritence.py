class person:
	def f1(self):
		print("Ram is a person")
class student(person):
	def f2(self):
		print("Ram is a student")
class engineeringstudent(student):
	def f3(self):
		print("Ram is an engineeringstudent")
ob = engineeringstudent()
ob.f1()
ob.f2()
ob.f3()

#parent class
class Person:
    def __init__(self, name, age):
        self.name = name         #property
        self.age = age

    def display_person(self):    #method
        print("Name:", self.name)
        print("Age:", self.age)

#child class
class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self, name, age)  #calling person constructor
        self.roll = roll                  #property

    def display_student(self):
        print("Roll Number:", self.roll)

#grand child class
class EngineeringStudent(Student):
    def __init__(self, name, age, roll, branch):
        Student.__init__(self, name, age, roll)
        self.branch = branch

    def display_engineering(self):
        print("Branch:", self.branch)


# Creating object
e1 = EngineeringStudent("Ram", 21, 101, "Computer Science")

e1.display_person()
e1.display_student()
e1.display_engineering()