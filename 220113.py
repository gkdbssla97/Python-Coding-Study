from collections import deque

N, M = map(int, input().split())

ice = []
for i in range(N):
    ice.append(list(map(int, input())))
visited = [False * N for range in (M)]
def dfs(x, y):
    if x<= -1 or x >= N or y <= -1 or y >= M:
        return False
    nx = x +
    elif N > x >= 0 and M > y >= 0 and visited[nx][ny] == 0:
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
