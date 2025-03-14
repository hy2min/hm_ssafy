name = 'ABCDE'
inf = int(21e8)

arr = [
    [0, 3, inf, 9, 5],
    [inf, 0, 7, inf, 1],
    [inf, inf, 0, 1, inf],
    [inf, inf, inf, 0, inf],
    [inf, inf, 1, inf, 0],
]

used = [0] * 5  # 경유지 체크 여부
used[0] = 1  # A(0번 인덱스)를 시작점으로 등록
result = [0, 3, inf, 9, 5]  # A ~ n번 인덱스까지 가는 최소 비용

def select_ky():
    Min = int(21e8)
    Minidx = 0
    for i in range(5):
        if used[i] == 0 and result[i] < Min:
            Min = result[i]
            Minidx = i
    return Minidx

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via = select_ky()
        used[via] = 1


    # 시작점 -> 도착지

    # 시작점 -> 경유지 -> 도착지 비교 후 작은 값으로 갱신

        for j in range(5):  # result 배열에 갱신할 것
            baro = result[j]
            ky = result[via] + arr[via][j]
            if baro > ky:
                result[j] = ky

dijkstra()
print(*result)