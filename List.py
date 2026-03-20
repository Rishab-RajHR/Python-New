# List (similar to array0 is used to store a list of values   syntax : list = []

num1 = 10
num2 = 20
num3 = 30

print(num1, num2, num3)


# Instead of creating a lots of variable we use list

num = [1, "Alex", 4, 7.10, True]
print(num)
print(type(num))

# fruits = [] -> Empty list is also valid list


# Accessing the list of items

num1 = [10, 20, 45, 16]

print(num1[0]) # Accessing the first element
print(num1[1]) # Accessing the second element
print(num1[2]) # Accessing the third element
print(num1[3]) # Accessing the fourth element

print(len(num)) # Length of the list



# Changing list 
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

fruits[1] = 'blueberry'  # Change 'banana' to 'blueberry'

print(fruits) # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']


# Slicing
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# slicing
# list_num = [start_idx, end_idx] (end_idx not included)

print(fruits[1:4])