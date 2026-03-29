# Abstraction is about hiding complexity — showing only what's necessary and concealing the implementation details.

class Vehicle:
    def __init__(self):
        self.engine = False
        self.brk = False
    
    def start_engine(self):
        self.engine = True
        self.brk = True
        print("Engine started.")

car1 = Vehicle()
car1.start_engine()




# Using Abstract Base Class (ABC) to achieve abstraction in Python

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car started.")

car = Car()
car.start_engine()