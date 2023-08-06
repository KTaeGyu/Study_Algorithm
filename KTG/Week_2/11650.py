# ----------------------------------------------------------------------------------------------------------문제
# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# ------------------------------------------------------------------------------------------------------예제 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
"""
5
3 4
1 1
1 -1
2 2
3 3
"""
# ------------------------------------------------------------------------------------------------------예제 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""
1 -1
1 1
2 2
3 3
3 4
"""
# --------------------------------------------------------------------------------------------------알고리즘 분류
<<<<<<< HEAD
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

=======
# 정렬
>>>>>>> b4fca9ba19c9bd6543d5e3030b19b01de5398286

def solution(arr, queries):
    answer = []
    for s, e, k in queries:

        nl = [arr[i] for i in range(s, e+1) if arr[i] > k]

        if nl == []:
            answer.append(-1)
        elif nl != []:
            answer.append(min(nl))

    return answer


print(solution(arr, queries))

# ----------------------------------------------------------------------------------------------------------풀이
cord = []
for T in range(int(input())):
    x, y = map(int, input().split())
    cord.append((x, y))

<<<<<<< HEAD
# arr = [0, 1, 1, 1, 0]

# # def top(arr):
# #     if arr != []:
# #         a = arr.pop()
# #         arr.append(a)
# #         return a


# def solution(arr):
#     i = 0
#     stk = []
#     while i < len(arr):
#         if stk == []:
#             stk.append(arr[i])
#             i += 1
#         else:
#             if stk[len(stk)-1] == arr[i]:
#                 stk.pop()
#                 i += 1
#             else:
#                 stk.append(arr[i])
#                 i += 1
        
#     return stk


# print(solution(arr))

=======
cord = sorted(cord, key=lambda x: (x[0], x[1]))
>>>>>>> b4fca9ba19c9bd6543d5e3030b19b01de5398286

for i in cord:
    print(*i)
 
# ------------------------------------------------------------------------------------------------------풀이 과정
# 카운팅 정렬을 사용해서도 해보고 싶음 -> 음수때문에 실패함
# N = int(input())
# cord = []
# for n in range(N):
#     x, y = map(int, input().split())
#     cord.append((x, y))

# max_x = 0
# for i in cord:
#     if max_x < i[0]:
#         max_x = i[0]

# arr_x = [0]*(max_x + 1)

# for i in cord:
#     arr_x[i[0]] += 1

# for i in range(1, max_x + 1):
#     arr_x[i] += arr_x[i-1]

# nl = [0]*N
# nl_x = [[] for _ in range(max_x + 1)]
# for i in range(N-1, -1, -1):
#     nl_x[cord[i][0]].append(cord[i])
    
#     max_y = 0
#     for j in range(len(nl_x[i])):
#         if max_y < nl_x[i][j][1]:
#             max_y = nl_x[i][j][1]
    
#     arr_y = [0](max_y + 1)

#     for j in nl_x[i]:
#         arr_y[j[1]]