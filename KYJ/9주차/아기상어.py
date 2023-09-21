# 백준 16236번 아기상어

'''
아기상어 초기 크기: 2
1초에 상하좌우 한칸씩
자기보다 작은 물고기만 먹을 수 있다.
크기가 같은 물고기는 못 먹지만, 지나갈 수는 있다.

더이상 먹을 수 있는 게 없으면 엄마를 불러요
1마리면 먹으러가요
먹을 수 있는 물고기가 1마리보다 많으면 가장 가까운걸 먹으러가요(= BFS)
거리가 가까운게 여러개라면 가장 위에, 가장 왼쪽에 있는걸 먹으러간다
(상-좌-우-하 순서)
상어는 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1증가한다

9 = 상어의 위치
물고기를 잡아먹을 수 있는 시간을 출력

[tc 1]
3
0 0 0
0 0 0
0 9 0

0

[tc 2]
3
0 0 1
0 0 0
0 9 0

3

print(f'좌표({cy}, {cx}), t = {t}, 상어크기 = {sharksize}, 물고기={fish} 누적시간 ={time}')
'''


from collections import deque

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]    # 상 좌 우 하
N = int(input())
ocean = [list(map(int,input().split())) for _ in range(N)]

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            sharky = i
            sharkx = j
sharksize = 2
fish = 0    
time = 0    # 총시간
ocean[sharky][sharkx] = 0   # 초기 위치도 움직일 수 있으니까 0만들어주기

def eat(y, x, t):  # 시작점, 시간
    global sharksize, fish, time
    que = deque([(y, x, t)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 1
    eatable = []
    while que:
        cy, cx, t = que.popleft()
        if 0 < ocean[cy][cx] < sharksize:
            eatable.append((t, cy, cx)) # 먹을 수 있는 물고기 리스트에 넣어주기
        for dy, dx in dir:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0 and ocean[ny][nx] <= sharksize:
                    visited[ny][nx] = 1
                    que.append((ny, nx, t + 1))
    distance = 99999    # 가장 가까운 물고기 구해주기
    if eatable:
        for dis, ay, ax in eatable:
            if dis < distance:
                nesty, nextx = ay, ax
                distance = dis
            elif dis == distance:
                if nesty > ay:
                    nesty, nextx = ay, ax
                    distance = dis
                elif nesty == ay:
                    if nextx > ax:
                        nesty, nextx = ay, ax
                        distance = dis
        fish += 1   # 물고기 먹어주고
        if fish == sharksize:   # 만약 먹은 물고기 == 상어 크기라면
            sharksize += 1      # 상어 크키 늘려주고
            fish = 0            # 물고기 초기화
        ocean[nesty][nextx] = 0 # 자리에 있는거 먹었으니까 자리는 비었음
        time += distance
        eat(nesty, nextx, 0)
    else:   # 먹을게 없다면 종료
        return 0  

eat(sharky, sharkx, 0)
print(time)


'''
물고기 우선순위 찾는게 힘들엇따..
그냥 먹을 수 있는 물고기를 리스트에 담고
가장 가까운거 -> 같으면 위에 있는거 -> 같으면 왼쪽에 있는거 if문으로 정해서 다시 돌리기
'''



# from collections import deque
# import pprint

# dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]    # 상 좌 우 하
# N = int(input())
# ocean = [list(map(int,input().split())) for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if ocean[i][j] == 9:
#             sharky = i
#             sharkx = j
# sharksize = 2
# fish = 0
# time = 0
# ocean[sharky][sharkx] = 0

# def eat(y, x, t):  # 시작점, 시간
#     global sharksize, fish, time
#     que = deque([(y, x, t)])
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     visited[y][x] = 1
#     while que:
#         cy, cx, t = que.popleft()
#         print(f'좌표({cy}, {cx}), t = {t}, 상어크기 = {sharksize}, 물고기={fish} 누적시간 ={time}')
#         if 0 < ocean[cy][cx] < sharksize:
#             fish += 1
#             if fish == sharksize:
#                 fish = 0
#                 sharksize += 1
#             time += t
#             ocean[cy][cx] = 0
#             left = 0
#             pprint.pprint(ocean)
#             for i in range(N):
#                 left += sum(ocean[i])
#             if left == 0:
#                 return time
#             else:
#                 return eat(cy, cx, 0)
#         for dy, dx in dir:
#             ny = cy + dy
#             nx = cx + dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if visited[ny][nx] == 0 and ocean[ny][nx] <= sharksize:
#                     visited[ny][nx] = 1
#                     que.append((ny, nx, t + 1))
    
# eat(sharky, sharkx, 0)
# print(time)
# print(ocean)