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
print(student2)
 