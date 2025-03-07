from copy import deepcopy
def delta(y,x):
    d_y = [0,0,-1,1,0]
    d_x = [-1,1,0,0,0]
    for i in range(5):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0 <= dy < 3 and 0 <= dx < 4:
            arr[dy][dx] = (arr[dy][dx] * 7) % 10

def dfs(level):
    global Max, arr
    if level == 4:
        Sum = 0
        for i in arr:
            Sum += sum(i)
        Max = max(Sum, Max)
        return

    backup = deepcopy(arr)
    for i in range(3):
        for j in range(4):
            delta(i,j)
            dfs(level+1)
            arr = deepcopy(backup)  # 원상복구

arr = [
    [3,1,9,6],
    [6,5,9,6],
    [5,8,3,7],
]

n = int(input())
Max = -21e8
dfs(0)
print(Max)