arr = [6,4,1,4,7,8,1]
heap = [0] * 20
h_idx = 1 # heap 배열의 인덱스 역할

def insert(value):
    global h_idx
    heap[h_idx] = value # 루트노드 저장
    now = h_idx
    h_idx += 1
    while True:
        p = now //2  # 부모 인덱스 구하기
        if p == 0: break  # 해당 노드가 루트노드라면 off
        if heap[p] >= heap[now]:  # 부모가 크거나 같으면 끄기 (maxheap 구현중)
            break
        heap[p], heap[now] = heap[now], heap[p]  # 부모가 더 작으면 자식이랑 swap
        now = p  # swap 당한 부모가 그 다음 프로세스의 자식이 되면서 위로 올라감

def top():
    return heap[1]

def pop():
    global h_idx
    h_idx -= 1
    heap[1] = heap[h_idx]
    heap[h_idx] = 0
    now = 1
    while True:
        son = now * 2
        r_son = son + 1
        if r_son < h_idx and heap[son] < heap[r_son]: son = r_son # 오른쪽 자식이 있는데 and 왼 < 오 앞으로 부모(now)랑 비교할 자식은 '오'
        if son >= h_idx or heap[now] > heap[son]: break  # 자식이 없거나 or 부모(now)가 자식보다 크다면 break
        heap[p],heap[son] = heap[son], heap[p]
        now = son

for i in arr:
    insert(i)

for i in range(len(arr)):
    print(top(), end=" ")
    pop()

# insert 함수로 완전이진트리로 저장
# top() 루트 노드를 리턴하는 함수
# pop() 루트 노드 출력 후 맨 뒤의 값을 맨 앞으로 올리고 자식들이랑 비교 후 swap