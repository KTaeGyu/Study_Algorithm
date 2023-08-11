"""
예선전에서 승리한 삼성이는 결승전 까지 진출하게 되었다.
결승전인 만큼 수영장이 아닌 바다에서 진행되었다.
바다 전체를 사용 할 수 없기에 가로 N 세로 N만큼의 공간만 사용하여 진행하도록 하였다.
이 공간을 벗어나면 실격처리가 되므로 공간안에서 가장 빠른 길을 찾아야 한다.
이 공간에는 섬과 같은 지나갈 수 없는 장애물과, 주기적으로 사라졌다 나타나는 소용돌이 같은 장애물이 존재한다.
( 섬과 같은 장애물은 지도에서 1로 표시, 소용돌이 같은 장애물은 2로 표시 )
소용돌이는 생성되고 2초동안 유지되다가 1초동안 잠잠해진다.
예를들어, 0초에 생성된 소용돌이는 0초, 1초까지 유지되고 2초에 사라지게된다. 또한 3초, 4초에는 생성되고 5초에 사라진다.
(단 ,한번 통과한 소용돌이 위에서는 머물러 있을 수 있다 )
이런 바다에서 삼성이를 우승시키려면 어떤 경로로 보내야 될까?
똑똑한 여러분들은 한번에 그 경로를 찾을 수 있었다. 해당 경로로 수영을 했을때 삼성이는 몇초만에 골인 할 수 있을까?
 
5
0 0 0 0 0
0 0 0 1 0
0 0 0 1 0
2 2 1 1 0
0 0 0 0 0
4 0
2 0

EX) 
이 경우에는 (4,0) 에서 시작, 소용돌이가 존재하므로 이동하지 않는다 ( 0초 )
                (4,0) 아직 소용돌이가 사라지지 않았으므로 제자리에 있다 ( 1초)
                (4,0) 이제 소용돌이가 사라지는 것을 보았고 건너려고한다 ( 2초)
                (3,0) 소용돌이를 통과하였고 바다위를 수영하고 있다 (3초)
                (2,0) 도착지에 도착하였다 (4초)

입력 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 수영장의 크기 N  ( 2<=N<=15 )
다음 N개의 줄의 i번째 줄에는 수영장의 모양이 공백으로 구분되어 주어진다. ( 0 : 지나갈 수 있는 곳 , 1 : 장애물 , 2: 주기가 2초인 소용돌이)
다음으로 시작위치 A,B가 주어지고 ( 0<=A,B<=N-1)
마지막 줄에 도착위치 C, D가 주어진다 ( 0 <=C,D<=N-1) ( 도착점과 시작점은 소용돌이가 아니다 )

출력
각 테스트 케이스마다 테스트 케이스의 번호와 이동시간을 공백을 두고 표시한다 
도착 할 수 없다면 -1을 출력한다.

(Ex) #1 4
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(graph, s, e):
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    visited = [[[False]*3 for _ in range(N)] for _ in range(N)]

    queue = [(s[0], s[1], 0, 0)]

    while queue:
        y, x, time, timing = queue.pop(0)

        if (y, x) == end:
            return time
        
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx][(timing + 1) % 3]:
                visited[ny][nx][(timing + 1) % 3] = True
                
                if graph[ny][nx] == 1:
                    continue
                elif graph[ny][nx] == 2:
                    if (timing % 3) == 2:
                        queue.append((ny, nx, time + 1, (timing + 1) % 3))
                        graph[ny][nx] = 0
                    else:
                        queue.insert(0, (y, x, time + 1, (timing + 1) % 3))
                        visited[ny][nx][(timing + 1) % 3] = False
                elif graph[ny][nx] == 0:
                    queue.append((ny, nx, time + 1, (timing + 1) % 3))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pool = [list(map(int, input().split())) for _ in range(N)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    result = bfs(pool, start, end)
    print(f'#{tc} {result}')
"""
3
5
0 0 0 0 0
0 0 0 1 0
0 0 0 1 0
2 2 1 1 0
0 0 0 0 0
4 0
2 0
6
0 0 0 0 0 0
0 1 1 0 0 0
0 0 0 1 2 0
1 1 0 1 0 1
0 0 0 1 0 1
0 0 0 2 0 1
5 0
2 5
6
0 0 0 0 0 0
0 0 0 0 0 0
1 0 1 1 1 0
1 0 0 0 0 0
1 0 1 1 1 0
0 0 2 0 2 0
5 0
3 5

#1 4
#2 10
#3 7
"""