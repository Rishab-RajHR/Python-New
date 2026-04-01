# __len__(self) - For len()

class Basket:
   def __init__(self, items):
      self.items = items
   def __len__(self):
      return len(self.items)
   
b = Basket(["apple", "banana", "cherry"])
print(len(b))   # Length will be 3