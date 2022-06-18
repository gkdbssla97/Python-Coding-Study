#
# Created by 하윤 on 2022/06/18.
#
N, M = map(int,input().split())

result = 0
for _ in range(N):
    num = list(map(int, input().split()))
    min_val = 10001
    for a in num:
        min_val = min(a, min_val)
    result = max(min_val, result)
print(result)