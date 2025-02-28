T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            cnt += 1
            for j in range(i,n):
                arr1[j] = 1-arr1[j]
    print(f'#{tc} {cnt}')