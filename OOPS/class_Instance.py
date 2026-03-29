# A class is a blueprint, and an instance is an actual object created from that blueprint.

# class.attr => class attribute
# obj.attr => instance attribute

class Car:
   car_company = "TATA"   # class attribute
   def __init__(self, model, color):
       self.model = model
       self.color = color
       print("Car created")

s1 = Car("Nexon", "Red")
print(s1.model, s1.color)
s2 = Car("Safari", "Black")
print(s2.model, s2.color)
print(Car.car_company) # Accessing class attribute using instance
      



# Methods are functions defined inside a class. They are used to perform operations on the data contained in the class. Methods can be called on instances of the class to manipulate or retrieve information about the instance.

class Student:
    def __init__ (self, name):
        self.name = name

    def hello(self):
        print("Hello, self.name")

s1 = Student("Alex")
print(s1.name)
s1.hello()



# Static method => does not take self as parameter
class Student:
     @staticmethod #decorator
     def college():
         print("I am from DU")

Student.college() # Calling static method without creating an instance