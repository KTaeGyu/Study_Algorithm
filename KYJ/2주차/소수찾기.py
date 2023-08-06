# 1978번 소수 찾기

# 주어진 N개의 수에서 소수가 몇개인지 찾아서 출력하는 프로그램
# N은 100이하, N개의 수는 모두 1000이하의 자연수

def find_so(num): # 숫자를 받아서 소수면 1, 아니면 0을 출력
    find_list = []
    for i in range(1, 1001): # 1000 이하의 자연수니까 일일히 나눠서 찾아보자
        if num >= i: # 우선 작은 자연수로 나눠야함
            if num % i == 0:    # 나누어 떨어지면
                find_list.append(i) # 리스트에 넣어줌
    if len(find_list) == 2: # 리스트의 길이가 2라는건 1과 자기자신밖에 없을 때니까 소수
        return 1
    else:
        return 0
    
n = int(input())

nums_list = list(map(int,input().split()))
value_list = list(map(find_so,nums_list))
print(sum(value_list))