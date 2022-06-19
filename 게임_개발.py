#
# Created by 하윤 on 2022/06/19.
#
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

N, M = map(int, input().split())
x, y, d = map(int, input().split())

game = []
for _ in range(N):
    game.append(list(map(int, input().split())))
game[x][y] = 1
direction = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turn_time, cnt = 0, 1

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    print(nx, ny)
    if nx < 0 or ny or nx >= N or ny >= M:
        continue
    if game[nx][ny] == 0:
        x, y = nx, ny
        game[x][y] = 1
        turn_time = 0
        cnt += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if game[nx][ny] == 1:
            break
        x, y = nx, ny

    turn_time += 1
print(cnt)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
