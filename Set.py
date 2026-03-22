# A set is an unordered, mutable, and unique-elements-only collection in Python.
# No Duplicates allowed


# Creating
my_set = {2,3,1,4,2,1,6,"Alex","Alex"}

print(my_set)
print(type(my_set))
print(len(my_set))



# Empty set 
my_set1 = set()

print(my_set1)
print(len(my_set1))



# Empty set Adding Values
my_set2 = set()
my_set2.add(1)
my_set2.add(2)

print(my_set2)
print(len(my_set2))



# Adding or removing values
num = {2,3,1,4}
# num.add(5)
num.remove(2)
print(num)


# Set is unordered because its ordered changes every time
num1 = {2,3,1,"Mohit",4}
print(num1)


# Discard means if element is not found there will be no error
num2 = {2,3,1,4}
# num2.discard(6)
# num2.pop()
num2.clear()
print(num2)



# Set Method
num3 = {2,3,1,4}
num4 = {1,2,3,4,5}


# num3.union(num4)
print(num3.union(num4))   # ignore duplicate and add

# num3.intersection(num4)
print(num3.intersection(num4))   # common value between two set
