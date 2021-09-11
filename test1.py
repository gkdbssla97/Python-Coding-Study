# 큰 수의법칙 1번

N, M, K = map(int, input().split())

memo = []
data = list(map(int,input().split()))
data.sort(reverse = True)

cnt = 0
sum = 0

while True :
    sum += data[0]
    cnt += 1
    M -= 1
    #print(sum)
    if cnt == K :
        sum += data[1]
        M -= 1
        cnt = 0
    if M == 0 :
        break

print(sum)
print(data)
