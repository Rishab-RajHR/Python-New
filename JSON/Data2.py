# Covert string to json (deserialize)

import json

json_data = '{"name": "Alex Pandian","age": 24,"languages": ["Python", "JavaScript", "C++"],"is_trainer": true}'
python_data = json.loads(json_data)
print(python_data)