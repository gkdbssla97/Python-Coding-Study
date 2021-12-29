from collections import deque

q = deque([1,2,3])
q.append(10)
q.append(20)
q.append(30)

while q:
    print(q.popleft())