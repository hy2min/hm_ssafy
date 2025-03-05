from collections import deque
def bfs(ai,aj,y,x,level): # 소화전, 사람
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((y,x,level))
    visited[y][x] = 1

    while q:
        y, x, level = q.popleft()

        if (y,x) == (ai,aj):
            return level

        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if 0 <= dy < n and 0 <= dx < n:
                if arr[dy][dx] != '#' and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx, level+1))



n = int(input())
arr = [list(input()) for _ in range(n)]
y, x = map(int,input().split())

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]

lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'A':
            lst.append((i,j))

        if arr[i][j] == '$':
            fi,fj = i,j

mn = 21e8
for ai,aj in lst:
    ans = bfs(ai,aj,y,x,0) + bfs(ai,aj,fi,fj,0)
    mn = min(ans,mn)
print(mn)