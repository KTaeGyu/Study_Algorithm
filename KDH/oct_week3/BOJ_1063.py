#BOJ_1063 킹

# 문제
# 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 
# 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 
# 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 
# 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

# 킹은 다음과 같이 움직일 수 있다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 

# 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 
# 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

    
def move_R(start):
    if start[0] < 72:
        start[0] += 1
def move_L(start):
        if start[0] > 65:
            start[0] -= 1
def move_B(start):
        if start[1] > 1:
            start[1] -= 1
def move_T(start):
        if start[1] < 8:
            start[1] += 1        
def move_RT(start):
        if start[0] <72 and start[1] <8:
            start[0] += 1
            start[1] += 1
def move_LT(start):
        if start[0] > 65 and start[1] <8:
                start[0] -= 1
                start[1] += 1
def move_RB(start):
        if start[0] < 72 and start[1] >1:
            start[0] += 1
            start[1] -= 1
def move_LB(start):
        if start[0] > 65 and start[1] > 1:
            start[0] -= 1
            start[1] -= 1

K, S, N = input().split()
N = int(N)
K = list(K)


K_start = [ord(K[0]),int(K[1])]
S_start = [ord(S[0]),int(S[1])]

for _ in range(N):
    M = input()
    if M == 'R':
        move_R(K_start)
        if K_start == S_start:
            if S_start[0] == 72:
                K_start[0] -= 1
            else:
                move_R(S_start)

    elif M == 'L':
        move_L(K_start)
        if K_start == S_start:
            if S_start[0] == 65:
                K_start[0] += 1
            else:
                move_L(S_start)
    elif M == 'B':
        move_B(K_start)
        if K_start == S_start:
            if S_start[1] == 1:
                K_start[1] += 1
            else:
                move_B(S_start) 
    elif M == 'T':
        move_T(K_start)
        if K_start == S_start:
            if S_start[1] == 8:
                K_start[1] -= 1
            else:
                move_T(S_start)
    elif M == 'RT':
        move_RT(K_start)
        if K_start == S_start:
            if S_start[0] == 72 or S_start[1] == 8:
                K_start[0] -= 1
                K_start[1] -= 1
            else:
                move_RT(S_start)
    elif M == 'LT':
        move_LT(K_start)
        if K_start == S_start:
            if S_start[0] == 65 or S_start[1] == 8:
                K_start[0] += 1
                K_start[1] -= 1
            else:
                move_LT(S_start)
    elif M == 'RB':
        move_RB(K_start)
        if K_start == S_start:
            if S_start[0] == 72 or S_start[1] == 1:
                K_start[0] -= 1
                K_start[1] += 1
            else:
                move_RB(S_start)
    elif M == 'LB':
        move_LB(K_start)
        if K_start == S_start:
            if S_start[0] == 65 or S_start[1] == 1:
                K_start[0] += 1
                K_start[1] += 1
            else:
                move_LB(S_start)

x1 = chr(K_start[0])
x2 = chr(S_start[0])
y1 = K_start[1]
y2 = S_start[1]
print(f'{x1}{y1}')
print(f'{x2}{y2}')
          
        
