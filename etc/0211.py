def stone_chk(i,j):
    flag = 1
    for x in range(1, j + 1):
        if i - x < 1 or i + x > N :
            flag = 0
            break
        if state[i-1-x] == state[i-1+x] == 0:
            state[i-1-x] = state[i-1+x] = 1
        elif state[i-1-x] == state[i-1+x] == 1:
            state[i-1-x] = state[i-1+x] = 0


T = int(input()) # 게임의 개수
for idx in range(T):
    N, M = map(int, input().split()) # 돌 개수, 뒤집기 횟수

    state = list(map(int, input().split())) # 돌 상태
    for _ in range(M):
        i, j = map(int, input().split())
        stone_chk(i,j)

    print(f'#{idx+1} {" ".join(map(str,state))}')

