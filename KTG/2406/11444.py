import sys
sys.stdin = open('./11444.txt', 'r')

N = int(input())
denominator = 1000000007

memo = {}


def fib(n):
    if memo.get(n) is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n

    if n % 2 == 0:
        memo[n // 2] = fib(n // 2) % denominator
        memo[n // 2 - 1] = fib(n // 2 - 1) % denominator
        return memo[n // 2] * (2 * memo[n // 2 - 1] + memo[n // 2])
    else:
        memo[n // 2] = fib(n // 2) % denominator
        memo[n // 2 + 1] = fib(n // 2 + 1) % denominator
        return memo[n // 2] ** 2 + memo[n // 2 + 1] ** 2


print(fib(N) % denominator)
