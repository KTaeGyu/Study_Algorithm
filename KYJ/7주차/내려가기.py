# 2096번 내려가기
'''
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 
이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 
그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 


[입력]
3
1 2 3
4 5 6
4 9 0

[출력]
최대 점수와 최소 점수를 띄어서 출력한다.
18 6
'''

# readline 안쓰면 시간초과남^...
import sys
input = sys.stdin.readline

N = int(input())
maxv = [0 for _ in range(3)]
minv = [0 for _ in range(3)]
for i in range(N):
    a, b, c = map(int,input().split())
    if not i:       # 초기 조건 설정
        maxv = [a, b, c]
        minv = [a, b, c]
    else:
        maxv = [max(maxv[0], maxv[1]) + a, max(maxv)+ b, max(maxv[1], maxv[2]) + c]
        minv = [min(minv[0], minv[1]) + a, min(minv)+ b, min(minv[1], minv[2]) + c]

print(max(maxv), min(minv))
        


# # 이래도 메모리 초과 남 input받고 그냥 바로 해버려
# N = int(input())
# MAP = [list(map(int,input().split())) for _ in range(N)]
# maxv = []
# minv = []
# for k in range(3):
#     maxv.append(MAP[0][k])
#     minv.append(MAP[0][k])
# for i in range(1, N):
#     maxv[0] += max(MAP[i][0], MAP[i][1])
#     maxv[1] += max(MAP[i][0], MAP[i][1], MAP[i][2])
#     maxv[2] += max(MAP[i][2], MAP[i][1])
#     minv[0] += min(MAP[i][0], MAP[i][1])
#     minv[1] += min(MAP[i][0], MAP[i][1], MAP[i][2])
#     minv[2] += min(MAP[i][2], MAP[i][1])
# print(max(maxv), min(minv))
    










# 메모리 초과 남
# N = int(input())
# MAP = [list(map(int,input().split())) for _ in range(N)]
# DP = [[(0, 0) for _ in range(3)] for _ in range(N)]

# for i in range(3):
#     DP[0][i] = (MAP[0][i], MAP[0][i])

# for i in range(1, N):
#     DP[i][0] = (MAP[i][0] + max(DP[i - 1][0][0], DP[i - 1][1][0]), MAP[i][0] + min(DP[i - 1][0][1], DP[i - 1][1][1]))
#     DP[i][1] = (MAP[i][1] + max(DP[i - 1][0][0], DP[i - 1][1][0], DP[i - 1][2][0]), MAP[i][1] + min(DP[i - 1][0][1], DP[i - 1][1][1], DP[i - 1][2][1]))
#     DP[i][2] = (MAP[i][2] + max(DP[i - 1][2][0], DP[i - 1][1][0]), MAP[i][2] + min(DP[i - 1][2][1], DP[i - 1][1][1]))

# maxv = 0
# minv = float('INF')
# for k in range(3):
#     a, b =DP[N - 1][k][0], DP[N - 1][k][1]
#     if a > maxv:
#         maxv = a
#     if b < minv:
#         minv = b

# print(maxv, minv)