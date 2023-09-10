# 2630번 색종이만들기

'''
4등분씩해서 다 같은 색이면 stop, 아니면 또 4등분....
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

[입력]
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

[출력]
9
7
'''
'''
생각이 마땅히 안나서 상당히 무식하게 풀었다..

남들 코드를 구경해보니까
함수의 input을 자르는 위치의 좌표, 각각 위치의 길이를 매개변수로 놓은 듯..
그러고 나서 각각의 위치의 색 == 처음 점의 색인지를 확인해서 재귀를 돌려줌
'''


N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]
mid = N // 2
is_True = True
cnt1 = 0
cnt0 = 0

def square(arr):    # 4등분 한번씩 해서 확인하는 함수
    global cnt1
    global cnt0
    if len(arr) == 1:
        if 1 in arr:
            cnt1 += 1
        else:
            cnt0 += 1
        return 
    
    
    # 잘라보기
    mid = len(arr) // 2
    A, B, C, D = [], [], [], []
    for i in range(mid):
        A.append(arr[i][:mid])
        B.append(arr[i][mid:])
    for j in range(mid,len(arr)):
        C.append(arr[j][:mid])
        D.append(arr[j][mid:])

    # 확인하기
    acnt, bcnt, ccnt, dcnt = 0, 0, 0, 0
    for k in range(mid):
        acnt += sum(A[k])
        bcnt += sum(B[k])
        ccnt += sum(C[k])
        dcnt += sum(D[k])
    # 다 1일경우
    p = len(arr) ** 2 // 4
    if acnt == p:
        cnt1 += 1
    elif acnt == 0:
        cnt0 += 1
    else:
        square(A)
    if bcnt == p:
        cnt1 += 1
    elif bcnt == 0:
        cnt0 += 1
    else:
        square(B)
    if ccnt == p:
        cnt1 += 1
    elif ccnt == 0:
        cnt0 += 1
    else:
        square(C)
    if dcnt == p:
        cnt1 += 1
    elif dcnt == 0:
        cnt0 += 1
    else:
        square(D)

sums = 0
for i in range(N):
    sums += sum(MAP[i])
if sums == 0:
    cnt0 += 1
elif sums == N * N:
    cnt1 += 1
else:
    square(MAP)       
print(cnt0)
print(cnt1)