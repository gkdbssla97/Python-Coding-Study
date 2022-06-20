#
# Created by 하윤 on 2022/06/20.
#

from collections import deque
N, M = map(int, input().split())
monster = []

for _ in range(N):
    monster.append(list(map(int,input())))

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if monster[nx][ny] == 0:
                continue
            if monster[nx][ny] == 1:
                monster[nx][ny] = monster[x][y] + 1
                queue.append((nx, ny))

    return monster[N-1][M-1]


print(bfs(0, 0))