# 2605번 줄세우기
'''
[입력]
5
0 1 1 3 2

[출력]
4 2 5 3 1

'''
N = int(input())
nums = list(map(int, input().split()))
student = []
for i in range(N):
    student.insert(i - nums[i], i + 1)      
print(*student)