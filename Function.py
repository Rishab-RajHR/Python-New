# A function is a reusable block of code used to perform a specific task.



# Without Function

# num1 = 10
# num2 = 20
# sum = num1 + num2
# print("The 1st sum is:", sum)


# num1 = 1
# num2 = 2
# sum = num1 + num2
# print("The 2nd sum is:", sum)



# With the help of function

# Function without Parameter
def sum():
    num1 = 10
    num2 = 20
    sum = num1 + num2
    print("The sum is:", sum)
sum()
print("End of the function call")


# Function with Parameter
def sum1(a,b):
    print("The sum is:", a+b)
sum1(10,20)
sum1(1,2)
sum1(10,50)
print("End of the function call")


# Slight change from the above program
def sum2(a,b):
    add = a+b
    print("The sum is:", add)
sum2(10,20)
sum2(1,2)
sum2(10,50)
print("End of the function call")


# Function with return value
def sum(a,b):
    return a+b  # After return don't write return
add = sum(1,5)
print(add)


def print_hello():
    print("Hello, World!")
print_hello()


# Slight change from the above
def print_hello1():
    print("Hello, World!")
output = print_hello1()
print(output)  # None




#Without  Default Parameters
def multiply(a,b):
    print("The product is:", a*b)
    return a * b
output = multiply(10, 20)
print("The output of the multiply function is:", output)



# Default Parameters
def multiply(a=2,b=4):
    print("The product is:", a*b)
    return a * b
output = multiply()
print("The output of the multiply function is:", output)

# When we will pass the value then it will overide the default value
