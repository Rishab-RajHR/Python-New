# Polymorphism means “many forms” — the same function or method behaves differently depending on the object.

# print (len("Alex")) 
# print (len([1, 2, 3, 4, 5])) 
# print (len({"a": 1})) 


class Bird:
    def make_sound(self):
        print("Chirp")

class Cat:
    def make_sound(self):
        print("Meow")

for animal in [Bird(), Cat()]:
    animal.make_sound() # Output : Chirp, Meow



# Polymorphism and Inheritance together

class Employee:
    def work(self):
        print("Employee working")
class Developer(Employee):
    def work(self):
        print("Developer coding")
class Manager(Employee):
    def work(self):
        print("Manager is managing")

for emp in [Developer(), Manager()]:
    emp.work() # Output: Developer coding, Manager is managing