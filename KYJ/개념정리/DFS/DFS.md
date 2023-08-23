# DFS(깊이우선탐색)
:한 방향으로 계속 가다가 더 이상 갈 곳이 없다면, 가장 마지막에 본 갈림길에서 다른길로 가서 탐색을 하는 방법
- 빠짐없이, 중복없이 하는 것이 목표
- Depth First: 넓게 탐색하기 보단 하나를 깊게 탐색하는 것을 먼저 하는 것
- 주로 `스택`을 이용하나, 스택을 이용한다고 무조건 DFS는 아님을 주의
  
## DFS의 과정

![사진](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

#### 구현
- 시작하기 전에, 현재의 위치를 담을 비어있는 스택과 검색을 했는지 확인할 visited 리스트를 만들어 준다.

1. 시작 정점 v를 결정하여 방문한다
2. 정점 v에 인접한 정점 중에서
    - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문하고 w를 v로 해서 다시 반복
    - 방문하지 않은 정점이 없다면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여받은 가장 마지막 방문 정점을 v로해서 반복
3. 스택이 공백이 될 때까지 반복한다.


```python
visited[], stack[] 초기화
DFS(v)
    시작점 v 방문
    visited[v] ← true
    while{
        if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v)
            v ← w (w에 방문)
            visited[w] ← true
        else
            if (스택이 비어 있지 않으면)
                v ← pop(stack)
            else
                break
    }
end DFS()
```


```python
# V E = 7 8   # 총개수, 간선개수?
# v1 w1 v2 w2 .... = 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# v1, w1, v2, ... 를 저장하는 방법: (인장행렬 / 인접리스트)의 방법을 이용함

V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split())) # 우선 정리하기전에 리스트로 받아줌
adj_m = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1


def dfs(n, V, adj_m): # n번까지 탐색을 해봐
    # stack 생성
    stack = []
    # visited 생성
    visited = [0] * (V + 1)
    # 시작점 방문 표시
    visited[n] = 1
    # do[n] 
    print(n)
    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        for w in range(1, V):
            if adj_m[n][w] ==1 and visited[w] == 0: # n과 w가 인접하고, 방문하지 않았다면
                # push(v)
                stack.append(n) # 들린거 stack에 넣어주고,
                n = w           # 다음은 이제 w가 되고, 
                # do(w)
                print(n)        # 할일하고
                # w 방문표시
                visited[n] = 1  # 방문한거 체크해줘
                break           # 찾았으니까 break
        else: # 근데 다 돌았는데 안보였으면 뒷걸음
            if stack: # 스택에 지나온 정점이 남아있으면
                n = stack.pop() #pop()해서 다시 다른 w를 찾을 n 찾기
            else:   # 스택이 비어있으면
                break   # While True에 대한 break

dfs(1, V, adj_m)
```