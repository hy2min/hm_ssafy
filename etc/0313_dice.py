def dfs(level, start):
    if level == n:
        print(*path)
        return
    for i in range(start,7):
        path.append(i)
        dfs(level+1, i)
        path.pop()
n = int(input())
path = []
dfs(0, 1)