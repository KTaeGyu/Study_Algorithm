# 스위치 켜고 끄기
'''
남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 
가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다. 
학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 
스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

[입력]
8
0 1 0 1 0 0 0 1
2
1 3
2 3

[출력]
1 0 0 0 1 1 0 1

출력을 끝까지 읽자...
스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
'''

T = int(input())
switch = list(map(int,input().split()))
N = int(input())

def boy(num, switch):   # num은 받은 수
    k = num
    while k <= T:
        if switch[k - 1]:
            switch[k - 1] = 0
        else:
            switch[k - 1] = 1
        k += num        # num += num하면 틀림

def girl(num, switch):
    # 우선 현재위치 바꿔주고
    if switch[num - 1]:
        switch[num - 1] = 0
    else:
        switch[num - 1] = 1
    
    i = 1
    while 1 <= num - i < T + 1 and 0 <= num - 1 + i < T:    # 구간안에 있을 때만
        if switch[num -1 - i] == switch[num - 1 + i]:
            if switch[num - 1 - i]:
                switch[num - 1 - i] = 0
                switch[num - 1 + i] = 0
            else:
                switch[num - 1 - i] = 1
                switch[num - 1 + i] = 1
            i += 1    
        else:
            i = 1
            return
        
        

for _ in range(N):
    gen, num = map(int,input().split())
    if gen == 1:
        boy(num, switch)
    else:
        girl(num,switch)
    # print(switch)

if T > 20:
    i = 0
    cnt = 0
    while i < T:
        print(switch[i], end = ' ')
        i += 1
        cnt += 1
        if cnt == 20:
            print()
            cnt = 0
        
else:
    print(*switch)