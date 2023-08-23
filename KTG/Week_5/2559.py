"""
매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,
    3 -2 -4 -9 0 3 7 13 8 -3
모든 연속적인 이틀간의 온도의 합은 아래와 같다.
이때, 온도의 합이 가장 큰 값은 21이다.
또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,
이때, 온도의 합이 가장 큰 값은 31이다.
매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다.
N은 2 이상 100,000 이하이다. 두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다.
둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.

첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

N, K = map(int, input().split())
temp = list(map(int, input().split()))

sum_l = [0]*(N+1)
for i in range(N):
    sum_l[i+1] = temp[i] + sum_l[i]

max_v = float('-inf')
for i in range(N - K + 1):
    sum_k = sum_l[i+K] - sum_l[i]
    max_v = max(max_v, sum_k)

print(max_v)

"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3

21
"""

"""시도1
def add_v(i, n):
    global max_v
    if i >= n:
        return
    elif sum(bit) == K:
        sum_v = 0
        for i in range(N):
            if bit[i] == 1:
                sum_v += temp[i]
        if max_v < sum_v:
            max_v = sum_v
        return
    elif i > K-1 and bit[i-K] == 1 and bit[i] == 0:
        return
    else:
        bit[i] = 1
        add_v(i+1, n)
        bit[i] = 0
        add_v(i+1, n)


N, K = map(int, input().split())
temp = list(map(int, input().split()))
bit = [0]*N
max_v = 0
add_v(0, N)
print(max_v)
"""

"""시도2
N, K = map(int, input().split())
temp = list(map(int, input().split()))
result = []
for i in range(N-K+1):
    sum_v = sum(temp[i:i+K])
    result.append(sum_v)
print(max(result))
"""