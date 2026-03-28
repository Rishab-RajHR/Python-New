# An iterator is an object that allows you to traverse (loop through) elements one by one using methods like __iter__() and __next__().

# An iterator returns  element one by one
num = [10,20,30]
it = iter(num)
print(next(it))
print(next(it))
print(next(it))


# Custom iterator using __iter__() and __next__()

class CountUpto:
   def __init__(self,max):
      self.max = max;
      self.current = 1
   def __iter__(self):
      return self
   def __next__(self):
       if self.current <= self.max:
          value = self.current
          self.current += 1
          return value
       else:
          return StopIteration

for i in CountUpto(5):
   print(i)





# A generator in Python is a special type of function that returns values one at a time using the yield keyword, instead of returning all values at once like a normal function.

# Uses yield instead of return
# Generates values on demand (lazy evaluation)
# Maintains state between iterations
# Implements iterator automatically

def count_up_to(n):
   count = 1
   while count <= n:
      yield count
      count += 1
      

for num in count_up_to(5):
   print(num)