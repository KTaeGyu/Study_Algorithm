import sys
sys.stdin = open("../test.txt", "r")

R, C, N = map(int, input().split())
initial_State = list(list(input()) for _ in range(R))


def solve(board):
    bombs = []
    for y in range(R):
        for x in range(C):
            if board[y][x] == '.':
                continue
            bombs.append((y, x))

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    new_board = list(['O'] * C for _ in range(R))
    for y, x in bombs:
        new_board[y][x] = '.'
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 > ny or ny >= R or 0 > nx or nx >= C:
                continue
            new_board[ny][nx] = '.'

    return new_board


board1 = solve(initial_State)
board2 = solve(board1)

if N == 1:
    for i in range(R):
        print(*initial_State[i], sep='')
elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)
elif N % 4 == 3:
    for i in range(R):
        print(*board1[i], sep='')
elif N % 4 == 1:
    for i in range(R):
        print(*board2[i], sep='')
