arr = [0] * 20 # 트리의 형태로 저장할 1차원 배열 만들기
lst = [4,2,9,7,15,1]

def insert(value):
    now = 1 # 내가 저장할 index
    while True:
        if arr[now] == 0:
            arr[now] = value
            return
        if arr[now] < value:
            now = now * 2 +1
        else:
            now = now * 2


# 입력된 값(lst) 트리 형태로 저장
# insert() 함수 만들기

def search(target):
    now = 1
    while True:
        if now >= 20:
            return False
        if arr[now] == target:
            return True
        if arr[now] < target:
            now = now*2 + 1
        else:
            now = now*2

for i in lst:
    insert(i)
