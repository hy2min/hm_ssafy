arr = [
    [0,5,3,6,8],
    [1,4,2,9,1],
    [6,9,1,7,7],
    [8,5,4,1,0],
]

dp = [[0] * 5 for _ in range(4)]
dp[0][0] = arr[0][0]

for i in range(4):
    for j in range(5):
        if i == 0 and j == 0:
            continue

        up = dp[i-1][j]
        right = dp[i][j-1]

        if i == 0:
            up = 21e8
        if j == 0:
            right = 21e8

        dp[i][j] = min(up,right) + arr[i][j]

print(dp[3][4])
#
# for i in di:
#     dy = y + i[0]
#     dx = x + i[1]
#     if dy >= 5 or dx >= 5:
#         continue
#
#     dp[dy][dx] += arr[dy][dx] + dp[y][x]
#     y,x = dy,dx
#