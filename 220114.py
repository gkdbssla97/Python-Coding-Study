import sys

# summary = 0
# for i in range(1,10):
#     summary += i
# print(summary)
# # List comprehension
# array = [i for i in range(1,10) if i % 2 == 1]
# print(array)
# for i in range(1, 10):
#     if i % 2 == 1:
#         array.append(i)
# print(array)
# array.sort()
# array.sort(reverse=False)
# print(array)
#
# a = [1,2,3,4,5,5,5]
# remove_set = [3, 5]
# result = [i for i in a if i not in remove_set]
# print(result)
# result = [i for i in a if i in remove_set]
# print(result)
# data = sys.stdin.readline().rstrip()

import heapq

def heapsort(iterable):
    h = []
    result = []
    for val in iterable:
        heapq.heappush(h, val)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
def heapsort1(iterable):
    h = []
    result = []
    for val in iterable:
        heapq.heappush(h, -val)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort1([1,3,5,4])
print(result)

from bisect import bisect_left, bisect_right
# 정렬된 배열임을 강조
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 [left_value, right_value]인 데이터의 갯수를 반환하는 함수
def count_by_range(a, left_val, right_val):
    right_idx = bisect_right(a, right_val)
    left_idx = bisect_left(a, left_val)
    return right_idx - left_idx
print("-----")
# list declaration
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# Output the number of data with a value of 4
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

print("----")
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
data.pop()
data.popleft()
print(data)
print(list(data))
