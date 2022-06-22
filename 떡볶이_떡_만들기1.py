#
# Created by 하윤 on 2022/06/22.
#

N, M = map(int, input().split())
DDK = list(map(int, input().split()))
start, end = 0, max(DDK)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in DDK:
        if x > mid:
            total += x - mid
    if total > M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)


