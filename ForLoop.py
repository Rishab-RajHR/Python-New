# Used when you know how many times you want to repeat something.  In List Tuple

# for i in range(5):
#     print(i)


fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

for fruit in fruits:
  print(fruit)


# For Loops with List
nums = [1,2,3,4]

for num in nums:
  print(num)


# For Loop with String
name = "Alex"
for char in name:
  print(char)


# With else Loop
name1 = "Alex"
for char in name1:
  print(char)
else:
  print("End of for loop")


# With break statement
name2 = "Alex"
for char in name2:
   if char == 'e':
    print('Found e, breaking the loop')
    break
else:
  print("End of for loop")



# For Loop for the Range
for i in range(5):
   print(i)


# For Even Number
for j in range(5,10):
  if j%2 == 0:
    print(j,"Is Even")


# Nested For Loop in Range

for k in range(1,4):
  for l in range(1,3):
     print(f'k: {k}, l: {l}')



# pass when we don't want to execute the code
for t in range(4):
  pass




