# n개의 항, 각 항 안에 1~4 숫자 존재
# 각 항에서 숫자 1개씩 뽑아서 더할 때
# 10이 나오는 경우가 몇가지

def dfs(level,Sum):
    global cnt
    if level == n:
        if Sum ==10:
            cnt +=1
        return
    for i in range(1,5):
        dfs(level+1, Sum + i)

n = int(input())
cnt = 0
dfs(0,0) # lv,sum
print(cnt)