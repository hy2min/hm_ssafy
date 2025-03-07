def dfs(level, Sum):
    global Min
    if level == 12:
        if abs(Sum) < abs(Min):
            Min = Sum
        return

    if level % 2 == 0:
        for i in range(6):
            if used1[i] == 0:
                used1[i] = 1
                dfs(level+1, Sum+(line1[i]*(level+1)))
                used1[i] = 0
    else:
        for i in range(6):
            if used2[i] == 0:
                used2[i] = 1
                dfs(level+1, Sum+(line2[i]*(level+1)))
                used2[i] = 0
used1 = [0] * 6
used2 = [0] * 6
Min = 21e8

line1=[5,2,7,-5,-7,9]
line2=[4,-5,-7,9,-5,3]

dfs(0,0)

print(Min)