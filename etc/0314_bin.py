arr = [1,0,1,1]
arr = arr[::-1]

ans = 0
for i in range(len(arr)):
    if arr[i] == 1:
        ans += 1 << i
print(ans)