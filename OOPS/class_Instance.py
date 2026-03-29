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
      