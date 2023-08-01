# ----------------------------------------------------------------------------------------------------------문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# ------------------------------------------------------------------------------------------------------예제 입력
# 첫째 줄에 단어의 개수 N이 주어진다. 
# (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 주어지는 문자열의 길이는 50을 넘지 않는다.
'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''

# ------------------------------------------------------------------------------------------------------예제 출력
# 조건에 따라 정렬하여 단어들을 출력한다.
'''
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''

# --------------------------------------------------------------------------------------------------알고리즘 분류
# 문자열
# 정렬

# ----------------------------------------------------------------------------------------------------------풀이
# 세트에 추가 후 삭제하는 방식보다 조건문을 사용해서 없는 단어만 추가하는 것이 더 효율적
wl = set()

for n in range(int(input())):
    w = input()
    if w not in wl:
        wl.add(w)

# 파이썬 내장함수 sorted를 사용하면 더 간단하게 표현할 수 있음. key는 정렬에 적용할 기준이 되는 함수.
wl = sorted(wl, key=lambda x: (len(x), x))

print(*wl, sep='\n')

# ------------------------------------------------------------------------------------------------------풀이 과정
''' 버블정렬로 단어를 길이별로 정렬했고, 3중 for 문을 사용하여 알파벳 순서로 정렬을 시도함, 시간 초과
import sys
input = sys.stdin.readline

wl = set()
for n in range(int(input())):
    wl.add(input())
wl = list(wl)

N = len(wl)
for i in range(N-1, 0, -1):
    for j in range(i):
        if len(wl[j]) > len(wl[j+1]):
            wl[j], wl[j+1] = wl[j+1], wl[j]
        elif len(wl[j]) == len(wl[j+1]):
            for k in range(len(wl[j])):
                if ord(wl[j][k]) > ord(wl[j+1][k]):
                    wl[j], wl[j+1] = wl[j+1], wl[j]

print(*wl)
'''