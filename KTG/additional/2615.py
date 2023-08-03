# ----------------------------------------------------------------------------------------------------------문제
# 오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다. 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 
# 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.

# 위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다. 
# 여기서 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻한다. 즉, 위의 그림은 검은색이 이긴 경우이다. 
# 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.

# 입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오. 
# 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.

# ------------------------------------------------------------------------------------------------------예제 입력
# 19줄에 각 줄마다 19개의 숫자로 표현되는데, 검은 바둑알은 1, 흰 바둑알은 2, 알이 놓이지 않는 자리는 0으로 표시되며, 숫자는 한 칸씩 띄어서 표시된다.
"""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
# ------------------------------------------------------------------------------------------------------예제 출력
# 첫줄에 검은색이 이겼을 경우에는 1을, 흰색이 이겼을 경우에는 2를, 아직 승부가 결정되지 않았을 경우에는 0을 출력한다. 
# 검은색 또는 흰색이 이겼을 경우에는 둘째 줄에 연속된 다섯 개의 바둑알 중에서 가장 왼쪽에 있는 바둑알
# (연속된 다섯 개의 바둑알이 세로로 놓인 경우, 그 중 가장 위에 있는 것)의 가로줄 번호와, 세로줄 번호를 순서대로 출력한다.
"""
1
3 2
"""
# --------------------------------------------------------------------------------------------------알고리즘 분류
# 구현
# 브루트포스

# ----------------------------------------------------------------------------------------------------------풀이
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")


def find_rank(chess_board):
    rank = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    over = [(0, -1), (0, 5)]
    win_count = 0
    for y in range(18, -1, -1):
        for x in range(18, -1, -1):
            count = 0
            for dy, dx in rank:
                nx = x + dx
                if 0 <= nx < 19:
                    if chess_board[y][nx] == 1:
                        count += 1
                    if chess_board[y][nx] == 2:
                        count -= 1
            for ey, ex in over:
                ox = x + ex
                if 0 <= ox < 19:
                    if chess_board[y][ox] == 1:
                        count += 1
                    if chess_board[y][ox] == 2:
                        count -= 1
            if count == 5:
                win_count += 1
            if count == -5:
                win_count -= 1
    return win_count


def find_stripe(chess_board):
    stripe = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    over = [(0, -1), (0, 5)]
    win_count = 0
    for y in range(18, -1, -1):
        for x in range(18, -1, -1):
            count = 0
            for dy, dx in stripe:
                ny = y + dy
                if 0 <= ny < 19:
                    if chess_board[ny][x] == 1:
                        count += 1
                    if chess_board[ny][x] == 2:
                        count -= 1
            if count == 5:
                win_count += 1
            if count == -5:
                win_count -= 1
    return win_count


def find_right_down(chess_board):
    right_down = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    over = [(0, -1), (0, 5)]
    win_count = 0
    for y in range(18, -1, -1):
        for x in range(18, -1, -1):
            count = 0
            for dy, dx in right_down:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 19 and 0 <= nx < 19:
                    if chess_board[ny][nx] == 1:
                        count += 1
                    if chess_board[ny][nx] == 2:
                        count -= 1
            if count == 5:
                win_count += 1
            if count == -5:
                win_count -= 1
    return win_count


def find_right_up(chess_board):
    right_up = [(0, 0), (-1, 1), (-2, 2), (-3, 3), (-4, 4)]
    over = [(0, -1), (0, 5)]
    win_count = 0
    for y in range(18, -1, -1):
        for x in range(18, -1, -1):
            count = 0
            for dy, dx in right_up:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 19 and 0 <= nx < 19:
                    if chess_board[ny][nx] == 1:
                        count += 1
                    if chess_board[ny][nx] == 2:
                        count -= 1
            if count == 5:
                win_count += 1
            if count == -5:
                win_count -= 1
    return win_count


def who_win(num, row, col):
    if num == 1:
        return f'{1}\n{row+1} {col+1}'
    if num == -1:
        return f'{2}\n{row + 1} {col + 1}'
    return f'{0}'


for tc in range(6):
    board = [list(map(int, input().split())) for _ in range(19)]
    wc = 0
    wc += find_rank(board)
    wc += find_stripe(board)
    wc += find_right_down(board)
    wc += find_right_up(board)
    print(who_win(wc, 0, 0))


# ------------------------------------------------------------------------------------------------------풀이 과정
# 뭔지 모를 똥떵어리
# board = [list(map(int, input().split())) for _ in range(19)]
# judge = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],    # strip
#          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],    # rank
#          [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],  # dia_1
#          [(0, 0), (1, -1), (2, -2), (3, -3), (4, -4)],  # dia_2
#          [(-1, 0), (5, 0)],                             # over_strip
#          [(0, -1), (0, 5)],                             # over_rank
#          [(-1, -1), (5, 5)],                            # over_dia_1
#          [(-1, 1), (5, -5)]]                            # over_dia_2
#
# wwc = 0
# wbc = 0
# for std in range(4):
#     for i in range(18, -1, -1):
#         for j in range(18, -1, -1):
#             wc = 0
#             bc = 0
#             for k in range(5):
#                 ni = i + judge[std][k][0]
#                 nj = j + judge[std][k][1]
#                 if 0 <= ni < 19 and 0 <= nj < 19:
#                     if board[ni][nj] == 1:
#                         wc += 1
#                     if board[ni][nj] == 2:
#                         bc += 1
#             if wc == 5 or bc == 5:
#                 is_ok = True
#                 for k2 in range(2):
#                     ci = i + judge[std+4][k2][0]
#                     cj = j + judge[std+4][k2][1]
#                     if wc == 5 and 0 <= ci < 19 and 0 <= cj < 19 and board[ci][cj] == 1:
#                         is_ok = False
#                     if bc == 5 and 0 <= ci < 19 and 0 <= cj < 19 and board[ci][cj] == 2:
#                         is_ok = False
#
#                 wy, wx = 0, 0
#                 if is_ok:
#                     if wc == 5:
#                         wwc += 1
#                         wy, wx = i+1, j+1
#                     if bc == 5:
#                         wbc += 1
#                         wy, wx = i+1, j+1
#
#
# if wwc == 0 and wbc == 1:
#     print(2, '\n', wy, ' ', wx, sep='')
# elif wwc == 1 and wbc == 0:
#     print(1, '\n', wy, ' ', wx, sep='')
# else:
#     print(0)