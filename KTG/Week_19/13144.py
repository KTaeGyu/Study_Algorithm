"""
문제
길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)
두 번째 줄에는 수열을 나타내는 N개의 정수가 주어진다.
수열에 나타나는 수는 모두 1 이상 100,000 이하이다.

출력
조건을 만족하는 경우의 수를 출력한다.

예제 입력 1            예제 출력 1
5                     15
1 2 3 4 5

예제 입력 2            예제 출력 2
5                     12
1 2 3 1 2

예제 입력 3            예제 출력 3
5                     5
1 1 1 1 1
"""
import sys
sys.stdin = open('../test.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

cnt = 0
start, end = 0, 0
tmep = [0] * 100001

while start < N and end < N:
    if not tmep[arr[end]]:
        tmep[arr[end]] = 1
        end += 1
        cnt += (end - start)
    else:
        tmep[arr[start]] = 0
        start += 1

print(cnt)
