import sys
sys.stdin = open("../test.txt", "r")

N = int(input())
initial_state = list(map(int, input()))
final_state = list(map(int, input()))


def solve(state, cnt):
    for i in range(1, N):
        if state[i - 1] != final_state[i - 1]:
            cnt += 1
            state[i - 1] = (state[i - 1] + 1) % 2
            state[i] = (state[i] + 1) % 2
            if i == N - 1:
                continue
            state[i + 1] = (state[i + 1] + 1) % 2
    if state[N - 1] == final_state[N - 1]:
        print(cnt)
        return 0
    return 1


state1 = initial_state[:]
state2 = initial_state[:]
state2[0] = (state2[0] + 1) % 2
state2[1] = (state2[1] + 1) % 2

if solve(state1, 0):
    if solve(state2, 1):
        print(-1)
