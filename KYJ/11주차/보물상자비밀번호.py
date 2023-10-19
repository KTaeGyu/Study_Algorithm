# SWEA 보물상자 비밀번호

'''
돌려서 나온 수 중 K번째로 큰 수를 10진수로 출력
'''
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int,input().split())
    
    # 한면에 들어가는 숫자의 갯수
    m = N // 4

    # 가능한 모든 숫자를 담을 lst
    nums = []

    # 가공안된 input
    lst = input()
    # 회전하는거 처리 -> 그냥 처음부터 이어붙여준다
    lst = lst + lst

    # 가능한건 N개
    for i in range(N):
        number = lst[i: i + m]
        nums.append(number)


    # 중복 제거를 위해 set로 바꿔준다
    nums = set(nums)

    # 결과값을 담을 result
    result = []
    for num in nums:
        num = int(num, 16)
        result.append(num)

    # K번째 수 찾기위해 내림차순 정렬
    result.sort(reverse=True)

    print(f'#{tc} {result[K - 1]}')