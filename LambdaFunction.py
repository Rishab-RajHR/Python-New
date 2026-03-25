# A lambda function in Python is a small, anonymous (unnamed) function defined using the lambda keyword. It’s typically used for short, one-line operations where defining a full function using def is unnecessary.


# lambda arguments: expression
# f = lambda a: a*a

add = lambda x,y : x+y
print(add(10,20))


# Normal Function
def add_func(a,b):
   return a+b
print(add_func(10,20))



# Lambda function with map
nums = [1, 2, 3, 4, 5]
# squared_nums = list(map(function,iteration))
add = list(map(lambda x: x+2, nums))
print(add)


# Lambda function with filter
nums1 = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x%2 == 0, nums1))
print(evens)


# Using loop
nums2 = [1, 2, 3, 4]
product = 1
for num in nums2:
   product = product * num
print(product)


# Lambda function with reduce
from functools import reduce

nums3 = [1, 2, 3, 4]
product1 = reduce(lambda x,y: x*y, nums3)
print(product1)