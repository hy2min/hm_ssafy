# # 10진수 > n진수
# a = 13
# b = bin(a)
# c = oct(a)
# d = hex(a)

# print(b,c,d)
# print(type(c))

# # n진수 > 10진수
# print(int(b,2))
# print(int(c,8))
# print(int(d,16))



# # 10진수를 3진수로 바꾸는 코드 작성해보기
# n = int(input())
# tri = ''
#
# while n != 0:
#     tri = str(n%3) + tri
#     n //= 3
#
# print(tri)
# # -----------
# a= 13
#
# def trans(value):
#     ans = ''
#     while value >= 1:
#         value, rest = divmod(value,3)
#         ans += str(rest)
#     ans = ans[::-1]
#
# result = trans(a)
# print(result)

# print(int(result,3))
#
# print(13&9) # anpersand 둘다 1이면 참
# print(13|9) # bar 둘 중 하나만 1 이면 참
# print(13^9) # caret exclusive xor
#                 # 같으면 0 다르면 1
# # 10<<n -> 10*(2**n)
# # 10>>n -> 10 /(2**n)
# print(10 >> 2)
# 101
# 5&(1<<1)  # 결과값 0  5의 1번째 비트 값은 0
# 5&(1<<2)  # 결과값 4  5의 2번째 비트 값은 1
# 5&(1<<3)  # 결과값 0  5의 3번째 비트 값은 0
## 위 결과가 0이 아니면 값의 n번째 비트의 값은 1이다.
#
# arr = [1,2,3]
# n = 3
# for i in range(1 << 3):  # 1000 = 8
#     answer = []
#     for idx in range(3):  # arr 원소 개수
#         if i & (1 << idx) != 0:
#             answer.append(arr[idx])
#     if answer:
#         print(answer)
#
# answer = 0
# a, b = map(int, input().split())
# for i in range(2, min(a,b)):
#     if a % i == 0 and b % i == 0:
#         answer = i
# print(answer)

# answer = 0
# a,b = map(int, input().split())
# while b:
# 	answer = a % b
# 	a = b
# 	b = answer
# print(a)

# # GCD
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b  # b가 a 자리로 내려가고, a/b 나머지값이 b 자리로 내려가는 과정 ~ 나머지 값이 0이 될때까지
#     return a
#
# # LCM
# def lcm(a, b):
#     return (a * b) / gcd(a,b)

# # # prime number n보다 작은 모든 소수 출력
# n = int(input())
# ans = []  # 2~n까지의 소수 갯수
# for i in range(2, n+1):  # 2~n까지 확인
#     flag = 0
#     for j in range(2, i):  # 2~i보다 작은 수로 나눠지는지 확인할 수
#         if i % j == 0:  # 나눠진다면 소수 x
#             flag = 1
#             break
#     if flag == 0:  # break 걸리지 않는다면 소수
#         ans.append(i)
# print(ans)
#
# # 에라토스테네스의 체 -> 소수 찾는 알고리즘
#
# n = int(input())
# check = [0] * (n + 1)
# end = int(n ** 0.5)
#
# for i in range(2, end + 1):  # 1. 2부터 입력받은 수까지 확인
#     if check[i] == 1:  # 4. 이미 체크가 된 값이라면 pass
#         continue
#     for j in range(i+1,n+1,i):  # 2. 작은수부터 배수에 해당하는 인덱스에
#         check[j] = 1  # 3. 1 체크하기
# for i in range(2, n+1):
#     if check[i] == 0:
#         print(i, end=" ")

# sliding window
n,m = map(int, input().split())
arr = list(map(int, input().split()))
Max = Sum = sum(arr[:m])
for i in range(n-m):
    Sum += arr[m+i]
    Sum -= arr[i]
    Max = max(Max, Sum)
print(Max)