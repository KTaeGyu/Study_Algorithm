# 2805 나무자르기

# # Try1(실패!)

# import sys
# input = sys.stdin.readline
#
# # 입력받기
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# # 정렬
# arr.sort(reverse=True)
#
# # 변수선언
# sumTree = 0
# checkhigh = 0
# checkpoint = 0
# ans = 0
# newsumTree = 0
#
# # 자른 나무의 합이 M(잘라야 하는길이)보다 클때까지
# while sumTree < M:
#     for i in range(1,N):
#         # 자른 길이는 긴거에서 그다음 긴거까지
#         cutTree = arr[i-1] - arr[i]
#         # i가 증가함에 따라 자르는 나무 갯수 증가
#         sumTree += cutTree*i
#         # 딱 맞을때
#         if sumTree == M:
#             ans = arr[i]
#             # 뒤에서 쓸 것
#             newsumTree = M
#             break
#         # 더 많이 잘랐을 때
#         elif sumTree > M:
#             checkhigh = arr[i-1]
#             checkpoint = i
#             newsumTree = sumTree - cutTree*i
#             break
#     break
#
# # 더 많이 잘랐을 때 한번 더 계산
# while newsumTree < M:
#     for i in range(1,M):
#         newcut = checkpoint*i
#         newsumTree += newcut
#         if newsumTree > M:
#             ans = checkhigh-(i+1)
#             break
#
# print(ans)
# # 중복된 나무 길이가 있으면 해결 불가



# Try2
import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))
# arr.sort()
# 이거때문인가


# 나무 자르기
# start, end = 1, arr[-1]
start, end = 1, max(arr)


while start <=end:
    sumtree = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            sumtree += i-mid

    # if sumtree <= M: // 이건왜안될까
    if sumtree < M:
        end = mid -1
    else:
        start = mid + 1
print(end)

#시간초과

