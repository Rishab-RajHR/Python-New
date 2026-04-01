# _getitem__(self, index) - For index

class MyList:
  def __init__(self,data):
      self.data = data
  def __getitem__(self, index):
     return self.data[index]
  
m1 = MyList([1, 2, 3, 4, 5])
print(m1[2])