# List comprehension is a concise (short and readable) way to create a new list by applying an expression to each item in an iterable (like a list, tuple, or range), optionally with conditions.


# Without list comprehension

# nums = [1,2,3,4,5]
# square = []

# for n in nums:
#     square.append(n**2)
# print(square)



# With list comprehension

# nums = [1,2,3,4,5]
# square = [n**2 for n in nums if n % 2 == 0]
# print(square)


# For range
nums = [n for n in range(10) if n % 2 == 0]
print(nums)



# Real World Examples

# Convert string to character
chars = [char for char in "Alex"]
print(chars)


# Convert a list of celsius temperature to Fahrenheit
celsius = [0, 10, 20.1, 34.5, 100]
feh = [((9/5) * temp + 32) for temp in celsius]
print(feh)

# UpperCase a list of strings
names = ["mohit", "alex", "aman", "rohit"]
upper_names = [name.upper() for name in names]
print(upper_names)

