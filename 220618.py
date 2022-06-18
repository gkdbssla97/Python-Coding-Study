N, M, K = map(int,input().split())

num = list(map(int, input().split()))

#max_num = max(num)
sum, cnt = 0, 0

num.sort()
num.reverse()
i = 0
while i < M:
    i += 1
    if cnt == K:
        cnt = 0
        sum += num[1]
        print(num[1])
    else:
        print(num[0])
        sum += num[0]
        cnt += 1

print(sum)
