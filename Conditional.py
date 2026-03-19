# Example If you are above 18 you can give vote

# if , elif , else
age = 16
if (age >= 18):
  print("You are an adult.")
else:
  print("You are a minor.")

# With Boolean Condition
age = 16
if (True):
  print("You are an adult.")
else:
  print("You are a minor.")


# if elif else
marks = 95
if (marks >= 90):
  print("Grade A")
elif (marks >= 80):
  print("Grade B")
elif (marks >= 70):
  print("Grade C")
elif (marks >= 60):
  print("Grade D")
elif (marks >= 50):
  print("Grade E")
else:
  print("Grade F")



# Nested Conditions => condition inside condition
num = 10
if num > 0:
  print("Positive")
  if num % 2 == 0:
    print("Even")