'''
A형 기출 > 재귀

[입력]
5
4
1 2 3 4
5
3 10 1 2 5
7
12 48 28 21 67 75 85
8
245 108 162 400 274 358 366 166
10
866 919 840 944 761 895 701 912 848 799

[출력]
#1 20 
#2 100 
#3 16057 
#4 561630 
#5 6455522
'''


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    def pang(score, idx, arr):  # 누적 점수, 지금 터트릴 인덱스, 현재의 남은 풍선
        if len(arr) == 3:
            if idx == 0:
                a.append(score + arr[1] + max(arr[1], arr[2]) * 2)
                return
            elif idx == 1:
                a.append(score + arr[0] * arr[2] + max(arr[0], arr[2]) * 2)
                return
            else:
                a.append(score + arr[1] + max(arr[0], arr[1]) * 2)
                return
        elif len(arr) == 2:
            a.append(score + max(arr[0],arr[1]) * 2)
        elif len(arr) == 1:
            a.append(score + arr[0])
        else:
            n_arr = arr[:idx] + arr[idx + 1:]
            for i in range(len(n_arr)):
                if idx == 0:
                    pang(score + arr[idx + 1], i, n_arr)
                elif idx == len(arr) - 1:
                    pang(score + arr[idx - 1], i, n_arr)
                else:
                    pang(score + arr[idx + 1] * arr[idx - 1], i, n_arr)

    result = []
    for i in range(N):
        a = []
        pang(0, i, arr)
        result.append(max(a))


    print(f'#{tc} {max(result)}')
























# N = int(input())
# arr = list(map(int,input().split()))
# result = 0

# while True:
#     if len(arr) == 1:
#         result += arr[0]
#         break

#     mult = [0 for _ in range(len(arr))]
#     for i in range(len(arr)):
#         if i == 0:
#             mult[i] = arr[i + 1]
#         elif i == len(arr) - 1:
#             mult[i] = arr[i - 1]
#         else:
#             mult[i] = arr[i - 1] * arr[i + 1]
    
#     maxv = 0
#     for k in range(len(arr)):
#         if mult[k] >= maxv:
#             maxv = mult[k]
#             delk = k
    
#     result += maxv
#     arr.pop(delk)

# print(result)

