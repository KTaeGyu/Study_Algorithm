# 백준 1092번 배
'''
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다.
모든 화물은 박스에 안에 넣어져 있다. 
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 
모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 
이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 
둘째 줄에는 각 크레인의 무게 제한이 주어진다.
셋째 줄에는 박스의 수 M이 주어진다.
넷째 줄에는 각 박스의 무게가 주어진다.

3
6 8 9
5
2 5 2 4 7

[출력]
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다.
만약 모든 박스를 배로 옮길 수 없다면 -1을 출력한다.

2


그리디, 정렬
'''

import sys
input = sys.stdin.readline

N = int(input())
crains = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

if crains[0] < boxes[0]:
    print(-1)
    exit()

cnt = 0
while boxes:
    for crain in crains:
        for box in boxes:
            # 박스 큰거부터 보면서 된다면,
            if crain >= box:
                boxes.remove(box)
                break
    cnt += 1

print(cnt)


'''
이 방법이 생각이 나긴했는데 
당연히 시간초과일거같아서 안해봤다..
구글링하니까 다 이렇게 풀고 pypy로 돌리더라

일단 쉬운방법으로 해보고 안되면 다른 방법 찾아보자
'''














## 두번째 시도

# def find(crain, box):
#     if crain[0] < box[0]:
#         return -1
    
#     cnt = 1
#     i = 0
#     j = 0
#     while box:
#         if crain[i] >= box[j]:
#             box.pop(j)
#             i += 1
#         else:
#             j += 1
        
#         if i == N:
#             cnt += 1
#             i = 0
        
#         if j == M:
#             cnt += 1
#             i = 0
#             j = 0
#     return cnt

# result = find(crains, boxes)
# print(result)







# 첫시도
'''
문제를 덜 생각해씀
4
4 3 2 1
8
4 4 3 3 2 2 1 1 
이런 경우에는 각각 자기꺼 한개씩 들면 두번만에 끝나는디
'''
# N = int(input())
# crains = list(map(int,input().split()))
# M = int(input())
# boxes = list(map(int,input().split()))

# crains.sort(reverse=True)
# boxes.sort(reverse=True)
# cnt = 0
# print(crains, boxes)

# # 횟수를 찾아주는 함수
# def moving(crain, box):
#     global cnt
#     print(cnt, box)
#     boxlen = len(box)

#     for i in range(N):
#         if i >= boxlen:
#             if boxlen:
#                 cnt += 1
#                 return
#             else:
#                 return
#         if crain[i] < box[i]:    # 만약 중간에 걸리면, 되는데 까지만 싣고, 뒤에는 다시
#             cnt += 1
#             return moving(crain, box[i:])
#     else:   # 한번에 크레인이 다 적재 가능하면
#         cnt += 1
#         boxnum = len(box)
#         if boxnum <= N:
#             cnt += 1
#             return 
#         elif (boxnum - N) % N:
#             cnt += ((boxnum - N) // N) + 1
#             return
#         else:
#             cnt += ((M - N) // N)
#             return

# if crains[0] < boxes[0]:    # 만약 크레인의 최대값이 박스의 최대값보다 작다면
#     print(-1)
# else:
#     moving(crains, boxes)
#     print(cnt)   