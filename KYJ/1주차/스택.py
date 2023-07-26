# 10828번 스택

import sys

n = int(input())

# 스택은 위에서 부터 쌓음


stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    fun = command[0]
    if fun == 'push':
        stack.append(command[1]) # 새로 넣는게 뒤에 들어가니까
    if fun == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1)) # 뺄 때 뒤에서부터 빼야댐
    if fun == 'size':
        print(len(stack))
    if fun == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if fun == 'top':
        if len(stack) == 0:
            print(-1) # 맨 위에 있는것도 뒤에꺼
        else:
            print(stack[-1])