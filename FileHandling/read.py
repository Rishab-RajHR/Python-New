# File handling in Python means working with files (create, read, write, update, delete). It’s a very common interview and practical topic.

# To open a file
f = open("test.txt","r")
# data = f.read(2) => for reading limited characters
# data = f.read()
# print(data)

# For printing line by line
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()