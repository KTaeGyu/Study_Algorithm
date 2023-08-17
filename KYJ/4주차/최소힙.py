# 1927번 최소 힙
'''
널리 잘 알려진 자료구조 중 최소 힙이 있다. 
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
x는 2^31보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.

입력에서 0이 주어진 횟수만큼 답을 출력한다. 
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다

[input]
9
0
12345678
1
2
0
0
0
0
32

[output]
0
1
2
12345678
0

'''






from queue import PriorityQueue
import sys
input = sys.stdin.readline  # 이거 넣으니까 시간초과 안남

q = PriorityQueue()

for _ in range(int(input())):
    num = int(input())
    if num:
        q.put(num)
    elif q.empty():
        print(0)
    else:
        print(q.get())















# # 힙사용, 시간초과 남 

import heapq

hq = []

for tc in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(hq, num)
    else:
        try:
            print(heapq.heappop(hq))
        except:
            print(0)










# arr = []
# for tc in range(int(input())):
#     num = int(input())
   
#     if num:
#         arr.append(num)
#     elif num == 0 and arr:
#         print(min(arr))
#         arr.remove(min(arr))
#     else:
#         print(0)

# # 당연히 시간초과


