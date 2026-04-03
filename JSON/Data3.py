# To save and make the file

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