# JSON in Python is used to store and exchange data in a structured format (like dictionaries and lists in Python).

# Python provides a built-in module called json module to work with JSON data.

import json

data = {
   "name": "Alex Pandian",
   "age": 24,
   "languages": ["Python", "JavaScript", "C++"],
   "is_trainer": True
}

# Dictionary data convert to string
json_data = json.dumps(data)
print(json_data)