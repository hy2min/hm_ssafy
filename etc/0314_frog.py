arr = [0,7,-3,-5,-4,-2,6,5,-9,1,0]

dp = [[0,0,0] for _ in range(len(arr))]
dp[0] = [0,0,0]
dp[1] = [0,arr[1],0]

for n in range(2,11):
    dp[n][0] = max(dp[n-1]) + arr[n]
    dp[n][1] = max(dp[n-2]) + arr[n]
    if n % 2 == 0:
        dp[n][2] = max(dp[n//2]) + arr[n]

print(*dp)

print(max(dp[10]))