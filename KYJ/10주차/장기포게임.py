'''
아마도 BFS...
BFS에서 경로처리를 어케하는지 몰루겟다

'''

from collections import deque

# 현재의 지점을 주면 갈 수 있는 좌표를 반환하는 함수
def move(starty, startx, path):    # path는 지금까지 먹은 애들 좌표(비어있게 처리하기 위해서)       
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    temp = [0 for _ in range(4)]    # 모든방향에 대해 1만나면 멈춰야하므로
    ok = [] # 가능한 리스트
    for k in range(4):
        for i in range(1, N):
            ny = starty + i * dir[k][0] # 계속 늘려서 확인
            nx = startx + i * dir[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if '/'+str(ny)+','+str(nx)+'/' in path:  # 만약에 먹었던 거면
                    pan[ny][nx] = 0            # 0인걸로 처리
                    # print(f'경로는 {path}')
                    # print(f'여기를 0처리 했어요{ny}, {nx}')
                if not temp[k] and pan[ny][nx] == 1:    # 처음으로 만나는 말
                    temp[k] = 1
                elif temp[k] == 1:
                    ok.append((ny, nx))
                    if pan[ny][nx] == 1:
                        break
                if str(ny)+','+str(nx) in path:    # 아까 0바꿔준거 원상복귀
                    pan[ny][nx] = 0
                    # print(f'여기를 원상복구 했어요{ny}, {nx}')
    return ok


def game(starty, startx):
    que = deque([(starty, startx, 0, '/')])  # 위치, 시도한 횟수, 지금까지 먹은 애들, 이동한 경로
    cnt = 0
    numnum = []
    while que:
        cy, cx, level, path= que.popleft()
        if level == 3:
            return cnt
        else:
            able = move(cy, cx, path)
            # print(f'({cy},{cx})일때 가능한 좌표들 {able}, 지금까지의 cnt: {cnt}')
            for ny, nx in able:
                if pan[ny][nx] == 1 and (ny, nx) not in numnum:
                    cnt += 1
                    numnum.append((ny,nx))
                    que.append((ny, nx, level + 1, path +str(ny)+','+str(nx)+'/'))
                    # print(f'{ny},{nx}에 있는거 먹었어요 현재 레벨 {level}')
                else:
                    que.append((ny, nx, level + 1, path))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 2:
                poy = i
                pox = j
                pan[i][j] = 0

    print(f'#{tc} {game(poy,pox)}')




# answer code

def search(dx, dy, lst, n):
    global cnt
    if n == 3:
        return
    else:
        for k in range(4):
            flag = 0
            for l in range(1, N):
                nx = dx + d[k][0] * l
                ny = dy + d[k][1] * l
                if flag > 1:
                    break
                if 0 <= nx < N and 0 <= ny < N:
                    if lst[nx][ny] == 1:
                        if flag == 1 and v[nx][ny] == 0:
                            cnt += 1
                            v[nx][ny] = 1
                            lst[nx][ny] = 0
                            search(nx, ny, lst, n+1)
                            lst[nx][ny] = 1
                        elif flag == 1 and v[nx][ny] == 1:
                            lst[nx][ny] = 0
                            search(nx, ny, lst, n + 1)
                            lst[nx][ny] = 1
                        flag += 1
                    if lst[nx][ny] == 0 and flag == 1:
                        search(nx, ny, lst, n+1)


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for t in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                x, y = i, j

    MAP[x][y] = 0
    v = [[0] * N for _ in range(N)]
    cnt = 0
    search(x, y, MAP, 0)
    print(f'#{t+1}', cnt)