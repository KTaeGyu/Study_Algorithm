import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
print(arr)

