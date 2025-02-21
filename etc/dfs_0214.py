
# # 인접 리스트를 이용한 최소 경로
#
# n, m = map(int, input().split())
# lst = [[] for _ in range(n)]  # 정점 개수만큼 리스트 추가
#
# for i in range(m):  # 간선 정보 개수만큼 정보를 입력
#     start, end, cnt = map(int, input().split())
#     lst[start].append((end, cnt))
#     lst[end].append((start, cnt))  # 무방향 그래프이기 떄문에 start end 두번 추가
#
# used = [0] * n  # 무방향이기 때문에 이미 진행한 방향은 제거하기 위해
# Min = 21e8
# used[0] = 1  # A로 시작
#
#
# def dfs(now, Sum):
#     global Min
#
#     for i in lst[now]:
#         if used[i[0]] == 1:
#             continue
#
#         used[i[0]] = 1
#         dfs(i[0], Sum + i[1])
#         used[i[0]] = 0
#
#
# # 위에서 부터 한칸 씩 내려오면서
# # 숫자 한개씩을 선택합니다,
# # 선택한 숫자들을 모두 더했을 때
# # 합이 20 이상인 경우가 몇가지 인지 출력해 주세요
#
# arr=[[4,5,2],
#      [-2,1,6],
#      [3,9,-4],
#      [3,5,2]]
#
# # level = 4 / branch = 3
#
# cnt = 0
# def dfs(level, Sum):
#     global cnt
#     if level == 4:
#         if Sum >=20:
#             cnt += 1
#         return
#
#     if Sum >= 20:
#         cnt += 1
#         return cnt
#
#     for i in range(3):
#         dfs(level + 1, Sum + arr[level][i])
#
# dfs(0,0) # level Sum
# print(cnt)

# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다.
# 계단을 밑으로 내려오면서 이동할 수 있는 범위는
# 7시방향 6시방향 5시방향 입니다.
# 선택한 숫자들을 모두 더했을 때
# 합이 30 이상인 경우가 몇가지 인지 출력해 주세요

arr=[[3,5,9,6],
     [7,-8,1,6],
     [-10,2,3,9],
     [5,1,2,8],
     [4,7,1,8]]

# cnt = 0
#
# def dfs(level, Sum):
#     global cnt
#     if i <
#     if level == 5:
#         if Sum >= 30:
#             cnt += 1
#
#         return
#
#     for i in range(3):
#         dfs(level +1, Sum+ arr[level][i])
#
#
# dfs(0, 0) # level Sum
# print(cnt) # 수정 필요
#

# cnt = 0
# path = [0] * 5
# # 모든 경우를 다 탐색해봐야 하는 상황 > 위치에 따라 조건이 달라지기 때문에 : 완전탐색(Brute-Force)
# def dfs(now, level, Sum):
#     global cnt
#     if level == 4:
#         if Sum >= 30:
#             for i in range(5):
#                 print(path[i], end=" ")
#             print()
#             cnt += 1
#             return
#
#     for i in range(3):
#         direct = [-1, 0, 1]
#         dy = level + 1
#         dx = now + direct[i]
#         if dx < 0 or dx > 3: continue
#         path[level+1] = arr[dy][dx]
#         dfs(dx, level+1, Sum + arr[dy][dx])
#
# for i in range(4): # index 값에 따라서 들어갈 수 있는 i 값이 다르기 때문에 for 문을 돌려야 함.
#     path[0] = arr[0][i]
#     dfs(i, 0, arr[0][i])
#
# print(cnt)
#
# # 벽을 피해서 끝까지 가는 경로가 있는지 확인
# arr = [
#     [0,0,0,0],
#     [1,0,1,0],
#     [1,0,1,0],
#     [0,0,0,0],
# ]
# d_y = [1,-1,0,0]
# d_x = [0,0,-1,1]
# flag = 0
#
# visited = [[0] * 4 for _ in range(4)]
# flag = 0
#
# def dfs(y, x):
#     global flag
#     if y == 3 and x == 3:
#         flag = 1
#         return
#
#     for i in range(4):
#         dy = y+d_y[i]
#         dx = x+d_x[i]
#         if dy < 0 or dx < 0 or dy > 3 or dx > 3:
#             continue
#         if arr[dy][dx] == 1:
#             continue
#         if visited[dy][dx] == 1:
#             continue
#         visited[dy][dx] = 1
#
#         dfs(dy,dx)
#         if flag:
#             return
# visited[0][0] = 1
# dfs(0,0)
# if flag:
#     print('도착가능')
# else:
#     print('탈출불가')

# start~end까지 이동하는 최소 칸수
arr = [
    [0,0,0,0,0,0],
    [1,0,1,0,1,0],
    [1,0,1,0,1,0],
    [1,0,1,0,1,0],
    [0,0,0,0,0,0],
]
start = (0,0)
end = (2,3)

flag = 0
d_y = [1,-1,0,0]
d_x = [0,0,-1,1]

visited = [[0] * 6 for _ in range(5)]
Min = 21e8

def dfs(y,x, level):
    global Min
    if level > Min:
        return

    if y == 2 and x == 3:
        if Min > level:
            Min = level
            return
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]

        if dy < 0 or dx < 0 or dy > 4 or dx > 5: # 배열 범위 체크를 제일 먼저 해야 함!!!!
            continue
        if visited[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dfs(dy, dx, level +1)
        visited[dy][dx] = 0



visited[0][0] = 1
dfs(0, 0, 0)

print(Min)

arr = [
    [4,8,1],
    [9,2,6],
    [3,5,7],
    ]

d_y = [1,-1,0,0]
d_x = [0,0,-1,1]
Max = -21e8

def dfs(y, x, level):
    global Max
    if level == 3:
        Sum = 0
        for i in arr:
            Sum += sum(i)
        if Max < Sum:
            Max = Sum
            return

    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]

        if dy < 0 or dx < 0 or dy > 2 or dx > 2:
            continue
        for j in range(4):
            arr[dy][dx] = (arr[dy][dx] * 7) % 10
            if dy + d_y[j] < 0 or dx + d_x[j] < 0 or dy + d_y[j] > 2 or dx + d_x[j] > 2:
                arr[dy + d_y[j]][dx + d_x[j]]  = (arr[dy + d_y[j]][dx + d_x[j]] * 7) % 10
            dfs(dy, dx, level + 1)

dfs(0,0,0)
print(Max)