t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = -21e8
    for i in range(n):
        cnt = 0
        point = arr[i]
        for j in range(i+1,n):
            if point < arr[j]:
                point = arr[j]
                cnt += 1
        mx = max(cnt, mx)
    print(f'#{tc} {mx}')