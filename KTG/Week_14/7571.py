import sys
input = sys.stdin.readline

# 입력값
N, M = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(M)]

# 중앙값 찾기
dots_y, dots_x = list(zip(*dots))
center_x = sorted(list(dots_x))[M//2]
center_y = sorted(list(dots_y))[M//2]

# 거리 계산
result = 0
for dot_y, dot_x in dots:
    result += abs(center_y - dot_y) + abs(center_x - dot_x)

print(result)
