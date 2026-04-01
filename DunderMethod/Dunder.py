# n Python, “dunder” stands for “double underscore” methods — methods that start and end with __. They are also called magic methods or special methods.


"""
__init__(self,...) - Constructor
__str__(self) - For print()
__len__(self) - For len()
__add__(self,other) - For + operator
__eq__(self, other) - For ==
_getitem__(self, index) - For index
"""



# __init__(self,...) - Constructor

class Person:
  def __init__(self,name): 
    self.name = name
  def __str__(self):
    return f"Person: {self.name}"
  
p = Person("Alex")
print(p) # This will call __str__ and Print : "Alex"