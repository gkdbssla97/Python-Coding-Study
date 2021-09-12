import sys
N, M = map(int, input().split())

value = 0

for i in range(N) :
    memo = list(map(int, input().split()))
    min_data = min(memo)
    value = max(min_data, value)

print(value)