#
# Created by 하윤 on 2022/06/24.
#

N = int(input())
food = list(map(int, input().split()))

d = [0] * 1001
# sum1, sum2 = 0, 0
# i = 0
# while i < N:
#     sum1 += food[i]
#     i += 2
# i = 1
# while i < N:
#     sum2 += food[i]
#     i += 2
# result = max(sum1, sum2)
# print(result)
d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + food[i])
print(d[N-1])