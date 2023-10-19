# 녹색 옷 입은 애가 젤다지?
'''
왼쪽 끝에서 오른쪽 아래까지 갈때
잃는 금액의 최소값 구하기

다잌스트라

https://memezz.tistory.com/48

'''
import heapq

dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def gangdo():
    pq = []
    heapq.heappush(pq,(MAP[0][0], 0, 0))
    while pq:
        # lose는 지금까지 잃은 돈
        lose, cy, cx = heapq.heappop(pq)
        
        if lose > coin[cy][cx]:
            continue

        for dy, dx in dire:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                nextlose = lose + MAP[ny][nx]
                if coin[ny][nx] > nextlose:
                    coin[ny][nx] = nextlose
                    heapq.heappush(pq,(nextlose, ny, nx))

tc = 0
while True:
    tc += 1
    N = int(input())
    # N이 0이 되면 프로그램 종료
    if not N:
        exit()
    MAP = [list(map(int,input().split())) for _ in range(N)]
    
    # 각 위치에서 잃는 최소한의 coin
    coin = [[float('inf') for _ in range(N)] for _ in range(N)]
    gangdo()
    print(f'Problem {tc}: {coin[N-1][N-1]}')
