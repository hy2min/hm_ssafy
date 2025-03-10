arr = [0] * 200

def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret
def union(a,b):
    global arr
    bossa, bossb = findboss(a), findboss(b)

    if bossa == bossb:
        return
    arr[ord(bossb)] = bossa




union('A', 'B')
union('D', 'E')
union('B', 'E')
union('B', 'D')
union('E', 'F')

y, x = input().split()
if findboss(y)==findboss(x):
    print('같은그룹')
else: print('다른그룹')