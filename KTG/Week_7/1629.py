"""
자연수 A를 B번 곱한 수를 알고 싶다.
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

A, B, C = map(int, input().split())
dp = [0] * (B+1)
dp[0] = 0
for i in range(1, B+1):
    dp[i] = A**i % C
print(dp)
print(dp[B])

"""
10 11 12

4
"""