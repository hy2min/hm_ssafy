from collections import deque
# 좌표 입력 하루 지날 때부터 상하좌우로 꽃이 핌
# (0,0) 좌표는 몇일 째 피는지

n = int(input())
y, x = map(int,input().split())
arr = [[0] * n for _ in range(n)]

arr[y][x] = 1
q = deque()
q.append((y,x,1))

ans = -1

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]

while q:
    y, x, level = q.popleft()
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0<=dy < n and 0<= dx < n:
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                q.append((dy,dx,level + 1))
                if dy == 0 and dx == 0:
                    ans = level + 1
                    break
    if ans != -1:
        break

print(ans)