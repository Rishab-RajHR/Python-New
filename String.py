# str1 = "My name is Mohit Decodes"
# str2 = 'My name is Mohit Decodes'
# str3 = """My name is Mohit Decodes"""

# print(str1)
# print(str2)
# print(str3)


# Escape sequence character
str1 = "My name is\nMohit Decodes"
print(str1)


# Concatenation => adding two strings
tr1 = "My name is"
tr2 = "Alex Pandian"

finalStr = tr1+" "+tr2
print(finalStr)


# String Length
tr3 = "My name is Alex"
tr4 = "Pandian"
print(len(tr3)+len(tr4))




# Indexing => starts from 0
tr5 = "Alex"
print(tr5[0])

# tr5[0] = "X"
# print(tr5[0])   => This will give an error



# Slicing => to cut from startIndex to endIndex
# tr6[startIndex:endIndex-1]
tr6 = "Alex Pandian"
tr6[1:4]
print(tr6[1:4])
print(tr6[:4])
print(tr6[1:])
print(tr6[:])
print(tr6[-3:-1])



# String Function => Capitalize
hr = "my name is basil"
print(hr.capitalize())
print(hr.upper())
print(hr.lower())
print(hr.endswith("basil"))
print(hr.replace("basil", "Tovino"))
print(hr.find("name"))
print(hr.count("name"))



name = input("Enter your name: ")
print(f'your name is uppercase: {name.upper()}')
print(f'your name has {len(name)} characters')
