# 11724번 연결 요소의 개수
'''
방향 없는 그래프가 주어졌을 때, 
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N x (N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
같은 간선은 한 번만 주어진다.

[입력]
6 5
1 2
2 5
5 1
3 4
4 6

[출력]
2
'''

'''
DFS로 진행
처음에 시간초과나서 생각해보니까 그냥 M값이 매우매우 커질 수도 있으므로 input을 바꿔줌
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [[] for _ in range(N + 1)]    
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
visited = [0 for _ in range(N + 1)]

def BFS(y):
    global cnt
    stack = []
    visited[y] = 1
    while True:
        for i in arr[y]:
            if visited[i] == 0:
                stack.append(y)
                y = i
                visited[y] = 1
                break
        else:
            if stack:
                y = stack.pop()
            else:
                cnt += 1
                break
    
for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)

print(cnt)
            
