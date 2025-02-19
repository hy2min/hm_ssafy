#
# a = [3, 8, 5, 2, 5, 7, 2, 4]
# n = int(input())
# b = list(map(int, input().split()))
#
# cnt = 0
# for i in range(b):
#     for j in range(len(a)):
#         if b[i] == a[j]:
#             cnt += 1
#     print(f'{b[i]} : {cnt}개 있음')

# n개의 숫자를 입력 받은 후 어떤한 숫자가 몇 개 입력이 되었는지 출력
# 7
# 1 1 2 3 1 2 6


# DAT
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# bucket = [0] * (max(arr)+1)
#
# for num in arr:
#     bucket[num] += 1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0:
#         print(f'{i} : {bucket[i]}개')

# 버킷 안에 넣는 값을 헷갈리지 않도록 주의

# 어떤 알파벳이 몇개씩 사용되었는지 출력

# lst = list(input())
# # banana
# # a:3개
# # b:1개
# # n:2개
#
# bucket = [0] * (ord(max(lst))+1)
#
# for alp in lst:
#     bucket[ord(alp)] += 1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0:
#         print(f'{chr(i)} : {bucket[i]}개')
#
# # 소문자만 입력된다고 가정
# # bucket 26칸 생성 > a =0 을 하기 위해 아스키 a-a하면 됨

# # Counting Sort
# lst = [3,6,7,2,1,7,7,9,3,2]
#
#
# bucket = [0] * 10
# bucket_sum = bucket
# cnt_sort = [0] * len(lst)
#
# # DAT
# for n in lst:
#     bucket[n] += 1
#
# # 누적합
# for i in range(len(bucket)-1):
#     bucket_sum[i+1] += bucket[i]
#
# # 값넣기
# for i in lst:
#     bucket_sum[i] -= 1
#     cnt_sort[bucket_sum[i]] = i
#
# print(cnt_sort)

# # 연속되는 숫자 3개의 합이 가장 클 때의 값을 출력해주세요
# lst = [
#     [4,5,2,6,7,3,1],
#     [2,9,9,6,1,6,7],
# ]
# max_sum = 0
# for i in range(len(lst)):
#     for j in range(len(lst[0])-3):
#
#         ssum = sum(lst[i][j:j+3])
#         if ssum > max_sum:
#             max_sum = ssum
# print(max_sum)

# # 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기
# # 1 2 3 4 5
# # 2 4 2 1 3
# # 3 4 5 2 5
#
# target = [3, 4, 5]
# # arr = []
# # for _ in range(3):
# #     arr.append(list(map(int, input().split())))
# arr = [
#     [1 ,2 ,3 ,4 ,5],
#     [2 ,4 ,2 ,1 ,3],
#     [3 ,4 ,5 ,2 ,5],
# ]
# flag = 0
# for i in range(len(arr)):
#     for j in range(len(arr[0])-len(target)+1):
#         if arr[i][j:j+3] == target:
#             flag = 1
#             print(i, j)
#
# if flag == 0:
#     print("존재하지 않음")
# ***
# ***
# 이 모양으로 땅을 갖을 수 있다고 할때 2*3 배열만큼 잘라서 합을 구할떄 최대값 !!
#
# lst = [
#     [1, 5, 4, 2],
#     [1, 3, 4, 2],
#     [3, 5, 3, 2],
#     [2, 6, 4, 1],
#     ]
#
# def my_land(y,x):
#     money = 0
#     for i in range(2):
#         for j in range(3):
#
#             money += lst[i+y][j+x]
#     return money
#
# max_money = -21e8
# for i in range(3): # len(lst)-2 + 1
#     for j in range(2): # len(lst[0]-3+1
#         result = my_land(i,j)
#         if result > max_money:
#             max_money = result
#
# print(max_money)

# 델타배열(방향배열)
# arr = [
#     [3, 5, 4],
#     [1, 1, 2],
#     [1, 3, 9],
# ]
#
# y, x = map(int, input().split())
# total = 0
#
# total += arr[y][x]
# if y != 0:
#     total += arr[y-1][x]
# if y != len(arr)-1:
#     total += arr[y+1][x]
# if x != 0:
#     total += arr[y][x-1]
# if x != len(arr[0])-1:
#     total += arr[y][x+1]
#
# print(total)
#
# result = arr[y][x]
# #하 상 우 좌
# direct_y = [1, -1, 0, 0]
# direct_x = [0, 0, 1, -1]
# for i in range(4):
#     dy = y + direct_y[i]
#     dx = x + direct_x[i]
#     if dy >= 0 and dx >= 0 and dy < len(arr) and dx < len(arr[0]):
#         result += arr[dy][dx]
# print(result)
#
# arr = [
#     [3,5,4],
#     [1,1,2],
#     [1,3,9],
# ]
# y, x = map(int, input().split())
# ret = arr[y][x]
# d_y = [1, -1, 0, 0]
# d_x = [0, 0, 1, -1]
# for i in range(4):
#         dy = y + d_y[i]
#         dx = x + d_x[i]
#         if dy >= 0 and dy < len(arr) and dx >= 0 and dx < len(arr[0]):
#             ret += arr[dy][dx]
# print(ret)

# arr = [[3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
# # 대각선 4개의 값 곱하기
# y,x=map(int,input().split())
# #
# # ret = arr[y][x]
# # d_y = [-1,-1,1,1]
# # d_x = [-1,1,-1,1]
# # for i in range(4):
# #     dy = y + d_y[i]
# #     dx = x + d_x[i]
# #     if 0 <= dy < len(arr) and 0 <= dx < len(arr[0]):
# #         ret *= arr[dy][dx]
# # print(ret)
# # 위 아래 좌 우 로 3칸까지 떨어진 곳들의 합을 구하시오.
# ret = arr[y][x]
# d_y = [-3,-2,-1,1,2,3,0,0,0,0,0,0]
# d_x = [0,0,0,0,0,0,1,2,3,-1,-2,-3]
#
# for i in range(len(d_x)):
#     dy = y + d_y[i]
#     dx = x + d_x[i]
#     if 0 <= dy < len(arr) and 0 <= dx < len(arr[0]):
#         ret += arr[dy][dx]
#
# print(ret)

# 0210

# # 방향배열 연습문제
# arr=[[1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]]
#
# d_y = [1,-1,0,0]
# d_x = [0,0,1,-1]
# max_total = 0
# for y in range(4):
#     for x in range(4):
#         total = 0
#         for i in range(4):
#             dy = y + d_y[i]
#             dx = x + d_x[i]
#             if dy > 0 and dx > 0 and dy < len(arr) and dx < len(arr[0]):
#                 total += arr[dy][dx]
#         if max_total < total:
#             max_total = total
#             max_y, max_x = y, x
#
# print(max_total)
# print(max_y, max_x)
#
# # 강사님 코드
# def findMaxValue(y,x):
#     direct_y = [1,-1,0,0]
#     direct_x = [0,0,-1,1]
#     Sum = 0
#     for i in range(4):
#         dy = y + direct_y[i]
#         dx = x + direct_x[i]
#         if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue
#         Sum+= arr[dy][dx]
#     return Sum
#
# Max = int(-21e8)
# Max_j = -1
# Max_i = -1
#
# for i in range(4):
#     for j in range(4):
#         ret = findMaxValue(i,j)
#         if ret > Max:
#             Max_j = j
#             Max_i = i

# # 연습문제2
# def find_max(y,x):
#     d_y = [1,-1,0,0]
#     d_x = [0,0,1,-1]
#     total = 0
#     for i in range(4):
#         dy = y + d_y[i]
#         dx = x + d_x[i]
#         if dy <0 or dx <0 or dy > n-1 or dx > n-1:
#             return 0
#         total += arr[dy][dx]
#     total -= arr[y][x]
#     if total < 0:
#        return 0
#
#     if total % 2 == 0:
#         return total * 2
#     else:
#         return total
#
#
#
# T = int(input())
# for idx in range(T):
#     max_total = float('-inf')
#     n = int(input())
#     arr = []
#     for i in range(n):
#         arr.append(list(map(int, input().split())))
#
#     for i in range(n):
#          for j in range(n):
#              ret = find_max(i,j)
#              if ret > max_total:
#                  max_total = ret
#     print(f'#{idx+1} {max_total}')
#
#
# # binary search (이진탐색)
# lst = [2,3,4,7,8,10,11,13,15]
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# def binary_search(start, end, target):
#     while 1:
#         mid = (start + end) //2
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] > target:
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#         if start > end:
#             return 0
#
# arr.sort() # 이진 탐색을 위한 전제조건
#
# answer = binary_search(0, n-1, target)
# if ans:
#     print('TARGET')
# else:
#     print("존재하지 않음")
#
#
# # n = int(input())
# # arr = list(map(int, input().split()))
# # target = int(input())
# #
# # def binary_search(start, end, target):
# #     start = 0
# #     end = n-1
# #     while True:
# #         mid = (start + end) // 2
# #         if arr[mid] == target:
# #             return True
# #         elif arr[mid] > target:
# #             end = mid - 1
# #         elif arr[mid] < target:
# #             start = mid + 1
# #         if start > end:
# #             return 0
# # arr.sort()
# #
# # answer = binary_search(0, n-1, target)
# # print(answer)

# # parametric search
# battery="###_______"
# last = len(battery)-1
#
# def Battery(start, end):
#     now_charging = -1 # 0% 출력을 위해서
#     while True:
#         mid = (start + end) // 2
#         if battery[mid] == "#":
#             now_charging = mid
#             start = mid + 1
#         elif battery[mid] == "_":
#             end = mid -1
#         if start > end:
#             break
#     return now_charging + 1
#
# answer = Battery(0, last)
# print(answer*10)

# curser=[
#     '##########',
#     '##########',
#     '###_______',
#     '__________',
#     '__________',
#     '__________']
#
# # (2,3)
#
# curser_lst = ""
# for i in curser:
#     curser_lst += i
# print(curser_lst)
# def binary_search(start, end):
#     now_cursor = -1
#     while True:
#         mid = (start+end) // 2
#         if curser_lst[mid] == '#':
#             now_cursor = mid
#             start = mid + 1
#         elif curser_lst[mid] == '_':
#             end = mid - 1
#         if start > end:
#             break
#     return now_cursor + 1
#
# answer = binary_search(0, len(curser_lst)-1)
# y = answer // len(curser[0])
# x = answer % len(curser[0])
#
# print(y,x)


# 강사님 코드
# 행 기준으로 # 위치 일단 찾고
# 그 후, 열 기준으로 # 위치 찾기

# def abc(level):
#     print(level, end=" ")
#
#     if level == 2:
#         return
#
#     abc(level+1)
#     print(level, end=" ")
#
# abc(0)
# level ==3 일때 return 하는 함수

# # 0 1 2 출력
# def abc(level):
#     if level == 3:
#         return
#
#     print(level, end=" ")
#     abc(level+1)
#
# abc(0)
#
#
# # 0 1 2 3 출력
# # 2 1 0 출력
# def abc(level):
#     if level == 3:
#         return
#     abc(level+1)
#     print(level, end=" ")
# abc(0)
#
# # 0 1 2 3 2 1 0
# def abc(level):
#     if level == 3:
#         return
#     abc(level + 1)
#
#
# abc(0)
# # 0 1 2 2 1 0
#
# n = int(input())
# # 0 1 2 3 4 4 3 2 1 0
# # 0 1 2 2 1 0
# def abc(level):
#     if level == n:
#         return
#     print(level, end=" ")
#     abc(level + 1)
#     print(level, end=" ")
#
# abc(0)


# 0211
# 연습문제


# def abc(level):
#
#     if level ==2:
#         return
#     for i in range(2):
#         abc(level+1)
# # i, level 디버깅 통해 흐름 체크
# abc(0)

# 0212

# 누적합
# 재귀 이용해서 누적합 구하기
# 3 7 12 13 19 28

# 1
# def stack_sum(level, Sum):
#     print(Sum, end=" ")
#     if level == 5:
#         return
#
#     stack_sum(level+1, Sum+arr[level+1])
#
# stack_sum(0,arr[0])

# # 2
# Sum = arr[0]
# def abc(level):
#     global Sum
#     print(Sum, end=" ")
#     if level == 5:
#         return
#     Sum += arr[level+1]
#     abc(level+1)
#
# abc(0)


# arr = [3,4,5,1,6,9]
# Sum = arr[0]
# def abc(level):
#     global Sum
#     if level == 5:
#          return
#     Sum += arr[level+1]
#     abc(level+1)
#     Sum -= arr[level+1]
#     print(Sum, end=" ")
# abc(0)
# 점프(리턴하며 밟았던 곳 출력하기)
# arr = [2,0,1,1,3,5,1]
#
# def abc(level):
#     if level >= 7:
#         return
#
#     abc(level+arr[level])
#     print(arr[level], end= " ")
#
# abc(0)

# 3,4,7,1,6 숫자가 섞여있는 n개의 카드 묶음에서 카드를 1장씩 뽑았을떄
# 택한 숫자들의 합이 10이 나오는 경우는 몇가지 있을까요?
# 정답은 2 입력시 4
# 정답은 3 입력시 9

# n = int(input())
# arr = [3,4,7,1,6]
# cnt = 0
# def abc(level, Sum):
#     global cnt
#
#     if Sum > 10: # backtrackting 가지치기 / 기저까지 가지 않고 조건에 맞으면 되돌아오기
#         return
#     if level == n:
#         if Sum == 10:
#             cnt +=1
#         return
#     for i in range(5):
#         abc(level+1, Sum + arr[i])
#
#
# abc(0,0)
# print(cnt)

# 중복 순열


# arr = "ABC"
# path = [""] * 2
#
# def abc(level):
#     if level == 2:
#         print(*path)
#         return
#     for i in range(3):
#         path[level] = arr[i]
#         abc(level+1)
# abc(0)

# # n개의 주사위(1,2,3,4,5,6)
# n = int(input())
# path = [""] * n
#
# def abc(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(1,7):
#         path[level] = i
#         abc(level + 1)
#         # path[level] = 0 # 들어갔다 나온 값 지우기 (적는 것은 옵션 - 안지우면 덮어쓰기로 진행)
# abc(0)
#


# # 순열
# n = int(input())
# arr = "ABCD"
# path = [0]* n
# used = [0]*len(arr)
#
# def abc(level):
#     if level == n:
#         print((*arr))
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         if used[i] ==0:
#
#             used[i] =1
#             abc(level+1)
#             used[i] = 0
# abc(0)
#
# # 조합
# card = 'abcd'
# path = [0] * 3
#
# def abc(level,start):
#     if level ==3:
#         print(*path)
#         return
#
#     for i in range(start, 4):
#         path[level] = card[i]
#         abc(level+1, i+1)
#         path[level] = 0
#
#
# abc(0,0)
#
# # i = 0 이면 a로 들어감. 그 아래 레벨은 i = 1 부터 즉, i + 1
#
# # 중복 조합
# card = 'abcd'
# path = [0] * 3
#
# def abc(level,start):
#     if level ==3:
#         print(*path)
#         return
#
#     for i in range(start, 4):
#         path[level] = card[i]
#         abc(level+1, i) # 여기가 차이점점
#         path[level] =0
#
#
# abc(0,0)
#
# # i 다음 레벨은 i부터

# 주사위 abcd 중복 순열
# n개의 주사위

# arr = 'abcd'
# n = int(input())
# path = [0] * n
#
#
#
# # 1. 3개의 주사위 던졌을 때, 나오는 경우를 출력
# # 조건: B는 나오지 않도록 하시오
# #     1. 진입을 하지 않도록
#
#
# def abc(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         if i == 1: continue # 진입을 하지 않도록
#         abc(level+1)
#         path[level] = 0
# abc(0)
#
# #     2. 진입 후 return
#
# arr = 'abcd'
# n = int(input())
# path = [0] * n
#
# def abc(level):
#     if level > 0 and path[level-1] == 'B': return
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] = 0
# abc(0)
#
# # 조건: 연속해서 같은 카드가 2번 나오면 안됨
#
# def abc(level):
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         if level > 0 and path[level-1] == arr[i] : continue
#         abc(level+1)
#         path[level] = 0
# abc(0)
#
# def abc(level):
#     if level > 1 and  path[level-2] == path[level-1]: continue
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] = 0
# abc(0)
#
# # 조건: 첫번째 주사위에서 C가 나오면 안됨
# def abc(level):
#
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         if level == 0 and i == 2: continue
#         abc(level+1)
#         path[level] = 0
# abc(0)
#
# def abc(level):
#     if level==1 and path[level-1] =='c': return
#     if level == n:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#
#         abc(level+1)
#         path[level] = 0
# abc(0)
#


# DFS

# # 인접행렬
# name = ['Amy', 'Bob', 'Charles', 'Diane', 'Edger']
# arr = [
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0],
# ]
#
# people = [0] *5
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 1:
#             people[j] += 1
#
# print(name[people.index(max(people))])
#
# # 인접행렬로 표시
# # 문자열의 형제 출력
# ch = input()
# idx = ord(ch) -65
# parent = -1
# bro = =1
#
# arr = [
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
#
# # 1. 부모노드 찾기
# for i in range(6):
#     if arr[i][idx] == 1:
#         parent = i
#         break
# if parent == -1:
#     print('형제없음')
# else:
#     for i in range(6):
#         if arr[parent][i] == 1 and i!= idx:
#             bro = i
#             break
#     if bro == -1:
#         print('형제없음')
#     else:
#         print(chr(bro+65))
#
# # j //2 가 같은 경우가 1이면 형제가 있어 그걸 코드로 구현해봐
#
# stack queue
# CS
# 1. 자료구조(data structure)
#     data를 어떻게 저장, 처리(관리)하는지
#         1. 선형 for while
#         2. 비선형 DFS BFS
# 2. 알고리즘
#     효율적인 해 찾기
#
# queue - FIFO
# stack - LIFO
#
# # stack
# st = list()
# st = []
# st.append(2)
# st.append(3)
# st.append(4)
# st.append(5)
# test = st.pop()
#
# # queue
# q = list()
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)
# q.append(7)
# q.pop(0)
#
# from collections import deque
# q = deque()
# q.append(5)
# q.append(15)
# q.append(25)
# q.append(35)
# q.append(45)
#
# print(q)
# print(list(q))
#
# q.popleft()
# q.popleft()
#
# print(list(q))
#
# # 이건 그냥 알고 넘어가도 됨.
# import queue
# q = queue.Queue()
# q.put(5)
# q.put(15)
# q.put(25)
# q.get()
# print(q)
# print(q.queue)
# print(list(q.queue))


arr = [
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0],
]
cnt = 0
visited = [0] *4
def dfs(now):
    global cnt
    if now == 3:
        cnt += 1

    for i in range(4):
        if not visited[i] and arr[now][i]:
            visited[i] = 1
            dfs(i)
            visited[i] = 0
dfs(0)
print(cnt)

arr = [
    [0,1,8,0],
    [0,0,1,7],
    [0,1,0,1],
    [0,0,0,0],
]

Sum = 0
Min_sum = 21e8
visited = [0] * 4

def dfs(now,Sum):
    global Min_sum
    if now == 3:
        if Min_sum > Sum:
            Min_sum = Sum
    for i in range(4):
        if not visited[i] and arr[now][i] != 0:
            visited[i] = 1
            dfs(i, Sum + arr[now][i])
            visited[i] = 0

dfs(0,0)

print(Min_sum)

arr = [
    [0,0,0,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,0,0],
    [1,0,0,0,0],
]

visited = [[0] * 5 for _ in range(5)]
d_y = [-1,1,0,0]
d_x = [0,0,-1,1]
Min_cnt = 21e8

def dfs(y,x,Cnt):
    global Min_cnt
    if y == 4 and x == 2:
        if Min_cnt > Cnt:
            Min_cnt = Cnt
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 5 or dx >= 5:
            continue
        if not visited[dy][dx] and arr[dy][dx] == 0:
            visited[dy][dx] = 1
            dfs(dy,dx,Cnt + 1)
            visited[dy][dx] = 0

dfs(0,0,0)
print(Min_cnt)