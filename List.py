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




# Slicing List
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# slicing
# list_num = [start_idx, end_idx] (end_idx not included)

print(fruits[1:4])
print(fruits[:4])
print(fruits[1:])
print(fruits[-3:-1])



# Useful Methods

num3 = [10,30,80,12]
num3.append(50)
print(num3)


# remove method 
num4 = [10,30,80,12]
num4.remove(30)
print(num4)


# For removing entire list
num5 = [10,30,80,12]
num5.clear()
print(num5)


# through indexing
num6 = [10,30,80,12]
num6.pop(2)
print(num6)


# For inserting at particular position
num7 = [10,30,80,12]
num7.insert(2, 100)
print(num7)


# For sorting getting the element in ascending order
num8 = [10,30,80,12]
num8.sort()
print(num8)

# We can also do sorting in string
num9 = ['b', 'c', 'd', 'e', 'a']
num9.sort()
print(num9)



# We can also do sorting in string in descending order
num10 = ['b', 'c', 'd', 'e', 'a']
num10.sort(reverse=True)
print(num10)