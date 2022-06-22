#
# Created by 하윤 on 2022/06/22.
#

N, M = map(int, input().split())
H = 0
DDK = list(map(int, input().split()))
max_val = max(DDK)
sum = 0
for i in range(max_val, 0, -1):
    #print(f'max:{i}')
    for x in DDK:
        #print(x)
        result = x - i
        if result >= 0:
            sum += result
    #print(f'sum:{sum}')
    if sum == M:
        H = i
        break
    sum = 0
print(H)

