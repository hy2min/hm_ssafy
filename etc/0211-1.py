T = int(input()) # 게임 갯수
for idx in range(T):
    N, M = map(int,input().split()) # 돌의 수, 뒤집기 횟수
    state = list(map(int, input().split())) # 돌의 초기상태

    for _ in range(M): # 뒤집기 M번 반복
        i, j = map(int,input().split()) # 돌 위치, 마주보는 돌의 쌍 갯수
        i -= 1 # 기준 인덱스 설정

        for x in range(1, j+1): # j개의 돌 색 체크
            if i-x < 0 or i+x > N-1:
                break
            if state[i-x] == state[i+x] == 0:
                state[i-x] = state[i+x] = 1
            elif state[i - x] == state[i + x] == 1:
                state[i - x] = state[i + x] = 0

    print(f'#{idx+1} {" ".join(map(str,state))}')
