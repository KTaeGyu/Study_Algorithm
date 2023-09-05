"""
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
"""
import sys
from pprint import pprint
sys.stdin = open("../test.txt", "r")

N = int(input())
graph = {}
for i in range(1, N+1):
    graph[i] = []
print(graph)
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

"""
7
1 6
6 3
3 5
4 1
2 4
4 7

4
6
1
3
1
4
"""