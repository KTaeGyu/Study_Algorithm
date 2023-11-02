"""
문제
n × n의 크기의 대나무 숲이 있다.
욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다.
그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다.
그리고 또 그곳에서 대나무를 먹는다.
그런데 단 조건이 있다.
이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다.
우리의 임무는 이 사육사를 도와주는 것이다.
n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

입력
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다.
그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다.
대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다.
대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")


# dfs + dp, 먹으면서 이동한다 개념 대신 그 자리에서 몇 칸까지 이동할 수 있는가를 기록하며 이동
def move(sy, sx):
    if visited[sy][sx]:
        return visited[sy][sx]
    visited[sy][sx] = 1
    for dy, dx in directions:
        ny, nx = sy + dy, sx + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if arr[sy][sx] >= arr[ny][nx]:
            continue
        visited[sy][sx] = max(visited[sy][sx], move(ny, nx) + 1)
    return visited[sy][sx]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * n for _ in range(n)]
result = 0
for y in range(n):
    for x in range(n):
        result = max(result, move(y, x))

print(result)

"""
예제 입력 1 
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

예제 출력 1 
4
"""