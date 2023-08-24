# 빙고
'''
사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

[입력]
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

[출력]
15

'''

nums = [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]

def bingo_count(arr):
    rere = 0        # 빙고의 갯수
    for row in arr:
        if row == [0, 0, 0, 0, 0]:      # 가로빙고
            rere += 1
    
    for i in range(5):
        cnt1 = 0 
        for j in range(5):
            if not arr[j][i]:           # 세로빙고
                cnt1 += 1
        if cnt1 == 5:
            rere += 1

    cnt2 = 0
    cnt3 = 0
    for i in range(5):
        if arr[i][i] == 0:              # ↘ 빙고
            cnt2 += 1
        if arr[i][4 - i] == 0:          # ↗ 빙고
            cnt3 += 1
    if cnt2 == 5:
        rere += 1
    if cnt3 == 5:
        rere += 1

    return rere

def makepan(arr, n):    # 각각의 숫자가 불렸을 때, 빙고판이 어떻게 바뀌는지 알려주는 함수
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0
    

def result():
    cnt = 0
    for i in range(5):
        for j in range(5):
            makepan(nums, ans[i][j])
            numsbingo = bingo_count(nums)
            cnt += 1
            if numsbingo >= 3:      # 동시에 될 때가 있어서 ==를 쓰면 틀림,,,
                return cnt

print(result())




    
# 하나하나 따지는게 쉽지않다