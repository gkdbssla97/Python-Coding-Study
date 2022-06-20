#
# Created by 하윤 on 2022/06/20.
#

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=False)
B.sort(reverse=True)
#print(B[0])
for i in range(K):
    A[i] = B[i]
print(sum(A))