"""
자연수 A를 B번 곱한 수를 알고 싶다.
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")


def solve(a, b, c):
    if b == 1:
        return a % c
    else:
        nxt = solve(a, b//2, c)
        if b % 2 == 0:
            return nxt * nxt % c
        else:
            return nxt * nxt * a % c


A, B, C = map(int, input().split())
result = solve(A, B, C)
print(result)

"""
10 11 12

4
"""