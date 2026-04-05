# The collections module in Python is a built-in library that provides specialized container data types—basically more powerful alternatives to lists, tuples, and dictionaries.

# Tuple with named fields (like lightweight objects). Accessed based on name

from collections  import namedtuple

person = namedtuple('Person', ['name', 'age'])
s1 = person('Alex', 30)
print(s1)

