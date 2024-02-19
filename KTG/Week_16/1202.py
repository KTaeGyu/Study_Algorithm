import sys
sys.stdin = open('../test.txt', 'r')
import heapq

N, K = map(int, input().split())
jewels = []
for n in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewels, [M, V])
bags = []
for k in range(K):
    C = int(input())
    bags.append(C)
bags.sort()

total_value = 0
possible = []
# 가벼운 가방부터 처리
for bag in bags:
    # 현재 가방에 담을 수 있는 보석을 모두 힙에 추가
    while jewels and bag >= jewels[0][0]:
        jewel = -heapq.heappop(jewels)[1]
        heapq.heappush(possible, jewel)
    # 가장 가치가 높은 보석 선택
    if possible:
        jewel = heapq.heappop(possible)
        total_value += -jewel
    # 담을 수 있는 보석도 없고, 남은 보석도 없다면 중지
    elif not jewels:
        break

print(total_value)

