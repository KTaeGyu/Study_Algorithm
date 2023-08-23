# 그래프 경로

T =  int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = []
    for _ in range(E):
        a1, a2 = map(int,input().split())
        arr.append(a1)
        arr.append(a2)
    S, G = map(int, input().split())
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]
    
    for i in range(E): # 방향을 고려해주기 위해서 
        v1, v2 = arr[2 * i], arr[2 * i + 1]
        adj_m[v1][v2] += 1 # 양방향 아니라 이거 하나만 추가
    

    def dfs(n, V, adj_m): # n은 시작점, V는 총 몇개인지
        stack = []
        visited = [0] * (V + 1)
        visited[n] = 1  # 1부터 시작
        mylst = [] # 어디어디 들리는지 확인용 리스트
        
        # 탐색 시작
        while True:
            for w in range(1, V + 1):
                if adj_m[n][w] == 1 and visited[w] == 0:
                    stack.append(n)
                    n = w
                    mylst.append(n) # 여기 들렸다고 넣어주기
                    visited[n] = 1
                    break
            else:
                if stack:
                    n = stack.pop()
                else:
                    break
        
        return mylst
    
    visited_list = dfs(S,V,adj_m)
    if G in visited_list:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')
