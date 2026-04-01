# __add__(self,other) - For + operator

class Numbers:
  def __init__(self,values):
    self.values = values
  def __add__(self,other):
    return Numbers(self.values + other.values)
  
num1 = Numbers(10)
num2 = Numbers(5)
result = num1 + num2
print(result.values)  