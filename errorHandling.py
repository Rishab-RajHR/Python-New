# Error handling lets your program avoid crashing and handle unexpected situations gracefully.

# a = int(input("Enter a number:"))
# b = 10/a
# print("Result:", b)


# try:
#    a = int(input("Enter a number:"))
#    b = 10/a
#    print("Result:", b)
# except:
#    print("Something went wrong")



# Specific Error

# try:
#    a = int(input("Enter a number:"))
#    b = 10/a
#    print("Result:", b)
# except ValueError:
#    print("Please Enter a valid number")
# except ZeroDivisionError:
#    print("You can't divided by Zero")



# Handle Multiple exception
# try:
#    a = int(input("Enter a number:"))
#    b = 10/a
#    print("Result:", b)
# except (ValueError, ZeroDivisionError):
#    print("Invalid Input")


# try except else
# try: 
#    num = int(input("Enter age"))
# except ValueError:
#    print("Invalid Input")
# else:
#    print("Your age is :", num)




# Fnally block use 

try:
  f = open("demo.txt")
  print(f.read())
except FileNotFoundError:
  print("File Not Found")
finally:
  print("Executed completed")