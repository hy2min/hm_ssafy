from collections import deque

def bfs(y,x):
    q= deque()
    q.append((y,x))
    size = 1
    arr[y][x] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < 5 and 0 <= dx < 5:
                if arr[dy][dx] == 1:
                    q.append((dy,dx))
                    size += 1
                    arr[dy][dx] = 0
    return size
arr = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
]
directy=[0,0,-1,1]
directx=[1,-1,0,0]

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
           ans = bfs(i,j)
print(ans)