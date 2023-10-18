# 백준 1326 폴짝폴짝

from collections import deque

def polzzak(start, end):    # start와 end는 인덱스, 예제에서는 0, 4
    d = end - start     # 출발지와 목적지 사이의 거리
    startvalue = stone[start]
    visited = [0 for _ in range(10001)]
    visited[start] = 1

    # 만약 시작점에서 바로 갈 수 있다면 바로 리턴
    if d % startvalue == 0:
        return 1
    
    que = deque([(start, 1)])   # 현재의 인덱스, 레벨
    while que:
        nowidx, level = que.popleft()
        # print(stone[nowidx], level)
        nowvalue = stone[nowidx]
        # 현재 위치와 도착지 사이의 거리
        now_d = end - nowidx
        if now_d % nowvalue == 0:
            return level
        
        # 다음으로 갈 수 있는 곳
        nextdol = []
        k = nowidx
        while k <= 10000 - nowvalue:
            k += nowvalue
            nextdol.append(k)

        l = nowidx
        while 0 <= l:
            l -= nowvalue
            nextdol.append(l)


        for nextidx in nextdol:
            if 0 <= nextidx < len(stone) and visited[nextidx] == 0:
                visited[nextidx] = 1
                que.append((nextidx, level + 1))
    return -1



N = int(input())
stone = list(map(int,input().split()))
a, b = map(int,input().split())
print(polzzak(a - 1, b - 1))
