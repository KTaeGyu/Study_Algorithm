"""
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2^N-1 × 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
다음 예는 2^2 × 2^2 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
다음은 N=3일 때의 예이다.

첫째 줄에 정수 N, r, c가 주어진다.

r행 c열을 몇 번째로 방문했는지 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

N, r, c = map(int, input().split())
cnt = 0


def z_search(num, sy, sx):
    global cnt
    if num == 1:
        if sy == 0 and sx == 0:
            return
        elif sy == 0 and sx == 1:
            cnt += 1
        elif sy == 1 and sx == 0:
            cnt += 2
        elif sy == 1 and sx == 1:
            cnt += 3
    else:
        if sy < 2 ** (num - 1) and sx < 2 ** (num - 1):
            ny = sy
            nx = sx
            z_search(num-1, ny, nx) 
        elif sy < 2 ** (num - 1) and sx >= 2 ** (num - 1):
            ny = sy
            nx = sx - 2 ** (num - 1)
            cnt += 4 ** (num - 1)
            z_search(num-1, ny, nx)
        elif sy >= 2 ** (num - 1) and sx < 2 ** (num - 1):
            ny = sy - 2 ** (num - 1)
            nx = sx
            cnt += 4 ** (num - 1) * 2
            z_search(num-1, ny, nx)
        elif sy >= 2 ** (num - 1) and sx >= 2 ** (num - 1):
            ny = sy - 2 ** (num - 1)
            nx = sx - 2 ** (num - 1)
            cnt += 4 ** (num - 1) * 3
            z_search(num-1, ny, nx)


z_search(N, r, c)
print(cnt)


"""풀이 과정
처음에 재귀를 이용하여 풀어보았지만, 시간초과가 났음.
분할 정복에 대한 개념을 알아야 할듯. 공부하고 다시 풀음.
Z 모양을 작은것 부터 순서대로 카운트 하는 방법 대신 큰 네 구역으로 나누어 카운트를 한번에 더하고 좌표를 옮기는 방식으로 바꾸어 시간복잡도를 해결함.
N, r, c = map(int, input().split())
cnt = 0


def z_search(num, sy, sx):
    global cnt
    z_order = [[sy + 0, sx + 0], [sy + 0, sx + 2 ** (num - 1)], [sy + 2 ** (num - 1), sx + 0], [sy + 2 ** (num - 1), sx + 2 ** (num - 1)]]
    if num == 1:
        for y, x in z_order:
            if y == r and x == c:
                raise ValueError
            else:
                cnt += 1
    else:
        for y, x in z_order:
            z_search(num - 1, y, x)


try:
    z_search(N, 0, 0)
except ValueError:
    print(cnt)
"""

"""
2 3 1

11
"""