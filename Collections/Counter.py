# Counter => Counts frequency of elements.
from collections import Counter

text = 'apple banana apple orange banana apple'
count = Counter(text)
print("Word counts:", count)
print(count['p'])  # For counting particular character