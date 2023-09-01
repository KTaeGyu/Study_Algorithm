# # 시간 초과
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# for _ in range(M):
#     A, B = map(int, input().split())
#     print(sum(arr[A-1:B]))


#누적합?
def prefix_sum(N):
    prefixsum = [0] * N
    prefixsum[0] = arr[0]
    for i in range(1, N):
        prefixsum[i] = prefixsum[i-1] + arr[i]
    return prefixsum

N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefixsum = prefix_sum(N)

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# S = prefix_sum(N)
# for _ in range(M):
#     A, B = map(int, input().split())
#     partsum = prefixsum[B] - prefixsum[i-1]