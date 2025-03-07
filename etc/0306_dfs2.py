# 동전 거스름돈 최소 갯수
def dfs(n, cnt):
    global min_cnt
    if n < 0 or cnt > min_cnt:
        return
    if n == 0:
       min_cnt = min(cnt, min_cnt)
       return
    for i in coin:
        dfs(n-i, cnt + 1)



n = int(input())  # 거슬러 받은 돈
coin = [110,70,10]
min_cnt = 21e8
dfs(n, 0)
print(min_cnt)




# while n > 0:
# cnt = 0
#     if n % 10 !=0:
#         print('거스름돈 불가')
#         break
#     for i in [110, 70, 10]:
#         cnt += n //i
#         n = n % i#
#
# print(cnt)

