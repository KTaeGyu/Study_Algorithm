# 10845번 큐

import sys

N = int(sys.stdin.readline())
que = []

for i in range(N):
    command = sys.stdin.readline().split()
    fun = command[0]
    if fun == 'push':
        que.append(command[1])
    if fun == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    if fun == 'size':
        print(len(que))
    if fun == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if fun == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    if fun == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])