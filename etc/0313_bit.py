arr = ['A','B','C','D','E']
answer = 0
# 1인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for _ in range(len(arr)):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

for target in range(1 << len(arr)):
    if get_count(target) >= 2:
        answer += 1
print(answer)

