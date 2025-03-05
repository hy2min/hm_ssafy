#치즈먹고 여자친구

from collections import deque

def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj,0))
    visited = [[0] * 6 for _ in range(4)]
    visited[si][sj] = 1


    while q:
        y,x,level = q.popleft()
        if (y, x) == (ei, ej):
            return level
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < 4 and 0 <= dx < 6:
                if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                   visited[dy][dx] = 1
                   q.append((dy,dx,level+1))

arr=[[0,0,0,0,0,0],
     [1,1,0,0,1,0],
     [1,0,0,0,1,0],
     [0,0,0,0,0,0]]
directy=[0,0,-1,1]
directx=[1,-1,0,0]

by = (0,0)
gr = (3,5)
ch = (3,0)


ans = bfs(0,0,3,0) + bfs(3,0,3,5)
print(ans)