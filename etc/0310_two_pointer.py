n, m = map(int, input().split()) # arr 크기, 원하는 구간의 합
arr = list(map(int, input().split()))
cnt, Sum = 0, 0
right, left = 0, 0


while left < n:
    if Sum == m:
        cnt += 1

    if Sum >= m or right == n:
        Sum -= arr[left]
        left += 1

    elif Sum < m:
        Sum += arr[right]
        right += 1

print(cnt)