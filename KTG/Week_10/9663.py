"""
9663: N-Queen
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")


# 처음에 flag를 사용했으나 시간초과, 검색후 함수로 따로 뺌
def check(i):
    for k in range(i):
        if visited[i] == visited[k]:
            return False
        if abs(visited[i] - visited[k]) == abs(i - k):
            return False
    return True


def solve(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        visited[i] = j
        if check(i):
            solve(i+1, n)


N = int(input())
visited = [-1] * N
cnt = 0
solve(0, N)
print(cnt)
"""
8

92
"""