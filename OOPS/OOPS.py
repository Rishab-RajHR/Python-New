# Object-Oriented Programming (OOP) is a programming style where you organize code using classes and objects.

# a=10
# b=20
# sum=a+b
# print("The sum of a and b is:", sum)



# Functional Programming
# def hello():
#   print("Hello, world!")

# hello()



# OOPS => Class and Object

# class Student:
#   name = "Alex Pandian"

# s1 = Student()
# print(s1.name)


# class Car:
#   color = "Red"
#   modal = 2023

# car2 = Car()
# print(car2.color)
# print(car2.modal)



# constructor => __init__
# class Person:
#   def __init__(self):
#     print("Person created")

# p1 = Person()



# class Person:
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age
#       print("Person Created")

# p1 = Person("Alex", 30)
# print(p1.name)
# print(p1.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Person created")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Alex", 32)
p1.display()
# print(p1.name)
# print(p1.age)





