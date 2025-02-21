##################################
"""
 2025-01-22

# 소수


a = 3.14
print(type(a))
print(round(a,1))   
print(f'{a:.1f}')

a = 3.15
print(round(a,1))   #부동소수점을 이용을 해서 실수를 근사값으로 표현현

a = 1.2 - 1.1   # floating point error
print(a)

print(round(0.4))
print(round(1.4))
print(round(2.4))
print(round(3.4))
print(round(4.4))
print(round(5.4))
print("\n")
print(round(0.6))
print(round(1.6))
print(round(2.6))
print(round(3.6))
print(round(4.6))
print(round(5.6))
print("\n")
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
print("\n")

# 앞의 수가 짝수일 경우, 내림 처리
# 앞의 수가 홀수일 경우, 올림 처리

# decimal이란 모듈 사용 시 모듈이 무겁고, 느려서 별로..
# round도 부동소수점에러로 인해 제대로 작동 x
# round를 써서 소숫점을 정확하게 잘 표현하는 법 -> 꼼수
# 아아아아아아아주 작은 수를 더해줘서 오류를 줄여줌.

print(round(0.05+0.00001,1))
print(round(0.15+0.00001,1))
print(round(0.25+0.00001,1))
print(round(0.35+0.00001,1))
print(round(0.45+0.00001,1))
print(round(0.55+0.00001,1))

a = 3.12523
b = 2.72495
# 소수 두번째 자리까지 출력하기
print(round(a+1e-8,2))
print(round(b+0.0000000000001,2))
# 두 실수를 반올림해서 정수로 표현하기
print(round(a + 0.001))
from math import floor
print(floor(a+0.5))
print(floor(b+0.5))
# 0.5 더한다음에 내림 처리

##################################
# 순서 라는 개념이 있는 자료형을 살펴보자.
# str, list, tuple, range

# 오늘의 컨디션은 "100%" 입니다.
print('오늘의 컨디션은 "100%" 입니다.')
# 문자열 slicing
s = 'abcdefg'
print(s + 'abc')
print(s * 2)

print(s[:3])
print(s[3:])
print(s[2:5])
print(s[5:2:-1])
print(s[1:6:2])
print(s[::-1])
print(s[-2])

lst = [1, 2, 3, 4]
length = 0
for _ in lst:
    length +=1

print(length)

print(lst*3)

# 튜플 = 값을 바꿀 수 없는 자료형
tp = (1,2,3,4,5)
print(tp)
print(type(tp))
print(tp[1])
print(len(tp))
print(tp[-1])

# 딕셔너리 dictionary // 세트 set

# key - value 형태로 저장 (hash 라는 자료구조를 기반으로 만들어진 자료 구조)
# 순서 x, 중복 x (같은 키 값을 여러 번 사용 못함.)
di = {1:3, 2:{4:5}, '학':6, "교": [7,8,9]}
print(di)
print(type(di))
print(di[1])
print(di[2][4])
print(di['학'])
print(di['교'][2])

di[2] = '여름에는 민어탕'
print(di)

di[111] = di.pop(1)
print(di)

lst = [1,1,2,3,5,3,76,78,4,1,1,3]
print(set(lst))
print(type(set(lst)))

s1 = {1, 2, 3}
s2 = {3, 6, 9}
print(s1|s2)
print(s1-s2)
print(s1&s2) # & - ampersand

# lst = list(set(lst))
# print(lst)

a, b =0,-1
print(bool(a),bool(b))

a1 = bool('a1')
b1 = bool('')  # 빈 문자열 -> false
c1 = bool('0')
print(a1, b1, c1)

# 논리연산자
a = True
b = False
c = True
d = False
# print(a and b) # and 연산자 -> 그리고! 두 조건 모두 충족
# print(a and c) 
# print(a or b) # or 연산자 -> 둘 중 하나만 참이면 참참참

print('a' and 'b') # b
print('' and 'a') # ' '
print(0 and 1) # 0

#False면 뒤 볼 필요 없이 바로 출력, True라면 끝까지 True인지 체크 후에 출력

print(1 or 0)
print(0 or -1)
print(-1 or 1)

# True면 뒤 볼 필요 없이 바로 출력, False면 True 나올때까지 보고 출력

a = 1
b = 0
c = 3

print(a or c) # 1 논리연산자
print(a | c) # 1 비트연산(or) ???다시 확인
print(b or c) # 3
print(a and b) # 0
print(a and c) # 3
print(c and a) # 1


# 객체를 비교하는 is

a = 2 # int
b = 2.0 #float
if a is b:
    print("정답")
else:
    print("오답")


# 순서 변경 여부
# 연산자 우선 순위
# 실수값을 정확하게 출력하는 방법(아주 작은 값(1e-8)을 더해서 round 처리)
#     1. decimal 모듈 사용
#     2. 아주 작은 값 더하기
#     3. +0.5 한 후에 floor 처리

# 깊은 복사 / 얕은 복사

# 깊은복사
lst = [1,2,3]
lst2 = lst # 재할당
lst[0] = 100
print(lst2[0]) # 100

# 얕은복사
lst = [1,2,3]
lst2 = lst[:]
lst[0] = 100
print(lst2[0]) # 1

import copy
lst = [[1,2],[3,4]]
lst2 = copy.deepcopy(lst)
lst[0][0] = 100
print(lst2[0][0])



##########################################################
# 2025-01-22

# function
def getSum(a, b): # 매개변수 parameter
    return a + b, a* b

result = getSum(3, 7) # 인자값 argument
print(result)

# 예시 - argument와 parameter 개수가 다를 경우
    # 1.default parameter -> 항상 뒤에 적어줄 것
def getSum(a, b, c = 3): # 매개변수 parameter
    return a + b + c

result = getSum(3, 7) # 인자값 argument
print(result)

    # 2.packing / unpacking
num = [1, 2, 3, 4, 5]
num2 = (1, 2, 3, 4, 5)
print(num, num2)

a, b, c, d, e = num # unpacking
print(a, b, c)

a, b, *c = num2
print(a, b, c)
print(c)

def getsum(*a):
    print(type(a))
    return a[0] + a[1] + a[2]

result = getsum(1, 2, 3)
print(result)

    # 3.키워드 가변인자 (kargs)
def print_info(**args):
    print(args)
    print(type(args))
    for i, j in args.items():
        print(i,j)
    
print_info(kevin=1, john=2, bob=3) # kevin:1 딕셔너리 형태로 적어서는 안됨


# 지역변수 전역변수

aa = 3
bb = 5

def test():
    global aa, bb # 전역변수 선언언
    print(aa, bb) # 3 5
    aa += 1
    bb += 1
    print(aa, bb) # 4 6

test()
print(aa, bb) # 4 6

def abc():
    aa = 3 # 지역변수
    bb = 5
    print(aa, bb)

abc()
print(aa)

# 변수를 바깥에 적었다 하더라도, 재할당 하는 경우(값을 변경)에는 "global 선언 해줘야 함"

# 전역변수

def kfc():
    print(aa, bb)
    global aa, bb # 변수의 값을 변경했기 때문에 global 선언 필수수
    aa += 1
    bb += 1
    print(aa, bb)

def test():
    global aa, bb
    aa = 3
    bb = 5
    print(aa, bb)

test()
kfc()

# 지역변수 - 함수 안에서만 적용되는 변수
# 전역변수 - 다른 함수에서도 공통적으로 사용하는 변수 (출력 시 global 생략 가능)
        # - 그러나 값을 재할당시 global 반드시 적어주기!

# LEGB 규칙 한번 더 체크

# 내장함수
# 파이썬 내장함수 중 - map, zip, filter, rambda함수
# map - 리스트나 튜플 같이 순회가 가능한 데이터 구조의 값에 일괄적으로 함수를 적용할 때 사용
    # - 반환값은 map 객체를 반환!
    # - map(함수, iterables(순회가능한 객체))
 
num = ['1', '2', '3']
lst1 = []
for i in num:
    lst1.append(int(i))
print(lst1)

lst2 = map(int, num)
print(lst2)
print(list(lst2))

a, b, c = map(int, input().split())
print(a, b, c)

lst = list(map(int, input().split()))
print(lst)
# split() - 공백을 기준으로 입력받겠다

# zip - 순회 가능한 객체를 인자로 받고 각 요소를 잘라서 "튜플"을 원소로 하는 객체를 반환한다. (+ 길이가 다른 경우, 길이가 가장 짧은 요소를 기준으로 잘림림)

a = '12345'
b = 'qwert'
c = 'asdfgrrrrr' 

for i in zip(a, b, c):
    print(list(i))

for x, y, z in zip(a, b, c): # 튜플 언패킹
    print(x, y, z)

# ret = zip(a, b)
# print(ret)
# print(list(ret))

# 활용 사례
# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ]

for i in zip(arr[0], arr[1], arr[2]):
    print(list(i))

for i in zip(*arr):
    print(list(i))


arr = list(map(list,zip(*arr))) # 90도 돌려버림

for i in arr:
    for j in i:
        print(j, end=" ")
    print()


for i in range(3):
    for j in range(3):
        print(i, j,end=" ")
        print()

# filter -리스트나 튜플과 같이 순회 가능한 데이터 구조의 값들을 함수에 적용, 적용 후 값이 True인 것들만 반환 (filter라는 객체로)

num = list(range(1,10))

def get_even(value):
    if value % 2 == 0:
        return True
    else:
        return False
ret = filter(get_even, num)

print(list(ret))


# lambda - 이름이 없는 익명함수

def Sum(a, b):
    return a + b
result = Sum(3, 5)
print(result)

result = (lambda a, b : a+ b)(3, 5)
print(result)

result = (lambda a, b : a+ b)
print(result(3, 5))

# 연습문제 1
# 두 리스트값을 세로로 더했을 때 합을 각각 출력하기
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
# 1
lst = list(zip(lst1,lst2))

for i in lst:
    total = 0
    for j in i:
        total += j
    print(total, end=" ")
# 2
lst3 = [0] * 5
for i in range(5):
    lst3[i] = lst1[i] + lst2[i]
print(*lst3)
# 3
result = (lambda x, y : x+ y)
lst3 = map(result,lst1,lst2)
print(*lst3)
# 4 
lst3 = map(lambda x, y : x + y, lst1, lst2)
print(*lst3)

# 연습문제2
# 0~100 사이의 정수 중 짝수만 리스트에 담아서 출력해보기
# 1
even_lst = []
for i in range(0,100,2):
    even_lst.append(i)
print(even_lst)
# 2
result = filter(lambda even: even % 2 == 0, range(100))
print(list(result))


# 재귀함수 recursion

def abc():
    print("##")
    abc()
    print("##")

abc()

주사위 n개 던졌을 때 경우의 수수
n = int(input())
path = [0] * n

def abc(level):
    if level ==n:
        for i in range(n):
            print(path[i],end=" ")
    for i in range(6):
        path[level] = i+1
        abc(level+1)
abc()

def abc():
    global man

    lst[0] = 100
    arr = [100, 2, 3]
    man = [100, 2, 3]

lst = [1,2,3]
arr = [1,2,3]
man = [1,2,3]

abc()

print(lst)
print(arr)
print(man)

# 결론 : 변수 같은 경우, 전역변수의 값을 바꾸는 경우가 아니라면 global 생략가능 
        # 그러나 값을 재할당시 global 필수
# 리스트는... 리스트의 값을 바꾸는 것은 허용(global 생략 가능)
            # 리스트의 재할당은 반드시 global 써야함

def abc():
    mc[0][0] = 100
    kfc[0] = [100,2,3]
    bbq = [[100, 2, 3], [4, 5, 6]]

mc = [[1, 2, 3], [4, 5, 6]]
kfc = [[1, 2, 3], [4, 5, 6]]
bbq = [[1, 2, 3], [4, 5, 6]]

abc()
print(*mc)
print(*kfc)
print(*bbq)

###################################
# 2025.01.24
st = 'apple,banana,mango'

index = st.find('b')
print(index) # 6

index = st.find('z')
print(index) # -1 (찾는 값이 없는 경우)

index = st.find('p')
print(index) # 1 (찾는 값이 여러 개인 경우, 첫번째 해당값 출력 후 종료)

alpha = st.index('p')
print(alpha)


st = 'apple,banana,mango'
# 모두 대문자인지 || 모두 소문자로
print(st.isupper()) # False
print(st.islower()) # True
print(st.isalpha()) # False

st = ['apple','banana','mango']
st.append('orange') # 맨 뒤에 추가
st.insert(1,'orange') # 원하는 위치에 추가 (이동하고자 하는 위치, 추가하는 객체)
print(st)
a = st.find('orange')
# a = st.index('orange')
print(a)

lst = [(3, 'banana'), (2, 'apple'), (1, 'carrot')]
ret = sorted(lst)
print(ret)
ret = sorted(lst, key=lambda x:x[1], reverse=True)
print(ret)
"""

# import requests

# # 하드 코딩하는 변수
# URL = 'https://fakestoreapi.com/carts' # 요청 주소
# # .get(URL) : URL 주소에 요청을 보내는 메서드
# data = requests.get(URL)
# # 출력결과: <Response [200]>
# # [200]: 웹의 응답 코드 -> 정상적으로 응답하였습니다.
# # [400]: 웹의 응답 코드 -> 알 수 없는 주소로 요청했다.
# print(data)

# # .json(): 데이터를 JSON 형태로 변환해주는 메서드
# json_data = data.json()
# print(json_data)


#########################################
# 2025-01-31
# set(중복을 허용 x)
# s = {1,2,3,4,5}

# # 값 추가
# s.add(6)
# s.update([11,12,13,14])
# print(s)
# # 값 삭제
# s.remove(6)
# print(s)

st = {'kevin':1, 'john':2, 'bob':[3,4,5]}

# ls_key = ['asdf', 'zcv', 'qwe']
# ls_value = [1,2,3]

# for i in range(3):
#     st[ls_key[i]] = ls_value[i]
# print(st)


# for i in range(3):
#     st.update({ls_key[i]:ls_value[i]}) # 인자값으로 dictionary를 받음

# temp = dict(zip(ls_key,ls_value))
# st.update(temp)

# for i in range(3):
#     st.setdefault(ls_key[i], ls_value[i])
#     # 이미 존재하는 key 값을 입력할 경우 - 원본 값 변하지 않음(원본 값 보호)
#     st.setdefault('kevin', 1000) # {'kevin':1, ...}

# from collections import Counter
# lst = ['apple','mango','banana','mango','apple','mango','banana','mango','apple']
# # print(Counter(lst))
# ret = dict(Counter(lst))
# # print(ret) # 딕셔너리 형태 출력
# # print(Counter('an applemango'))
# st = 'an applemango'
# # + st 문자열에서 가장 많이 사용된 알파벳을 출력해주세요.
# ret = dict(Counter(st))
# ret = sorted(ret.items(), key=lambda x: x[1], reverse=True)
# print(ret[0][0])

# st = 'an applemango'
# ret = Counter(st).most_common(1)
# print(ret[0][0])

# a = Counter('apple')
# b = Counter('mango')
# print(a + b)
# print(a - b)

# class Calculator:
#     numberOfCalcul = 0 # 모든 인스턴스가 같이 사용할 변수 (=클래스 변수(속성)(attribute))
#     def __init__(self): # '__' : 매직메서드
#         # __init__: 생성자 함수, constructor, 인스턴스 생성시 자동으로 실행되는 함수
#         self.result = 0 # 각각의 인스턴스를 위한 변수 (=인스턴스 변수(속성)(attribute))
#         Calculator.numberOfCalcul += 1

#     def getsum(self, value):
#         self.result += value
#         return self.result
    
    
# cal1 = Calculator() # ->self는 cal1이 됨됨
# print(cal1.numberOfCalcul) # 1
# cal2 = Calculator()
# print(cal2.numberOfCalcul) # 2

# # 주의
# # 클래스 변수의 값을 변경 시 반드시 클래스로 접근해서 값 변경해야 함
# # 예시
# Calculator.numberOfCalcul = 5
# cal1.numberOfCalcul = 20 # 인스턴스로 클래스 변수 변경 (잘못된 예시)
# print(cal1.numberOfCalcul)
# print(cal2.numberOfCalcul)
# # print(cal1.result)
# # cal1.getsum(3)
# # print(cal1.result)
# # cal1.getsum(4)
# # print(cal1.result)
# # cal1.getsum(5)
# # print(cal1.result)

# # 두 수의 값을 더한 값 그리고 뺀 값을 돌려주는 클래스
# # 파이썬에서 클래스를 만들때.. 생성자 함수 작성
# class PlusMinus:
    
#     # def data(self, first, second): # 생성자함수 안쓰고 하는 방법
#     #     self.first = first
#     #     self.second = second
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
    
#     def plus(self):
#         result = self.first + self.second
#         return result

#     def minus(self):
#         result = self.first - self.second
#         return result
    
# # a = PlusMinus()
# # a.data(3, 5) # 생성자 함수 없이 사용하는 법
# # b = PlusMinus()
# # b.data(4, 6)
# # print(a.first, b.first)

# a = PlusMinus(3,5)
# print(a.plus())
# print(a.minus())


# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __add__(self, another):
#         return self.price + another.price

#     def __str__(self):
#         return f'{kia.name}의 가격은 {kia.price}입니다.'
# kia = Car('K8', 300)
# bmw = Car('m5', 500)
# print(kia.price + bmw.price) # 800

# print(kia + bmw) # __add__

# print(f'{kia.name}의 가격은 {kia.price}입니다.')
# print(kia) # __str__

# del kia # 인스턴스 삭제 시

# 속성 = 클래스속성(변수) / 인스턴스속성(변수)
# 메소드 = 인스턴스 메소드 (인스턴스로 메소드 접근 오케이)
#          정적 메소드 (static method)
#          클래스 메소드 (class method) -> 인스턴스로 접근하지 말고 클래스로 해당 메소드를 호출하세요!!!

# @classmethod 데코레이터(함수를 꾸며주는 역할)
# @staticmethod

# def deco(func):
#     def wrapping(value):
#         print('우유빛깔')
#         func(value)
#         print('화이팅')
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)

# call_name('혜민')
# call_age('29')

# class car : 
#     def __init__(self, name, price) : 
#         self.name = name
#         self.price = price

#     @staticmethod
#     def add_price(one, another):
#         print(one + another)

# kia = car('k8', 300)
# bmw = car('m5', 500)

# car.add_price(500, 700)


class MakePies:
    cnt=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        MakePies.cnt += 1

    @classmethod
    def number_of_pies(cls):
        print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

    @classmethod
    def from_birthday_year(cls, name, birthyear):
        age = 2025 - birthyear # 현재 연도를 기준으로 나이를 계산
        return cls(name, age)
    

a = MakePies('kevin', 40)
b = MakePies('jane', 35)
MakePies.number_of_pies()

# class 변수 사용하는 이유(경우)
# 1. 클래스로 클래스 변수에 접근하고자 하는 경우
# 2. 클래스 내 생성자 함수를 대체해서 인스턴스를 생성할 때  사용

c = MakePies.from_birthday_year('bob', 1990)

##########################
#0204#

# class PlusMinus:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def plus(self):
#         result = self.first + self.second
#         return result
#     def minus(self):
#         result = self.first - self.second
#         return result
    
# # 하위 클래스를 하나생성
# # 숫자 3개의 곱을 생성해주는 하위클래스
# class MoreFunction(PlusMinus):
#     def __init__(self, first, second, third):
#         super().__init__(first, second) # 부모 클래스의 init메서드를 그대로 호출하는 경우
#         self.third = third

#     def mul(self):
#         result = self.first * self.second * self.third
#         return result
    
#     def plus(self):
#         result = self.first + self.second + self.third
#         if result > 100:
#             print('버그')
#         else:
#             return print(result)
        
#     def parent_plus(self):
#         result = super().plus()
#         return result

# # b = MoreFunction(3, 4, 5)
# # print(b.mul())
# # print(b.plus())

# c = MoreFunction(77,22,11)
# c.plus()
# print(c.parent_plus())
# # 부모 클래스의 plus 메서드를 자식 클래스에서 수정을 하고자 한다.
# # plus 메서드는 숫자 2개가 아닌 숫자 3개의 합을 출력하는 메서드로 바꾸고, 
# # 만약에 숫자의 합이 100이 넘는다면 '버그'라고 출력이 되도록 수정해보자.


# # 메서드 오버로딩 VS 메서드 오버라이딩

# # 메서드 오버로딩
# # 클래스 내부에 같은 이름의 여러 메서드를 정의하는 것

# # 메서드 오버라이딩
# # 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다는 뜻

# # 다형성: 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다는 뜻으로 예를 들어 메서드 오버라이딩을 들 수가 있다.
# # 상속: 자식 클래스가 부모 클래스로부터 메서드 또는 속성 등을 상속받아서 사용하는 것
# # 추상화: 하위 객체에 각각 객체의 고유 기능만 추가하는 것 (EX. 자동차라는 공통 속성은 상위 클래스에 정의하고, 특정 브랜드의 속성을 하위 클래스에 정의) 
# # 캡슐화: 클래스 내 객체(속성 또는 메서드)를 외부에서 수정하지 못하도록 막는 것
# # (public - 일반적으로 사용하는

# # protected- '암묵적 규칙'에 의해 메서드를 호출 시 부모 클래스 내부나 자식 클래스에서만 호출이 가능하다 
#         # 변수 앞에 _(protected된 상태)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age # '_' 사용으로 protected 표현
#     def getage(self):
#         return self._age


# p1 = Person("홍길동", 20)
# print(p1._age) 
# # 사용은 가능하나 따로 메서드를 이용해서 클래스 안애서 접근을 하도록 한다.
# print(p1.getage())

# #  private- )
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age # '__' 사용으로 private 처리 표현
#     def getage(self):
#         return self.__age

# p1 = Person("홍길동", 20)
# print(p1.name)
# print(p1.__age)
# # 출력 불가능
# print(p1.getage())

# # 캡슐화된 속성값을 변경 가능
# # getter 데코레이터는 private한 변수 값을 읽을 목적으로 만든 것
# # setter 데코레이터는 private한 변수 값을 변경할 목적으로 만든 것
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age 
        
#     @property # getter함수 위에는 @property라고 적어주고, 비공개 속성의 값을 읽기 위한 용도로 사용한다.
#     def age(self): # @property를 사용함으로써 가독성 향상상
#         return self.__age


#     @age.setter # @메서드명.setter라고 적어준다. 비공개 속성의 값을 변경하기 위한 용도로 사용한다.
#     def age(self,value):
#         self.__age = value
    
# # getter setter 사용시에는 () 생략을 권장
# k = Person('홍길동',330)
# print(k.age) # getter
# k.age = 20
# print(k.age) # setter


# # 에러
# # 잘못된 문법으로 인하여 어떤 에러 메시지가 뜨는 지 확인해보는 시간
# if True:
#     print("참")
# else
#     print("거짓")
# # : 누락으로 문법 에러
# # SyntaxError: invalid syntax

# print('hi)
# # '누락으로 문법 에러 예제
# # EOL while

# a = 10 * (1/0)
# # ZerodivisionError

# print(abc)
# # NameError: name 'abc' is not defined
# # 선언하지 않은 변수의 값을 출력

# a = 1 + '1'
# # TypeError: unsupported operand type(s) for + 

# a = round('3.5')
# # TypeError

# import random
# random.sample([1,2,3])
# # TypeError: sample() missing 1 required positional argument: 'k'
# # 매개변수 누락

# a = int('3.5')
# # ValueError

# numbers = [1,2]
# numbers.index(3)
# # ValueError

# empty_list = []
# empty_list[-1]
# # IndexError

# songs = {'1':2,'2':r}
# songs['3']
# # KeyError

# # ModuleNotFoundError

# # IndentationError
# # 들여쓰기를 잘못한 경우


# # 문자열 안의 값을 바꿀 수 없음

