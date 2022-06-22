#
# Created by 하윤 on 2022/06/22.
#
# dp로 풀어야할거 같은 문제
d = [0] * 30000
X = int(input())

for i in range(2, X + 1):
    d[i] = d[i-1] + 1 #max 값
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[X])

