import heapq

# 1. 음수 붙여서 heap 정렬 후 -1 곱해서 maxheap
arr = [3422, 5, 3, 1, 5]
heap = []
# for i in range(len(arr)):
#     heapq.heappush(heap, -arr[i])
# print(heap)
# for i in range(len(arr)):
#     # print(heapq.heappop(heap)*(-1), end=" ")
#     print(-heapq.heappop(heap), end=" ")

# 2. 튜플로 저장 후 1번 인덱스를 출력하는 방법
# for i in range(len(arr)):
#     heapq.heappush(heap,(-arr[i],arr[i]))  # 튜플 상태로 저장
#
# print(heap)
#
# for i in range(len(arr)):
#     print(heapq.heappop(heap)[1], end=" ")

# 3.heapify
heap = list(map(lambda x:-x,arr))
heapq.heapify((heap))
for i in range(len(arr)):
    print(-heapq.heappop(heap), end=" ")




