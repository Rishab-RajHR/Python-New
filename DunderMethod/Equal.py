# __eq__(self, other) - For ==

class Book:
   def __init__(self,title):
      self.title = title
   def __eq__(self, other):
      return self.title == other.title
   
book1 = Book("1984")
book2 = Book("1984")
print(book1 == book2) 