# loops are used to repeat a block of code multiple times ( repeatation )


# Without Loop
print(1)
print(2)
print(3)


# While Loop => Used when you want to repeat something until a condition becomes false.
num = 1
while num <= 10:
  print(num)
  num += 1
print("Loop finished")


# In Reverse Order
num1 = 10
while num1 >= 1:
  print(num1)
  num1 -= 1
print("Loop finished")



# Infinite times loop will execute
# while True:
#    print("ALex Pandian")
# print("End of Loop")



# break statement terminates the loop
i = 1
while i <= 5:
   print(i)
   if i == 3:
      break
   i += 1
print("Loop ended")


# continue statement skips the current iteration

j = 0
while j < 5 :
   if j == 3:
      j += 1
      continue
   print(j)
   j += 1
print("Loop ended")