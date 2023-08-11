# ----------------------------------------------------------------------------------------------------------문제
# 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
# 이러한 촌수는 다음과 같은 방식으로 계산된다. 
# 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
# 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
# ----------------------------------------------------------------------------------------------------------입력
# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
# 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
# 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

# 각 사람의 부모는 최대 한 명만 주어진다.

# ----------------------------------------------------------------------------------------------------------출력
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 
# 이때에는 -1을 출력해야 한다.

# 3
# ----------------------------------------------------------------------------------------------------------풀이
import sys
from pprint import pprint
from collections import deque
sys.stdin = open("test.txt", "r")

# 입력
n = int(input())
s_people, e_people = map(int, input().split())
m = int(input())
family_relation = {}
for i in range(1, n+1):
    family_relation[i] = []
for i in range(m):
    x, y = map(int, input().split())
    family_relation[x].append(y)
    family_relation[y].append(x)


def bfs(nodes, start, end):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        node, cnt = queue.popleft()
        if node == end:
            return cnt
        if node not in visited:
            visited.add(node)
            for i in nodes[node]:
                queue.append((i, cnt + 1))
    return -1
        

print(bfs(family_relation, s_people, e_people))


# ------------------------------------------------------------------------------------------------ -예제 입, 출력
"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

3
"""

# --------------------------------------------------------------------------------------------------알고리즘 분류
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색

# ------------------------------------------------------------------------------------------------------풀이 과정
# # Try 1 : 깊이 탐색을 시도했다가 촌수 더하고 빼는 방법이 생각 안나서 BFS로 변경
# # Try 2 : 넓이 탐색을 시도. 카운트의 위치를 잘못 잡아서 2촌부터 오류남.
# import sys
# from pprint import pprint
# from collections import deque
# sys.stdin = open("test.txt", "r")


# def bfs(nodes, start, end):
#     queue = deque([start])
#     visited = set()
#     cnt = 0

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.add(node)
#             cnt += 1
#             for i in nodes[node]:
#                 if i == end:
#                     return cnt
#                 if i not in visited:
#                     queue.append(i)
#     return -1


# # 입력
# n = int(input())
# s_people, e_people = map(int, input().split())
# m = int(input())
# family_relation = {}
# for i in range(1, n+1):
#     family_relation[i] = []
# for i in range(m):
#     x, y = map(int, input().split())
#     family_relation[x].append(y)
#     family_relation[y].append(x)

# # 출력
# print(dfs(family_relation, s_people, e_people))

# # Try 3 : 넓이 탐색을 시도. 카운트의 위치를 큐 내부에 위치시켜서 현재 큐의 촌수에 1을 더하는 식으로 변경