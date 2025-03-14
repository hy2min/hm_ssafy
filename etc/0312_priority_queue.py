# 우선순위 큐
# from queue import PriorityQueue  # 알고리즘 PS 분야에서는 잘 쓰지 않음. 속도가 느림

import heapq

# 1.  원본 데이터 날라감
# arr = []
# heapq.heappush(arr, 4)  # 리스트에 heap 자료구조의 규칙에 의거해서 자료를 저장
# heapq.heappush(arr, 6)
# heapq.heappush(arr, 1)
# heapq.heappush(arr, 2)
# heapq.heappush(arr, 3)
#
#
# # for i in range(len(arr)):
# #     print(heapq.heappop(arr), end=" ")  # heap 규칙에 따라 출력
# # 저장 출력 둘다 시간복잡도-O(NlogN)
#
# while arr:
#     temp = heapq.heappop(arr)
#     print(temp, end=" ")

# # 루트의 우선순위가 중요함

# # 2.  원본 데이터 날라가지 않게
# arr = [3422, 5, 3, 1, 5]
# heap = []
# for i in range(len(arr)):
#     heapq.heappush((heap,arr[i]))
#
# for i in range(len(arr)):
#     print(heapq.heappop((heap), end=" ")

arr = [3422, 5, 3, 1, 5]
heapq.heapify(arr)  # heap 기준으로 정렬
print(arr)

for i in range(len(arr)):
    print(heapq.heappop(arr), end=" ")


