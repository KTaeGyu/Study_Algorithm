# 13549번 숨바꼭질 3
# 다잌스트라
'''
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 
구하는 프로그램을 작성하시오.

[입력]
5 17

[출력]
2
'''
'''
순간이동이면 0초임!!!!
'''
import heapq

N, K = map(int, input().split())
times = [float('INF') for _ in range(100001)]  # 최단 시간 table

def game(start):
    times[start] = 0    # 시작점은 시간 0
    pq = []
    heapq.heappush(pq, (0, start))  # 최소힙에 (시간, 좌표)순으로 넣어준다
    
    while pq:
        time, now = heapq.heappop(pq)   # 가장 최소값이 나올것
        
        # 만약 꺼낸 시간이 저장된 시간보다 크다면 pass
        if time > times[now]:
            continue
        
        # 다음에 갈 수 있는 후보자리
        hubo = [now * 2, now + 1, now - 1]
        for i in range(3):
            next = hubo[i]
            if 0 <= next < 100001:
                if i:   # +1, -1일 때
                    next_time = time + 1
                else:   # *2일때
                    next_time = time
                # 저장되어있는 시간보다 계산한 시간이 더 짧다면
                if times[next] > next_time: # 업데이트해주고, 다음 힙에 저장
                    times[next] =next_time
                    heapq.heappush(pq, (next_time, next))
    return times[K]

print(game(N))






'''
https://velog.io/@zirryo/Algorithm-%EB%8D%B0%EC%9D%B4%ED%81%AC%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
'''