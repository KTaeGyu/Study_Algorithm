import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    k = int(input())

    max_heap, min_heap = [], []
    visited = [False] * 1000001

    for i in range(k):
        operator, num = input().split()
        num = int(num)
        if operator == 'I':
            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))
            visited[i] = True

        elif operator == 'D':
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')