# arr = ["m", "i", "n"]
# n = int(input())
# print(arr[n])

# def KFC():
#     print("KFC입니다")

# def MC():
#     print("MC입니다")

# n = int(input())
# if n == 1:
#     KFC()
# elif n == 2:
#     MC()

# def LOT():
#     for i in range(1, 6):
#         print(i, end="")

# n = int(input())
# for i in range(n):
#     LOT()
#     print("")

# def KFC():
#     print("#" * 10)

# def MC():
#     print("@" * 10)

# KFC()
# MC()

# arr = [0] * 6
# arr[0], arr[1], arr[2] = map(int, input().split())
# arr[3] = int(input())
# arr[4] = arr[3] + 1
# arr[5] = arr[4] + 1

# for i in arr:
#     print(i, end=" ")
# # 좀 더 깔끔하게 코드 수정 필요

# def KFC():
#     global n
#     n = int(input())

# def BBQ():
#     global n
#     if n >= 5:
#         print("만세")
#     else:
#         print("다시")

# KFC()
# BBQ()

# arr = ["A", "B", "C"]

# def KFC():
#     for i in arr:
#         print(i, end="")


# n = int(input())
# for i in range(n):
#     KFC()
#     print("")

# def input1(): # input은 파이썬 내장 함수이기 때문에 함수명을 변경해야 함.
#     global arr
#     arr = list(map(int, input().split()))

# def output():
#     for i in arr[::-1]:
#         print(i, end="")

# input1()
# output()


# n = int(input())
# arr = [0] * 6
# for i in range(6):
#     arr[i] = n + i

# def PrintAll():
#     for i in arr:
#         print(i)

# PrintAll()

# def QTR():
#     print("QTR100%")
# def BBQ():
#     print("BBQ100%")

# arr = [0] * 3
# arr = list(map(int, input().split()))
# total = 0
# for i in arr:
#     total += i

# if total >= 10:
#     QTR()
# else:
#     BBQ()    

# arr = [3, 4, 1, 5, 8, 1, 7, 7, 3, 6, 9]
# n = int(input())
# for i in range(0, len(arr), n):
#     print(arr[i], end=" ")

# def mincoding():
#     a, b = map(int, input().split())
#     print(f"({a})({b})")

# mincoding()

# def KFC():
#     print("KFC")
# def BBQ():
#     print("BBQ")

# s = input()
# if s == "B":
#     KFC()
#     BBQ()
# elif s == "b":
#     BBQ()
# elif s == "7":
#     KFC()

# char = input()

# for i in range(65, ord(char)+1):
#     print(chr(i), end="")

# ch1, ch2 = map(str, input().split())
# for i in range(4):
#     for j in range(ord(ch1), ord(ch2)+1):
#         print(chr(j), end= " ")
#     print("")

# def input1():
#     global a, b, c
#     a, b, c = map(str, input().split())

# def process():
#     global flag
#     if a == "A" and b == "B" and c == "C":
#         flag = 1
#     else: 
#         flag = 0

# def output():
#     if flag == 1:
#         print("ABC를찾았다")
#     else:
#         print("못찾았다")

# input1()
# process()
# output()

# a, b, c = map(int, input().split())
# for i in range(c):
#     for j in range(a, b+1):
#         print(j, end=" ")
#     print("")

# arr = list(map(str, input().split()))
# for i in arr:
#     print(f"문자\'{i}\'의 아스키코드값은 {ord(i)}")

# str = input()
# for i in range(ord(str), 96, -1):
#     print(chr(i), end="")


# arr1 = arr2 = list(map(int, input().split()))
# for i in arr1:
#     print(i, end=" ")
# print("")
# for i in arr2:
#     print(i, end=" ")

# string = input()
# if string.islower() == True:
#     print("소문자입력!!")
# elif string.isupper() == True:
#     print("대문자입력!!")
# elif string.isdigit() :
#     print("숫자문자입력!!")

# arr = list(map(int, input().split()))
# total = 0
# for i in arr:
#     total += i
# for i in range(total):
#     for j in arr:
#         print(j, end=" ")
#     print("")

# arr = list(map(str, input().split()))
# count = 0
# for i in arr:
#     if i.isdigit():
#         count += 1
# if count == 0 :
#     print("숫자미발견")
# else:        
#     print(f"숫자{count}개발견")

# arr1 = list(map(str, input().split()))
# arr2 = []
# for i in arr1:
#     if i.islower():
#         arr2.append(i.upper())
#     elif i.isupper():
#         arr2.append(i.lower())

# for i in arr2:
#     print(i, end=" ")


# arr1 = [0] * 5
# arr2 = [0] * 5

# string = input()
# for i in range(5):
#     arr1[i] = chr(ord(string) + i) 
# for i in range(5):
#     arr2[i] = chr(ord(string) - i) 

# for i in arr1:
#     print(i, end="")
# print("")
# for i in arr2:
#     print(i, end="")

# arr = [5, 4, 1, 2, 7, 8]
# n = int(input())
# for i in range(n):
#     for j in arr[::-1]:
#         print(j, end=" ")
#     print("")

# arr = list(map(str, input().split()))
# if arr[0] == sorted(arr,reverse=True)[0]:
#     print(f"옳다{arr[0]}")
# else:
#     print("옳지않음")

# str1, str2 = map(str, input().split())
# print(ord(str2)-ord(str1))

# arr1 = [3, 5, 2, 4, 1]
# arr2 = [[9, 8], [7, 1], [3, 4]]
# n = int(input())

# if n % 2 == 1:
#     for i in arr1:
#         print(i, end="")
# else:
#     for i in arr2:
#         for j in i:
#             print(j, end="")
#         print("")

# a, b = map(int, input().split())
# if abs(a-b) % 2 == 1:
#     print("고백한다")
# else:
#     print("짝사랑만")

# arr = [[3, 1, 1], [2, 3, 2]]
# for i in arr:
#     for j in i :
#         print(j, end="")

# arr = []
# inputs = input()
# answer = 0
# for i in inputs.split():
#     arr.append(int(i))
# for i in arr:
#     if 3 <= i <= 7:
#         answer += 1

# print(answer)

# score = int(input())
# if score >= 80:
#     print("수")
# elif score >= 70:
#     print("우")
# elif score >= 60:
#     print("미")
# else:
#     print("재시도")

# arr = list(map(int, input().split()))
# for i in arr:
#     if i < 20:
#         print("더 큰수를 입력하세요")
#     elif i >20:
#         print("더 작은수를 입력하세요")
#     else:
#         print("정답입니다")

# arr = list(map(int, input().split()))
# maximum = 0

# for i in arr:
#     if i >= maximum:
#         maximum = i

# minimum = maximum
# for i in arr:
#     if i <= minimum:
#         minimum = i

# print(f"MAX={maximum}")
# print(f"MIN={minimum}")

# arr = [[3, 4, 1], [2, 1, 4], [3, 3, 0]]
# odd = 0
# even = 0
# for i in arr:
#     for j in i:
#         if j % 2 == 0 :
#             even += 1
#         else:
#             odd += 1
# print(f"짝수 : {even}\n홀수 : {odd}")

# scores = list(map(int, input().split()))

# for i in range(len(scores)):
#     if scores[i] >= 70:
#         print(f"{i + 1}번사람은{scores[i]}점PASS")
#     elif scores[i] >= 50:
#         print(f"{i + 1}번사람은{scores[i]}점RETEST")
#     else:
#         print(f"{i + 1}번사람은{scores[i]}점FAIL")

# char = input()
# array = []
# def input1():
#     for _ in range(4):
#         row = []
#         for _ in range(4):
#             row.append(char)
#         array.append(row)

# def output():
#     for row in array:
#         print("".join(row))

# input1()
# output()

# def input1():
#     global n
#     n = int(input())

# def process():
#     global n
#     global array
#     array = []
#     for _ in range(3):
#         row = []
#         for _ in range(3):
#             row.append(n)
#             n += 1
#         array.append(row)

# def output():
#     for i in array:
#         for j in i:
#             print(j, end=" ")
#         print("")
# input1()
# process()
# output()

# n = int(input())

# def BBQ():
#     if 0 < n < 5:
#         print("초기값")
#     elif 6 < n < 10:
#         print("중간값")
#     else:
#         print("알수없는값")

# if n == 3 or n == 5 or n == 7:
#     for i in range(1, 11):
#         print(i, end="")
# elif n == 0 or n == 8:
#     for i in range(10, 0, -1):
#         print(i, end="")
# else:
#     BBQ()

# n = int(input())
# for i in range(3):
#     for j in range(5):
#         print(n, end="")
#     print("")
# for i in range(3):
#     for j in range(3):
#         print(n, end="")
#     print("")

# arr = [0] * 6
# index = list(map(int, input().split()))
# for i in index:
#     arr[i] = 1
# for i in arr:    
#     print(i, end=" ")

# def input1():
#     global str1, str2
#     str1, str2 = map(str, input().split())

# def output():
#     if str1.isupper() and str2.isupper():
#         print("대문자들")
#     elif str1.isupper() or str2.isupper():
#         print("대소문자")
#     else:
#         for i in range(97, 123):
#             print(chr(i), end="")   

# input1() 
# output()

# s = input()
# chg_s = ord(s)
# array = []
# for _ in range(3):
#     row = []
#     for _ in range(5):
#         row.append(chr(chg_s))
#         chg_s += 1  
#     array.append(row)
# print(array[2][2].lower())

# char = [0] * 3
# cnt = 0
# strings = list(map(str, input()))
# for string in strings:
#     if string.isupper():
#         cnt += 1
# if cnt == 3:
#     print("풍족하다")
# elif cnt == 1 or cnt ==2:
#     print("적절하다")
# else:
#     print("부족하다")        

# arr = [[0]*4,[0]*4]
# y, x = map(int, input().split())
# arr[y][x] = 1

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print("")

# nums = list(map(int, input().split()))
# i = 0
# arr = []
# for _ in range(3):
#     row = []
#     for _ in range(2):
#         row.append(nums[i] + 2)
#         i += 1
#     arr.append(row)

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print("")

# # 8-1
# n = int(input())
# start = 1
# while start <= n:
#     print(start, end= " ")
#     start += 1

# # 8-2
# arr = list(map(int, input().split()))
# index = 0
# while index < 6:
#     if arr[index] == 7:
#         break
#     print(arr[index], end=" ")
#     index += 1

# # 8-3
# def input1():
#     global a, b
#     a, b = map(int, input().split())

# def output():
#     i = 5
#     while i <= (a + b):
#         print(i, end=" ")
#         i += 1

# input1()
# output()

# # 8.5-1
# arr = []
# inputs = input()
# for i in inputs.split():
#     arr.append(int(i))

# for i in range(len(arr)):
#     if arr[i] < 5:
#         print(f"{i}번은 {arr[i]}점 불합격")
#     else:
#         print(f"{i}번은 {arr[i]}점 합격")

# # 8.5-2
# arr = ["D", "T", "A", "B", "W", "Q"]
# s = input()
# for i in range(len(arr)):
#     if s == arr[i]:
#         print(f"{i}번 INDEX")

# # 8.5-3
# char = [0] * 5
# n = int(input())
# strings = list(map(str, input().split()))
# for i in range(n):
#     char[i] = strings[i]
#     print(char[i], end="")

# # 8.5-4
# arr = [0] * 17
# a, b, c = map(str, input().split())
# def input1():
#     for i in range(7):
#         arr[i] = a
#     for i in range(7, 13):
#         arr[i] = b
#     for i in range(13, 17):
#         arr[i] = c

# input1()
# for i in arr[::-1]:
#     print(i,end="")    

# # 8.5-5
# str1, str2, num = map(str, input().split())
# for i in range(int(num)):
#     for j in range(ord(str1),ord(str2)+1):
#         print(chr(j),end="")
#     print("")

# # 8.5-6
# s, n = map(str, input().split())
# for _ in range(int(n)):
#     for _ in range(int(n)):
#         print(s, end="")
#     print("")

# # 8.5-7
# arr = [[0] * 3 for i in range(3)]
# y, x, a = map(int, input().split())
# arr[y][x] = a

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print("")

# # 8.5-8
# arr = [[0] * 3 for i in range(6)]
# a, b = map(int, input().split())

# for i in range(3):
#     for j in range(3):
#         arr[i][j] = a
#         print(arr[i][j], end="")
#     print("")
        
# for i in range(3,6):
#     for j in range(3):
#         arr[i][j] = b
#         print(arr[i][j], end="")
#     print("")

# # 8.5-9
# str1, str2 = map(str, input().split())
# arr = [[0]*6 for _ in range(3)]
# for i in range(3):
#     for j in range(4):
#         arr[i][j] = str1
#     for j in range(4,6):
#         arr[i][j] = str2

# for i in arr:
#     for j in i:
#         print(j,end="")
#     print("")

# # 9-1
# arr = [4, 3, 6, 1, 3, 1, 5, 3]
# n = int(input())
# cnt = 0
# for i in arr:
#     if i == n:
#         cnt += 1
# print(f"숫자{n}개수는{cnt}개")

# # 9-2
# arr = [['A', 'B', 'C', 'D', 'E'], ['E', 'A', 'B', 'A', 'B'],['A', 'C', 'D', 'E', 'R']]
# s= input()
# cnt = 0
# for i in arr:
#     for j in i:
#         if s == j:
#             cnt += 1
# if cnt >= 3:
#     print("대발견")
# elif 1<= cnt <3:
#     print("발견")
# else:
#     print("미발견")


# # 9-3
# arr = ['A', 'F', 'G', 'A', 'B', 'C']
# str1, str2 = map(str, input().split())
# cnt1, cnt2 = 0, 0
# for i in arr:
#     if str1 == i :
#         cnt1 += 1
#     if str2 == i:
#         cnt2 += 1

# if cnt1 > 0 and cnt2 > 0 :
#     print("와2개")
# elif cnt1 > 0 or cnt2 > 0:
#     print("오1개")
# else:
#     print("우0개")

# # 9-4
# arr = [3, 4, 2, 5, 7, 9]
# a, b = map(int, input().split())
# temp = 0
# temp = arr[a]
# arr[a] = arr[b]
# arr[b] = temp
# for i in arr:
#     print(i, end=" ")

# # 9-6
# arr = []
# alp = ord("A")
# for i in range(3):
#     column = []
#     for j in range(3):
#         column.append(chr(alp))
#         alp += 1
#     arr.append(column)
# y1, x1 = map(int, input().split())
# y2, x2 = map(int, input().split())
# temp = 0

# temp = arr[y1][x1]
# arr[y1][x1] = arr[y2][x2]
# arr[y2][x2] = temp

# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# # 9-7
# arr = []
# for _ in range(6):
#     students = map(int, input().split())
#     arr.append(list(students))
# cnt = 0
# for i in arr:
#     if i[0] < i[1]:
#         temp = 0
#         temp = i[0]
#         i[0] = i[1]
#         i[1] = temp
#         cnt += 1

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()
# print(f"{cnt}명")    

# # 9-8
# a, b = map(int, input().split())

# def BBQ(a, b):
#     print(f"합:{a + b}")
#     print(f"차:{a - b}")
#     print(f"곱:{a * b}")
#     print(f"몫:{a // b}")

# BBQ(a, b)

# # 9-9
# arr = ['F', 'E', 'W', 'D', 'C', 'A']
# s = input()

# def findCh(s):
#     if s in arr:
#         print("발견")
#     else:
#         print("미발견")

# findCh(s)

# # 9-10
# arr = list(map(str, input().split()))
# def checkChar(s):
#     if s.isupper():
#         print("대", end="")
#     elif s.islower():
#         print("소", end="")
    

# for s in arr:
#     checkChar(s)

# # 9.5-1
# a = [2, 1, 2, 4, 5]
# b = [[2, 5, 3], [4, 5, 7], [8, 7, 2]]
# n = int(input())
# cnt = 0
# for i in a:
#     if n == i:
#         cnt += 1
# for i in b:
#     for j in i:
#         if n == j:
#             cnt += 1
# print(cnt)

# # 9.5-2
# arr = list(map(str, input().split()))
# cnt = arr.count("A")
# print(f"문자A는 {cnt}개발견")
# for i in range(5):
#     if arr[i] == "A":
#         print(f"{i}번")

# # 9.5-3
# arr = [
#     ['D', 'A', 'A'],
#     ['B', 'C', 'D'],
#     ['E', 'F', 'A'],
#     ['A', 'A', 'D'],
#     ['F',' G', 'E'],
#     ]

# s = input()
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == s:
#             print(f"({i},{j})")

# # 9.5-4
# arr = [
#     [10, 3, 20],
#     [60, 30, 40],
#     [20, 30, 40],
# ]
# a, b = map(int, input().split())
# cnt = 0
# for i in arr:
#     for j in i:
#         if a <= j <= b:
#             cnt += 1
# print(cnt)

# # 9.5-5
# def input1():
#     global arr
#     nums = list(map(str, input().split()))
#     index = 0
#     arr = []
#     for i in range(2):
#         row = []
#         for j in range(3):
#             row.append(nums[index])
#             index += 1
#         arr.append(row)

# def findUpper():
#     cnt = 0
#     for i in arr:
#         for j in i:
#             if j.isupper():
#                 cnt += 1
#     print(f"대문자{cnt}개")

# def findLower():
#     cnt = 0
#     for i in arr:
#         for j in i:
#             if j.islower():
#                 cnt += 1
#     print(f"소문자{cnt}개")

# input1()
# findUpper()
# findLower()

# # 9.5-6
# arr = [[3, 5, 14], [2, 3, 9], [6, 2, 7]]
# n = int(input())
# cnt = 0
# for i in arr:
#     for j in i:
#         if j % n == 0:
#             cnt += 1
# print(cnt)

# # 9.5-8
# inputs = int(input())

# def BBQ(n):
#     for i in range(n):
#         print(i+1, end="")

# def KFC(s):
#     for i in range(7):
#         print(s, end="")

# if inputs % 2 ==1 :
#     num = int(input())
#     BBQ(num)
# else:
#     string = input()
#     KFC(string)

# # 10-1
# def one():
#     n = int(input())
#     return n

# def two():
#     s = input()
#     return s

# print(f"{one()}{two()}")

# # 10-2
# arr = [[0]*4 for _ in range(4)]
# n = int(input())

# if n % 2 == 0:
#     for i in range(4):
#         arr[i][i] += i + 1
# else:
#     for i in range(4):
#         arr[i][3-i] += i + 1
# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10-3
# def KFC():
#     print(f"{chicken()}{coke()}")

# def chicken():
#     n = int(input())
#     return n + 10

# def coke():
#     s = input()
#     return s

# KFC()

# # 10-4
# def getChar():
#     strings = list(map(str, input().split()))
#     return sorted(strings,reverse=True)[0]

# print(getChar())

# # 10-5
# n = int(input())
# arr = [[0]*3 for _ in range(3)] 
# start = 1
# if n % 5 ==1:
#     for i in range(3):
#         for j in range(3):
#             arr[2-j][2-i] = start
#             start += 1
# elif n % 5 == 2:
#     for i in range(3):
#         for j in range(3):
#             arr[2-i][j] = start
#             start += 1
# else:
#     for i in range(3):
#         for j in range(3):
#             arr[j][i] = start + 9
#             start += 1


# for i in arr:
#     for j in i:
#         print(j,end=" ")
#     print()

# # 10-6
# def even(n):
#     printData(2 * n)

# def odd(n):
#     printData(n - 10)

# def printData(n):
#     print(n)

# a, b = map(int, input().split())

# if (a//b) %2 ==0:
#     even(a//b)
#     printData(a+b)
# else:
#     odd(a//b)
#     printData(a+b)

# # 10-7
# def GOP():
#     a, b = map(int, input().split())
#     return a * b
# def SUM():
#     a, b = map(int, input().split())
#     return a + b

# g = GOP()
# s = SUM()
# if g > s:
#     print("GOP>SUM")
# elif g < s:
#     print("GOP<SUM")
# else:
#     print("GOP==SUM")

# # 10-8
# stone = int(input())

# def pingpong():
#     tong = stone
#     return tong + 10

# ret = pingpong()
# print(ret)

# # 10-9
# arr = [[0]*4 for _ in range(4)]
# start = 1
# for i in range(4):
#     for j in range(4):
#         arr[j][3-i] = start
#         start += 1

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10-10
# n = int(input())
# start = 1
# arr = [[0] * 4 for _ in range(3)]
# for i in range(3):
#     for j in range(4):
#         arr[2-i][3-j] = start
#         start += 1

# for i in range(3):
#     arr[i][n] = 0

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10-11
# arr = []
# for _ in range(4):
#     row = list(map(int, input().split()))
#     arr.append(row)
# for i in range(4):
#     for j in range(4):
#         if arr[i][j] ==0:
#             arr[i][j] = "!"
#         elif arr[i][j] % 2 ==0:
#             arr[i][j] = "#"
#         else:
#             arr[i][j] = "@"
# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()
            
# # 10-12
# def input1():
#     n = int(input())
#     return n
# def countDown():
#     for i in range(input1(), 0, -1):
#         print(i, end=" ")

# countDown()

# # 10.5-1
# arr = [[0] * 4 for _ in range(4)]
# start = 1
# for i in range(4):
#     for j in range(4):
#         arr[j][i] = start * 2
#         start += 1
# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10.5-2
# arr = [[0] * 5 for i in range(5)]
# start = 1
# for i in range(5):
#     for j in range(5):
#         arr[j][4-i] = start
#         start += 1
# n = int(input())
# for i in range(5):
#     arr[n][i] = n

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10.5-4
# arr = [
#     ['D','A','C','C','D'],
#     ['S','D','F','A','E'],
#     ['E','E','T','J','H'],
#     ]
# def input1():
#     s = input()
#     if check(s) == 1:
#         print("있음")
#     elif check(s) == 0:
#         print("없음")
    
# def check(s):
#     for i in arr:
#         for j in i:
#             if s == j:
#                 return 1
#     return 0                    

# input1()

# # 10.5-5
# a, b, c = map(int, input().split())
# arr = [[0] * 4 for _ in range(3)]
# for j in range(4):
#     arr[0][j] = a
#     arr[1][j] = b
#     arr[2][j] = c
#     a += 1
#     b += 1
#     c += 1
# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()
    
# # 10.5-6
# a, b = map(int, input().split())
# arr = [[0]*3 for _ in range(6)]
# start = 10
# for i in range(3):
#     for j in range(6):
#         arr[j][i] = start
#         start += 1

# for i in range(a, b+1):
#     for j in range(3):
#         arr[i][j] = 7

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # 10.5-7
# def aToZ():
#     s = input()
#     if (ord(s) - 65) > (90 - ord(s)):
#         return 'Z'
#     elif (ord(s) - 65) < (90 - ord(s)):
#         return 'A'
    
# print(aToZ())

# # 10.5-8
# def Calculator():
#     score = int(input())
#     if score >= 90:
#         return 'A'
#     elif score >=80:
#         return 'B'
#     elif score >=70:
#         return 'C'
#     else:
#         return 'D'
# print(Calculator())

# # 10.5-10
# arr = [[1,0,0,0,0],
#        [1,0,1,0,0],
#        [1,1,0,1,0],
#        [1,0,1,0,0],
#        [0,1,0,0,1],
#        [0,0,0,1,0],
#        [1,1,0,0,0],
#        ]
# def INPUT():
#     n = int(input())
#     return n
# def PROCESS():
#     cnt = 0
#     i = INPUT()
#     for j in range(7):
#         if arr[j][i] == 1:
#             cnt += 1
#     return cnt

# def OUTPUT():
#     Count = PROCESS()
#     return print(Count)

# OUTPUT()

# # 10.5-11
# n = int(input())

# def run():
#     arr = [[0]*3 for _ in range(3)]
#     start = 1
#     if n < 10:
#         for i in range(3):
#             for j in range(3):
#                 arr[i][j] = start
#                 start += 1
#     else:
#         for i in range(3):
#             for j in range(3):
#                 arr[i][2-j] = start
#                 start += 1
#     for i in arr:
#         for j in i:
#             print(j, end="")
#         print()
# run()

# # 10.5-12
# def yesOrNo():
#     n = int(input())
#     if n % 3 == 0:
#         return 7
#     elif n % 3 == 1:
#         return 35
#     elif n % 3 == 2:
#         return 50

# print(yesOrNo())

# # 11-1
# def input1():
#     a, b, c = map(int, input().split())
#     return a, b, c

# def cal(a, b, c):
#     print(a+b+c)

# a, b, c = input1()
# cal(a, b, c)

# # 11-2
# a, b = map(int, input().split())

# def Sum(a, b):
#     return a + b
# def Comp(a, b):
#     return abs(a - b) 
# def Print(t1, t2) :
#     print(f'합:{Sum(t1,t2)}')
#     print(f'차:{Comp(t1,t2)}')

# Print(a,b)

# # 11-3
# a, gd = map(str, input().split())
# p = int(a)
# t = gd
# print(p, t)

# # 11-4
# a, b, c = map(str, input().split())
# x = chr(ord(a)+1)
# y = chr(ord(b)+1)
# z = chr(ord(c)+1)

# print(x, y, z)

# # 11-5
# a, b = map(int, input().split())
# p = a
# t = b
# temp = 0
# temp = p
# p = t
# t = temp
# print(p, t)

# # 11-6
# arr = [3, 4, 1, 3, 2, 7, 3]
# n = int(input())
# if n in arr:
#     print("발견")
# else:
#     print("미발견")

# # 11-7
# arr = list(map(int, input().split()))
# maximum = 0
# minimum = 2e18
# for i in arr:
#     if i > maximum:
#         maximum = i
#     if i < minimum:
#         minimum = i
# print(f'MAX={maximum}\nMIN={minimum}')

# # 11-8
# arr = ['S','t','r','u','c','t','P','o','i','n','t','e','r']
# s = input()
# for i in arr:
#     if s == i:
#         print("발견")
#         break
# else:
#     print("미발견")

# # 11-9
# arr = []
# for i in input().split():
#     arr.append(i)
# big = [0] * 8
# small = [0] * 8

# for i in arr:
#     if i.isupper():
#         big.insert(0,i)
#     if i.islower():
#         small.insert(0,i)
# filtered_big = [i for i in big if isinstance(i, str)]
# filtered_small = [i for i in small if isinstance(i, str)]
# print("".join(filtered_big))
# print("".join(filtered_small))

