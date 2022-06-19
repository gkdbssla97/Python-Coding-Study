#
# Created by 하윤 on 2022/06/19.
#

N = input()

kingdom = [[0] * 8 for _ in range(8)]
#print(kingdom)
pick_x = ord(N[0]) - 97
pick_y = int(N[1]) - 1
x, y = pick_x, pick_y
print(x, y)
move_types = ['N','E','W','S']
dx = [1, -1, 2, 2, -2, -2, 1, -1]
dy = [-2, -2, -1, 1, -1, 1, 2, 2]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue
    cnt += 1
print(cnt)

