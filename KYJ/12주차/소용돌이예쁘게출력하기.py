# 1022번 백준 소용돌이 예쁘게 출력하기
import sys
sys.setrecursionlimit(10 ** 6)
# 반시계 모양
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
r1, c1, r2, c2 = map(int,input().split())
# 나와야하는 총 갯수 = 
n = (r2 - r1 + 1) * (c2 - c1 + 1)
result = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]

gotcha = 0
# 만약 0, 0이 포함된다면 좌표가 어디일까? (-r1, -c1)이 0,0이된다
# 돌리기전에, 1, 2, 3이 있다면  넣어주자
if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    result[-1 * r1][-1 * c1] = 1
    gotcha += 1
if r1 <= 0 <= r2 and c1 <= 1 <= c2:
    result[-1 * r1][-1 * c1 + 1] = 2
    gotcha += 1
if r1 <= -1 <= r2 and c1 <= 1 <= c2:
    result[-1 * r1 - 1][-1 * c1 + 1] =3
    gotcha += 1


def roll(length, dir_idx, number, location):
    global gotcha
    if gotcha == n:
        return
    cy, cx = location
    for _ in range(2):
        dy, dx = dir[dir_idx]
        for _ in range(length):
            number += 1
            cy += dy
            cx += dx
            if r1 <= cy <= r2 and c1 <= cx <= c2:
                y, x = cy - r1, cx - c1
                result[y][x] = number
                gotcha += 1
        dir_idx = (dir_idx + 1) % 4
        
    roll(length + 1, dir_idx, number,(cy, cx))

roll(2, 0, 3, (-1, 1))
max_len = 1
for i in range(r2- r1 + 1):
    if len(str(max(result[i]))) > max_len:
        max_len = len(str(max(result[i])))
k = 0
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        k += 1
        print(str(result[i][j]).rjust(max_len), end=" ")
    print()






# 1. 그냥 배열 만들고 출력을 했더니 메모리 제한이 걸려버림... 
# 2. 시간 초과 돌아버리겠다
# # 반시계 모양
# dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# r1, c1, r2, c2 = map(int,input().split())
# # 나와야하는 총 갯수 = 
# n = (r2 - r1 + 1) * (c2 - c1 + 1)

# # 좌표들 중 최대값 기준으로 최대 x 최대 행렬을 만들어줄까?
# #  1, 2, 2, 3, 3, 4, 4, 5, 5, ... 개마다 방향 전환이 된다

# # # 인덱스(N)이 있는 좌표를 넣을 arr
# # arr = [(0, 0), (0, 0), (0, 1), (-1, 1)]   # 0번은 그냥 빼고, 1번은 (0, 0) 2번은 (0, 1) 3번은 (-1, 1)
# # # 3번부터 시작이니까 2, 2, 3, 3, 4, 4, ..


# result = []

# # 돌리기전에, 1, 2, 3이 있다면  넣어주자
# if r1 <= 0 <= r2 and c1 <= 0 <= c2:
#     result.append((0, 0, 1))
# if r1 <= 0 <= r2 and c1 <= 1 <= c2:
#     result.append((0, 1, 2))
# if r1 <= -1 <= r2 and c1 <= 1 <= c2:
#     result.append((-1, 1, 3))


# # 4 이후는 돌려
# num = 3
# cy, cx = -1, 1
# i = 2 # 몇칸 갈껀지?
# dir_i = 0

# while len(result) < n:
#     dy, dx = dir[dir_i]
#     for _ in range(i):
#         num += 1
#         cy += dy
#         cx += dx
#         if r1 <= cy <= r2 and c1 <= cx <= c2:
#             result.append((cy, cx, num))
#     dir_i = (dir_i + 1) % 4
#     dy, dx = dir[dir_i]
#     for _ in range(i):
#         num += 1
#         cy += dy
#         cx += dx
#         if r1 <= cy <= r2 and c1 <= cx <= c2:
#             result.append((cy, cx, num))
#     dir_i = (dir_i + 1) % 4
#     i += 1


# result.sort()
# k = 0
# max_num = max(result,key=lambda x:x[2])
# max_len = len(str(max_num[2]))

# for y, x, num in result:
#     k += 1
#     print(str(num).rjust(max_len), end=" ")
#     if k == c2 - c1 + 1:
#         k = 0
#         print()
