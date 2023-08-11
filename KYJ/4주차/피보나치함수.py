# 1003번 피보나치 함수

'''
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. 

N이 주어졌을 때, fibonacci(N)을 호출했을 때, 
0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.


[input]
3
0
1
3

[output]
1 0
0 1
1 2

'''

'''
DP 방식을 써보자
근데 각각 0호출 횟수와 1호출 횟수도 저장을 해야댐
DP[0] = [0, [1, 0]]이런식으로 저장을 해야하나 그럼..

끼리끼리 더하는 방법
1. list comprehension: [lst1[i] + lst2[i] for i in range(len(lst1))]
2. zip을 이용하기: [x + y for x, y in zip(lst1, lst2)]
'''

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    
    def fibo(n):
        DP = [[0, [0, 0]]] * (n + 1)     # 결과를 저장할 DP리스트 생성
        DP[0] = [0, [1, 0]]
        if n > 0:
            DP[1] = [1, [0, 1]]

            for i in range(2, n + 1):
                DP[i] = [DP[i-1][0] + DP[i-2][0], [x + y for x, y in zip(DP[i - 1][1], DP[i - 2][1])]]
            
        return DP[n][1]
        
    print(*fibo(n))
