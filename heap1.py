import heapq

arr = []
heapq.heappush(arr, 10)
heapq.heappush(arr, 20)
#heapq.heappop(arr)
heapq.heappush(arr, 15)
heapq.heappush(arr, 12)
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))
print(arr)