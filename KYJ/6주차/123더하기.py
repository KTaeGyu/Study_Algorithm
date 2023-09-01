# 9095번 1, 2, 3더하기
'''
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

[입력]
3
4
7
10

[출력]
7
44
274
'''
'''
DP[n] = DP[n - 1] + DP[n - 2] + DP[n - 3]
'''
def f(n):
    if DP[n]:
        return DP[n]
    else:
        DP[n] = f(n - 1) + f(n - 2) + f(n - 3)
        return DP[n]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    if n >= 3:
        DP = [0 for _ in range(n + 1)]
        DP[1] = 1
        DP[2] = 2
        DP[3] = 4
        print(f(n))
    else:
        print(n)


## n이 양수라고만 해서 1,2,3 일 때에도 고려해줘야한다.