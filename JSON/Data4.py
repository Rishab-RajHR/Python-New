# For Reading from the file

import json

data = {
   "name": "Alex Pandian",
   "age": 24,
   "languages": ["Python", "JavaScript", "C++"],
   "is_trainer": True
}
with open("JSON/student.json", "w") as file:
   json.dump(data, file)
print("Data written to student.json")

with open("JSON/student.json", "r") as file:
   loaded_data = json.load(file)
print("Data loaded from student.json:", loaded_data)
print("Name:", loaded_data["name"])