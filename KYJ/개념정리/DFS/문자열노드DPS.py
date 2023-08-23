# 문자열 노드
# 8개의 알파벳으로 구성된 문자열과 대응되는 인접행렬을 입력받음
# 0번 알파벳에서 부터 DFS로 노드들을 탐색하면서 출력해주세요

strs = input()
adj_m = []
for _ in range(8):
    mat = list(map(int, input().split()))
    adj_m.append(mat)
result = []
def dfs(n,adj_m): # 시작점(0), 개수(8), 인접행렬 
    stack = []
    visited = [0] * 8
    visited[n] = 1
    result.append(strs[n])
    while True:
        for m in range(8):
            if adj_m[n][m] == 1 and visited[m] == 0:
                stack.append(n)
                n = m
                result.append(strs[n])
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    
dfs(0, adj_m)
for k in result:
    print(k, end='')
    

'''
input:
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0 
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0


output:
RKBIFCCM
'''