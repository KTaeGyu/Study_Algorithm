"""
코코는 한 회사의 팀의 에이스이다. 코코의 팀에연말에 급하게 완료해야 하는 업무들이 부여되었다.
업무들은 단순해서 다른 부서에서 일하고 있는 직원들을 지원 받아 완료시키려 한다.

각각의 업무들은 업무 번호를 가지고 있으며 업무를 완료하는데 걸리는 소요 시간이 정해져 있다.
업무번호는 1부터 시작하여 1씩 증가하면서 부여된다.

업무는 독립적으로 진행이 가능한 경우도 있고 다른 업무들이 완료되어야 진행할 수 있는 업무들도 있다.
한 명의 직원은 하나의 업무를 맡게 되며 이 업무가 완료되기 전까지는 다른 업무를 맡을 수 없다.
따라서 업무를 최대한 빨리 완료시키기 위해서는  가능한 많은 수의 직원들을 투입하여야 한다.
급한 업무임으로 투입되는 직원들의 비용은 고려하지 않는다.

빠른 진행을 위해 코코는 단 하나의 업무를 도와줄 수 있다.
코코의 실력은 출중하기에, 코코가 도와주는 업무의 소요시간은 반으로 줄어든다.

업무를 완료하는데 필요한 소요시간과 업무를 시작하기 위해 미리 완료해야 하는 업무 목록이 주어졌을 때 코코와 직원들이 투입되어  전체 업무를 완료시키기 위해 필요한 최소 소요시간을 구하는 프로그램을 작성하여라.
완료해야 하는 업무들 중의 일부가 순환 관계를 가져 모든 업무를 완료할 수 없게 되는 경우 -1을 출력하면 된다.

[제약 사항]
1. 주어지는 업무의 개수 N은 1개 이상 50개 이하이다.(1 ≤ N ≤ 50)
2. 업무 번호는 1부터 N까지의 숫자로 나타내며, 중복되는 경우는 없다.
3. 업무별 소요시간은 2이상 1,000 이하의 정수로 주어진다.
4. 업무별 미리 완료해야 하는 업무의 개수 M은 0개 이상 N-1개 이하이다. (0 ≤ M ≤ N-1)
5. 투입할 수 있는 직원의 수는 제한이 없으며, 비용도 무시한다.
6. 한 명의 직원이 한번에 하나의 업무 만을 맡을 수 있으며, 업무가 끝나기 전에는 다른 업무를 맡을 수 없다.
7. 코코는 단 하나의 업무만 도와줄 수 있으며, 이 때 도와주는 업무의 소요시간은 반으로 줄어든다.
8. 소요 시간이 홀수인 경우 반으로 줄어들 때 소수점 이하는 제외된다. (예 : 소요시간 25 à 반으로 줄어들면 12)

입력
입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터는 각 테스트 케이스가 주어진다.
테스트 케이스의 첫째 줄에는 완료해야 하는 업무의 수 N이 주어진다.
그 다음 N개의 줄에는 1부터 N까지의 업무번호 순으로 업무의 정보가 주어진다.
각 줄에는 업무 소요시간, 미리 완료해야 하는 업무들의 개수 M이 주어지고, 미리 완료해야 하는 업무 번호 M개가 공백으로 구분되어 나열된다.
미리 완료해야 하는 업무번호는 정렬되어 있지 않음에 유의하라.

출력
테스트 케이스 T에 대한 결과는 “#T”을찍고, 한 칸 띄고, 정답을 출력한다. (T는 테스트케이스의 번호를 의미하며 1부터 시작한다. )
정답은 모든 업무를 완료하기 위해 필요한 최소 소요시간이다. (모든 업무를 완료할수 없는 경우 -1을 출력한다.)
"""
import sys
sys.stdin = open("../test.txt", "r")
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = [-1 for _ in range(N+1)]
    adjList = [[] for _ in range(N+1)]
    inOrder = [-1 for _ in range(N+1)]
    for n in range(1, N+1):
        arr = list(map(int, input().split()))
        weights[n] = arr[0]
        if arr[1] == 0:
            inOrder[n] = 0
            continue
        inOrder[n] = arr[1]
        for adjNode in arr[2:]:
            adjList[adjNode].append(n)

    result = float('inf')
    for coco in range(1, N+1):
        temp = weights[coco]
        weights[coco] = temp // 2
        curTime = [0 for _ in range(N+1)]
        tempOrder = inOrder.copy()
        q = deque()
        for i in range(1, N + 1):
            if tempOrder[i] == 0:
                q.append((i, weights[i]))
                curTime[i] = weights[i]
        v = []

        while q:
            cur, weight = q.popleft()
            v.append(cur)
            for adjNode in adjList[cur]:
                tempOrder[adjNode] -= 1
                curTime[adjNode] = max(curTime[adjNode], curTime[cur] + weights[adjNode])
                if tempOrder[adjNode] == 0:
                    q.append((adjNode, weight + weights[adjNode]))

        if len(v) < N:
            result = -1
            break
        result = min(result, curTime)
        weights[coco] = temp
    print(f'#{tc} {result}')



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 업무 소요시간
#     weights = [-1 for _ in range(N+1)]
#     # 후행 업무 리스트 (인접리스트)
#     adjList = [[] for _ in range(N+1)]
#     # 미리 완료해야 하는 업무 수 (진입 차수)
#     inOrder = [-1 for _ in range(N+1)]
#     # 자료 정리
#     for n in range(1, N+1):
#         arr = list(map(int, input().split()))
#         weights[n] = arr[0]
#         if arr[1] == 0:
#             inOrder[n] = 0
#             continue
#         inOrder[n] = arr[1]
#         for adjNode in arr[2:]:
#             adjList[adjNode].append(n)
#
#     # 결과값은 최소값을 찾을 예정
#     result = float('inf')
#     # 코코가 작업할 업무를 완전탐색으로 할당
#     for coco in range(1, N+1):
#         # 가중치의 복구를 위해 temp 를 이용
#         temp = weights[coco]
#         # 코코가 작업할 업무 시간 절반
#         weights[coco] = temp // 2
#
#         # 해당 회차에서 소요시간을 저장할 변수
#         curTime = 0
#         # 진입 차수의 값을 초기화해주기 위한 변수
#         tempOrder = inOrder.copy()
#         # 큐 초기화 및 초기값 할당
#         q = deque()
#         for i in range(1, N + 1):
#             if tempOrder[i] == 0:
#                 q.append((i, weights[i]))
#         # 사이클 발생 여부를 확인하기 위한 방문기록
#         v = []
#
#         while q:
#             cur, weight = q.popleft()
#             v.append(cur)
#             curTime = max(curTime, weight)
#
#             # 현재 가중치 조건에서 최종 소요 시간 계산
#             for adjNode in adjList[cur]:
#                 # 인접 노드의 진입차수를 1 빼주고, 0이되면 큐에 추가
#                 tempOrder[adjNode] -= 1
#                 curTime = max(curTime, weight + weights[adjNode])
#                 if tempOrder[adjNode] == 0:
#                     q.append((adjNode, weight + weights[adjNode]))
#
#         # 반복문 이후 모든 노드를 방문하지 않았다면 사이클 발생, -1 출력
#         if len(v) < N:
#             result = -1
#             break
#         # 결과값은 모든 가중치 경우 중 최솟값
#         result = min(result, curTime)
#
#         # 가중치 복구
#         weights[coco] = temp
#     print(f'#{tc} {result}')

"""
5
34
444 0
36 0
63 0
4 0
470 0
205 0
843 0
601 0
511 0
700 0
181 0
838 0
975 0
52 0
760 0
499 0
861 0
963 0
898 0
373 0
949 0
91 0
967 0
243 0
438 0
96 0
638 0
421 0
715 0
232 0
366 0
678 0
578 0
836 0
5
684 0
838 0
846 0
869 0
334 0
25
731 0
257 0
451 0
603 0
482 0
153 0
499 0
308 0
916 0
250 0
349 0
895 0
982 0
166 0
11 0
905 0
216 0
552 0
572 0
873 0
222 0
422 0
635 0
808 0
849 0
1
317 0
21
877 0
352 0
489 0
919 0
413 0
309 0
877 0
47 0
648 0
839 0
763 0
563 0
780 0
112 0
511 0
730 0
510 0
223 0
181 0
805 0
387 0


#1 967
#2 846
#3 916
#4 158
#5 877
"""