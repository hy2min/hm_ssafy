def dfs(level, Sum):
    global Min
    flag = 0
    if abs(sum(power) - (2 * Sum)) > abs(Min):
        return

    for i in range(7):
        if visited[i] == 0:
            visited[i] = 1

            dfs(level + 1, Sum + power[i])
            visited[i] = 0
            flag = 1
    if flag:
        if abs(sum(power) - (2*Sum)) < Min:
            Min = abs(sum(power) - (2*Sum))
        return
power=[50,40,99,5,25,6,37]
visited = [0] * 7
Min = 21e8
dfs(0,0)
print(Min)
