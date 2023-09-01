# 2 x n 타일링
'''
2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
9

[출력]
첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
55
'''

'''
걍 피보나치 수열인듯
'''

n = int(input())
DP = [0 for _ in range(n + 2)]
DP[1] = 1
DP[2] = 2

def square(n):
    if DP[n]:
        return DP[n]
    else:
        DP[n] = (square(n - 1) + square(n - 2)) % 10007
    return DP[n]
    
print(square(n))