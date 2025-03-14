arr = [(1,5), (1,9), (4,2)]
# 우선순위 조건 1. 첫번째 원소 내림차순
# 우선순위 조건 2. 두번째 원소 오름차순
# 4 2
# 1 5
# 1 9


# 조건을 커스터마이즈하기 위해서는 클래스 필요


import heapq

class Node:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __lt__(self, other):  # less than < 작다 : self - 앞에 놓여야 할 값/ other - 뒤에 놓여야 할 값
        if self.a > other.a:
            return True
        if self.a < other.a:
            return False
        return self.b < other.b
arr = [(1,5), (1,9), (4,2)]
arr = list(map(lambda x: Node(x[0],x[1]), arr))
heapq.heapify(arr)

heap = []
heapq.heappush(heap,Node(1,5))
heapq.heappush(heap,Node(1,9))
heapq.heappush(heap,Node(4,2))

while heap:
    temp = heapq.heappop(heap)
    print(temp.a, temp.b)