# A형 기출: 지역구 나누기
'''
나눠진 지역구를 관리할 대표는 투표를 통해 선정하려고 한다. 
단, 지역 대표 선출의 형평성을 위해, 
A와 B 지역구에 포함된 유권자의 수 차이가 최소가 되도록 지역을 분리하려고 한다.

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. 
그리고 다음 줄 부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 마을의 개수 N이 주어진다.
다음 N개의 줄에는 마을의 연결 정보인 Rrc가 주어진다. 
(Rrc는 r번째 행과 c번째 열의 값을 의미한다.)
각 테스트 케이스의 마지막 줄에는 i번째 마을의 유권자의 수 Pi가 순서대로 주어진다.

유권자수의 차이를 구하세요

[입력]
2
4
0 0 1 0
0 0 1 0
1 1 0 1
0 0 1 0
6 7 4 8 
5
0 1 0 1 0
1 0 1 1 1
0 1 0 0 0
1 1 0 0 1
0 1 0 1 0
10 10 3 10 7

[출력]
#1 9
#2 0
'''


from collections import deque
from itertools import combinations

# 마을 종류를 lst에 담아서 주면, 이 lst안의 마을들이 연결되었는지 체크하는 함수
# 근데 여기서 마을 종류는 인덱스임(-1씩 해줘야함~!!!!)
def check(lst):
    q = deque([lst[0]])
    checklst = []
    while q:
        village = q.popleft()
        checklst.append(village)
        for i in range(N):
            if adj[village][i] == 1 and i in lst and i not in checklst:
                q.append(i)
    if len(checklst) == len(lst):
        return True
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 마을 갯수
    adj = [list(map(int,input().split())) for _ in range(N)]    # 인접행렬
    P = list(map(int,input().split()))  # P의 i번째항 = i번 마을의 유권자 수

    combi = []
    minval = float('inf')
    lst = [i for i in range(N)]
    # 마을 조합을 만들어서 연결되어 있는지 체크
    for i in range(1, N // 2 + 1):
        for k in combinations(lst, i):
            A = list(k)
            B = []
            for num in lst:
                if num not in A:
                    B.append(num)
            # 만약 둘 다 연결되어 있다면, 각각 값 비교
            if check(A) and check(B):
                aval, bval = 0, 0
                for a in A:
                    aval += P[a]
                for b in B:
                    bval += P[b]
                val = abs(aval - bval)
                if val < minval:
                    minval = val
    print(f'#{tc} {minval}')