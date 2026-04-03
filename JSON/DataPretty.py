# For Reading from the file

import json

data = {
   "name": "Alex Pandian",
   "age": 24,
   "languages": ["Python", "JavaScript", "C++"],
   "is_trainer": True
}


print(json.dumps(data, indent=4)) # Pretty print JSON data