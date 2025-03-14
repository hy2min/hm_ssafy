import heapq
name = 'ABCDE'

n, m = map(int, input().split())  # 정점 개수, 간선 개수
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())  # 시작점, 도착점, 비용
    arr[a].append((b, c))

start, end = map(int, input().split())  # 시작점, 도착점 인덱스
result = [21e8] * n  # 초기세팅은 가장 큰값으로 해놓고 우선순위 큐로 체크하면서 갱신

heap = [(0,start)]
result[start] = 0  # 시작점 -> 시작점 가는 비용 0

while heap:
    ky_cost, ky = heapq.heappop(heap)  # 경유지 비용, 경유지 / 시작점에서 경유지까지의 정보(heap에서 가져온 정보)

    if result[ky] < ky_cost:  # heap에서 가져온 정보가 최신 result 데이터 값보다 크다면 pass
        continue

    for dochack, dochack_cost in arr[ky]:  # 경유지에서 도착점까지의 정보를 인접리스트에서 가져오기
        baro = result[dochack]  # 시작점 -> 도착점
        new = ky_cost + dochack_cost  # heap에서 빼고, 인접 리스트에서 빼고 / 시작점 -> 경유지 -> 도착점
        if new < baro:
            result[dochack] = new  # result 갱신
            heapq.heappush(heap, (new, dochack))  # heap에 갱신한 정보

print(*result)
print(result[end])