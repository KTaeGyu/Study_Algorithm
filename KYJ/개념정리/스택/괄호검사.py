# SWea 괄호검사

T = int(input())


def Test_str(string):
    stack = []
    top = -1
    # push
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == '{':
            stack.append('{')
        # pop
        elif string[i] == ')':
            if len(stack) != 0 and stack[top] == '(':
                stack.pop()
            else:
                return 0
        elif string[i] == '}':
            if len(stack) != 0 and stack[top] == '{':
                stack.pop()
            else:
                return 0
            
    if len(stack):
        return 0
    else:
        return 1
    

for tc in range(1, T + 1):
    my_str = input()     
    print(f'#{tc} {Test_str(my_str)}')
