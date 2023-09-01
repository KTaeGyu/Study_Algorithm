# 구간 합 구하기4

'''
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

[입력]
5 3
5 4 3 2 1
1 3
2 4
5 5

[출력]
12
9
1
'''

# M값의 범위가 꽤 커서 readline으로 하는게 의미가 있어보임
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sumarr = [0 for _ in range(N)]
sumarr[0] = arr[0]
for i in range(1, N):
    sumarr[i] = sumarr[i - 1] + arr[i]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(sumarr[b - 1] - sumarr[a - 1] + arr[a - 1])