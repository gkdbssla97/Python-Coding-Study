#
# Created by 하윤 on 2022/06/20.
#
N, M = map(int, input().split())
ice = []

for _ in range(N):
    ice.append(list(map(int,input())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

#print(ice)


result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)