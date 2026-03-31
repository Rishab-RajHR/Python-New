# Inheritance allows one class (child class) to acquire properties and methods of another class (parent class).


class Parent:
    def speak(self):
        print("Speaking from Parent class")

class Child(Parent):
    pass

c = Child()
c.speak() # This will call the speak method from the Parent class, demonstrating inheritance.



class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
c  = Cat()
d.speak()  # Output: Dog barks
c.speak()  # Output: Cat meows