#  deque (Double-ended queue) => Fast appends and pops from both ends.

from collections  import deque

dq = deque([1, 2, 3, 4, 5])
dq.append(6)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)