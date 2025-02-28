def check_stone(i,j):
    for x in range(1,j+1):
        if i-x <0 or i+x >= N:
            break
        if stone[i-x] == stone[i+x]:
            stone[i-x] = 1- stone[i-x]
            stone[i+x] = 1- stone[i+x]
    return stone

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1 # new index
        check_stone(i,j)

    print(f'#{tc} {" ".join(map(str,stone))}')