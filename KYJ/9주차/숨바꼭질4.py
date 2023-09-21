# 숨바꼭질4
'''
+1, -1, *2의 위치로 이동
이동할 때마다 1초
가장 빠른길, 그때의 경로도 같이
'''
from collections import deque

N, K = map(int,input().split())

def shushuk(start):
    q = deque([(start, 0, str(start))]) # 위치, 시간, 경로
    
    while q
