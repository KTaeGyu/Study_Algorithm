"""
1107: 리모콘
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다.
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다.
어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

수빈이가 지금 보고 있는 채널은 100번이다.

첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

# 그냥 완전탐색, 탐색범위는 2배로
N = int(input())
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []
difference = abs(N - 100)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
    else:
        difference = min(difference, abs(int(num)-N) + len(num))
print(difference)

""" 
# 입력할 수 있는 숫자중 가장 가까운 큰/작은 숫자를 찾는 방법(숫자를 1씩 더하고 빼서 구함)
# 시간초과
upper_result = N
upper_cnt = 0
while True:
    cnt = 0
    flag = 0
    for i in upper_result:
        cnt += 1
        if i not in rc:
            flag = 1
            break
    else:
        break
    upper_result = int(upper_result)
    upper_result += 1
    upper_result = str(upper_result)
    upper_cnt += 1
    if flag: continue
upper_cnt += cnt

lower_result = N
lower_cnt = 0
while True:
    cnt = 0
    flag = 0
    for i in lower_result:
        cnt += 1
        if i not in rc:
            flag = 1
            break
    else:
        break
    lower_result = int(lower_result)
    lower_result -= 1
    lower_result = str(lower_result)
    lower_cnt += 1
    if flag: continue
lower_cnt += cnt

print(min(upper_cnt, lower_cnt))
"""
"""
5457
3
6 7 8

6
"""