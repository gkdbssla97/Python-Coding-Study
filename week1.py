# 48 217
# N, M, K = map(int, input().split())

# memo = []
# for _ in N :
#     memo.append(int.input())

array = [i for i in range(20) if i % 2 == 1]
print(array)

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

a = [1,2,3,4,5,5,5]
remove_all = [3,5]

result = [i for i in a if i not in remove_all]
print(result)

a = 0
def func() :
    global a
    a += 1

for _ in range(10) :
    func()
print(a)