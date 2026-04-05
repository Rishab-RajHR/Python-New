# defaultdict => Dictionary with default values for missing keys.

from collections import defaultdict

score = defaultdict(int)
score['math'] = 60
score['science'] = 55
print(score)