#
# Created by 하윤 on 2022/06/18.
#

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1
nx, ny = 1, 1
N = int(input())

cmd = list(input().split())

for i in range(len(cmd)):
    if cmd[i] == 'L':
        nx += dx[0]
        ny += dy[0]
    elif cmd[i] == 'R':
        nx += dx[1]
        ny += dy[1]
    elif cmd[i] == 'U':
        nx += dx[2]
        ny += dy[2]
    elif cmd[i] == 'D':
        nx += dx[3]
        ny += dy[3]
    if (nx <= 0 or ny <= 0) or (nx > N or ny > N):
        nx, ny = x, y
        continue
    x, y = nx, ny
    nx, ny = x, y
    print(x, y)
print(x, y)

