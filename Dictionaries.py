# A dictionary is a key–value data structure in Python.
# word : meaning => key : value
# It is unordered list
# There is unique key


# Creating Dicitionaries
student = {
   "name" : "Alex Pandian",
   "age" : 20,
   "passed": True,
    "course": "Python Programming",
    "marks": [85, 90, 78, 92],
    "subjects": ("Python", "Data Structures", "Algorithm"),
}
print("Student Details", student)
print(type(student))
print(len(student))



# For accessing the Dictionaries
student1 = {
   "name" : "Alex Pandian",
   "age" : 20,
   "passed": True,
    "course": "Python Programming",
    "marks": [85, 90, 78, 92],
    "subjects": ("Python", "Data Structures", "Algorithm"),
}

print(student1["name"])
print(student1["subjects"])
print(student1.get("subjectData"))   # Will give none if not found




# For updating values in Dictionaries
student2 = {
   "name" : "Alex Pandian",
   "age" : 20,
   "passed": True,
    "course": "Python Programming",
}
student2["marks"] = 95
student2["age"] = 21
print(student2)



# For deleting values in Dictionaries
student3 = {
   "name" : "Alex Pandian",
   "age" : 20,
   "passed": True,
    "course": "Python Programming",
}

# del student3["course"]
# print(student3)

# student3.pop("age")
# print(student3)

student3.clear()
print(student3)




# Nested Dictionary => It is the dictionary inside the dictionary

user = {
   "user1" : {"name": "Alex", "Age": 30},
   "user2" : {"name": "Joe", "Age": 31},
}

# Accessing the Dictionary
print(user)


# Accessing the Nested Dictionary
print(user["user1"])


# Accessing the Nested Dictionary particular value
print(user["user1"]["name"])
 