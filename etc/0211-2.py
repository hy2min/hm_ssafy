
lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

d_y = [0, 0, -1, 1]
d_x = [-1, 1, 0, 0]

for y in range(7):
    for x in range(7):

        # A 일때
        if lst[y][x] == 'A':

            # 물풍선
            for i in range(4):
                for power in range(1, 6):  # A 물풍선 > 5칸
                    dy = y + d_y[i]*power
                    dx = x + d_x[i]*power
                    if dy < 0 or dx < 0 or dy >= 7 or dx >= 7:
                        continue
                    if lst[dy][dx] == '#' or lst[dy][dx] == 'A' or lst[dy][dx] == 'B':
                        break
                    else:
                        lst[dy][dx] = 0

        # B 일떄
        if lst[y][x] == 'B':

            # 물풍선
            for i in range(4):
                for power in range(1, 4):  # B 물풍선 > 3칸
                    dy = y + d_y[i] * power
                    dx = x + d_x[i] * power
                    if dy < 0 or dx < 0 or dy >= 7 or dx >= 7:
                        continue
                    if lst[dy][dx] == '#' or lst[dy][dx] == 'A' or lst[dy][dx] == 'B':
                        break
                    else:
                        lst[dy][dx] = 0

cnt = 0
for i in lst:
    for j in i:
        if j == '_':
            cnt += 1
print(cnt)



