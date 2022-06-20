#
# Created by 하윤 on 2022/06/20.
#
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(list(queue))

graph = [[] for _ in range(3)]
graph[0].append((1, 2))
graph[0].append((3, 4))
print(graph)

def bfs(graph, start, visited):
    queue = deque([start])