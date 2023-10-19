# SWEA A형 대비: 벽돌 깨기
'''
맨 위에 있는 벽돌만 깨트릴 수 있고
벽돌에 있는 숫자 - 1 만큼 상하좌우로 깨진다
깨지면서 그 벽돌도 터진다...
벽돌이 깨지면, 위에 있는 애들은 밑으로 떨어진다.
N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다
남은 벽돌의 개수를 구하세요
1 <= N <= 4

N이 어짜피 작으니까..


# 필요한 함수
1. boomx번째에 떨어트렸을 때, 터지는 구슬과, MAP이 어떻게 변하는지 바꿔주는 함수
2. 순열 만들기
'''
import copy

dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 어디에 떨어트릴지 구하면 찾아주기
def boom(boomx):
    global is_true
    for i in range(H):
        # 위에서부터 처음으로 나오는 숫자 찾기
        if MAP[i][boomx] != 0:
            size = MAP[i][boomx]
            boomy = i   # 폭탄은 (boomy, boomx)에서 터짐
            break
    else:
        boomy = 0
        size = 0
    pang(boomy, boomx, size)
    # MAP 정렬
    if count(MAP) == 0:
        is_true = False
        return 
    
    for j in range(W):
        cnt = 0
        while cnt < H - 1:
            cnt = 0
            for i in range(H - 1, 0, -1):  # 아래에서부터
                # 아래는 0인데 위는 아니라면 바꿔주기
                if MAP[i][j] == 0 and MAP[i - 1][j] != 0:
                    MAP[i][j], MAP[i - 1][j] = MAP[i - 1][j], MAP[i][j]
                else:
                    cnt += 1




# 폭탄을 실질적으로 터트리는 함수
def pang(starty, startx, size):
    # 해당위치는 우선 터트려 주고
    MAP[starty][startx] = 0
    # 추가적으로 터질 부분
    addtional = []
    for k in range(1, size):
        for dy, dx in dire:
            # ny와 nx는 없어질 부분
            ny, nx = starty + k*dy, startx + k*dx
            # 터질 부분이 0이나 1이 아니라면
            if 0 <= ny < H and 0 <= nx < W:
                if MAP[ny][nx] != 0 or MAP[ny][nx] != 1:
                    addtional.append((ny,nx, MAP[ny][nx]))
                MAP[ny][nx] = 0
    # 만약 추가로 터질게 남앗다면
    if count(MAP) == 0:
        return 
    
    if addtional:
        for y, x, newsize in addtional:
            pang(y, x, newsize)
    else:
        return

# 지도에서 벽돌 갯수 찾기
def count(field):
    cnt = 0 
    for i in range(H):
        for j in range(W):
            if field[i][j] != 0:
                cnt += 1
    return cnt


# 가능한 조합 찾기
def combi(N, W, lst):
    if len(lst) == N:
        a = copy.deepcopy(lst)
        combi_lst.append(a)
        return
    for i in range(W):
        lst.append(i)
        combi(N, W, lst)
        lst.pop()

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int,input().split())
    original_MAP = [list(map(int,input().split())) for _ in range(H)]
    combi_lst = []
    combi(N, W, [])
    minval = float('inf')
    for lst in combi_lst:
        is_true = True
        MAP = copy.deepcopy(original_MAP)
        for i in lst:
            if is_true:
                boom(i)
        val = count(MAP)
        if val == 0:
            minval = 0
            break
        if val < minval:
            minval = val

    print(f'#{tc} {minval}')
