class person:
    count = 0 #class variable
    def __init__(self, name, age):
        self.name = name #instance variable
        self.age = age
        person.count += 1 #accessing the class variable using the name of the class
    
    def greet(self):
        print("Hello, my name is " + self.name)
        print("Hello, my age is " + str(self.age))

person1 = person("Tony", 26)
#person1.greet()
person2 = person("Dylan", 12)
print(str(person.count))


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))

employee1 = employee("Sarah", 48937)
employee2 = employee("Steve", 53892)
employee1.display()
employee2.display()

#counting the number of objects in a class

class student:
    count = 0
    def __init__(self):
        student.count += 1

s1 = student()
s2 = student()
s3 = student()

print("number of students are ", student.count)

#default consturctor
class Student:
    count = 100
    name = "Dylan"

    def display(self):
        print(self.count, self.name)

s5 = Student()
s5.display()

#multiple constructor in a single class
class Program:
    def __init__(self):
        print("First Constructor")
    def __init__(self):
        print("second Constructor")

P = Program()



# built-in class attributes
class newclass:
    def __init__(self, name, id, age):
        self.name = name
        self.age = age
        self.id = id    
    
    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

nc = newclass("Tommy", 1754353, 19)
print(nc.__doc__)
print(nc.__dict__)
print(nc.__module__)