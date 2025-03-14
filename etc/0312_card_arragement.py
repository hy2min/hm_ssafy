import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]


heapq.heapify(arr)
ans = 0
while len(arr) > 1:
    temp1 = heapq.heappop(arr)
    temp2 = heapq.heappop(arr)
    ans += temp1 + temp2
    heapq.heappush(arr, temp1+temp2)
print(ans)