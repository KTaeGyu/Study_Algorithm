# 10866번 덱

import sys

N = int(input())

deque = []

for i in range(N):
    command = sys.stdin.readline().split()
    
    # push_front
    if command[0] == 'push_front':
        deque.insert(0,command[1])
    # push_back
    if command[0] == 'push_back':
        deque.append(command[1])
    # pop_front
    if command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            a = deque.pop(0)
            print(a)
    if command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            a = deque.pop(len(deque) - 1)
            print(a)
    if command[0] == 'size':
        print(len(deque))
    if command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])