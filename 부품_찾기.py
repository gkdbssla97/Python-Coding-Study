#
# Created by 하윤 on 2022/06/22.
#

def binary_search(N_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #print(mid)
        if N_list[mid] == target:
            return "yes"
        elif N_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))
for x in M_list:
    print(x)
    print(binary_search(N_list, x, 0, N - 1))

