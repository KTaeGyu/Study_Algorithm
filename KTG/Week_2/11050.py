# ----------------------------------------------------------------------------------------------------------문제
# 자연수 N과 정수K가 주어졌을 때 이항 계수 (N/K)를 구하는 프로그램을 작성하시오.

# ------------------------------------------------------------------------------------------------------예제 입력
# 첫쨰 줄에 N과 K가 주어진다.
# 5 2

# ------------------------------------------------------------------------------------------------------예제 출력
# (N/K)를 출력한다.
<<<<<<< HEAD
from math import factorial

N, K = map(int, input().split())

def combination(num1, num2):
    result = factorial(num1) / factorial(num1 - num2) / factorial(num2)
    return int(result)

print(combination(N, K))
=======
# 10
>>>>>>> b4fca9ba19c9bd6543d5e3030b19b01de5398286

# --------------------------------------------------------------------------------------------------알고리즘 분류
# 수학
# 구현
<<<<<<< HEAD
# 조합론

# ----------------------------------------------------------------------------------------------------------풀이
# 직접 구현했다가 런타임 에러 (재귀함수가 깊어지면 날 수 있음)
# N, K = map(int, input().split())

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# def combination(num1, num2):
#     result = factorial(num1) / factorial(num1 - num2) / factorial(num2)
#     return int(result)

# print(combination(N, K))
=======
# 조합론 

# ----------------------------------------------------------------------------------------------------------풀이
# from math import factorial
>>>>>>> b4fca9ba19c9bd6543d5e3030b19b01de5398286

# N, K = map(int, input().split())

# def combination(num1, num2):
#     result = factorial(num1) / factorial(num1 - num2) / factorial(num2)
#     return int(result)

# print(combination(N, K))

# ------------------------------------------------------------------------------------------------------풀이 과정
# 팩토리얼을 구현했다가 시간초과
# N, K = map(int, input().split())

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# print(factorial(N) / factorial(N - K) / factorial(K))