# 2491번 수열
'''
0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 
그 수열 안에서 연속해서 커지거나(같은 것 포함), 
혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 
그 길이를 출력하는 프로그램을 작성하라. 


9
1 2 2 4 4 5 7 7 2


8
'''

N = int(input())
arr = list(map(int, input().split()))
maxl = 1

# 계속 증가하는건 최대 몇개인지
cnt1 = 1
for i in range(1, N):
    if arr[i] >= arr[i - 1]:
        cnt1 += 1
        if cnt1 >= maxl:
            maxl = cnt1
    else:
        cnt1 = 1            # 초기화


# 계속 감소하는건 최대 몇개인지
cnt2 = 1
for i in range(1, N):
    if arr[i] <= arr[i - 1]:
        cnt2 += 1
        if cnt2 >= maxl:
            maxl = cnt2
    else:
        cnt2 = 1            # 초기화

print(maxl)

    