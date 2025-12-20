#문제
#큐는 FIFO(FIRST In First Out)
#1. 현재 Queue의 가장 앞에 있는 문서의 중요도를 확인하자.
#2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면, 이 문서를 인쇄하지 않고
    #큐의 가장 뒤에 재배치한다. 그렇지 않다면 바로 인쇄를 한다.

#예 Queue에 4개의 문서(ABCD)가 있고, 중요도가 2143이라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A,B를 인쇄한다.
#우리가 할 일은 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아보자.
#예를 들어 C문서는 1번째로, A문서는 3번째로 인쇄된다.


#입력
#첫 줄에 테스트 케이스의 수 ->T
#테스트케이스의 첫 번째 줄에는 문서의 개수(N)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째로 놓여 있는지를 나타내는 정수 M

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())#테스트 케이스

for _ in range(T):#테스트 케이스만큼 반복하자.
    N,M = map(int,input().split())#N:문서의 개수, M:몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
    priorities = list(map(int,input().split()))#중요도를 먼저 리스트로 받기
    #큐를 만들 때(인덱스, 중요도)쌍으로 묶어서 넣기
    #enumerate : i는 인덱스, p는 쌍
    queue = deque([(i,p) for i,p in enumerate(priorities)])

    count=0 #몇 번째로 인쇄되는지 세는 변수

    while queue:
        current = queue.popleft()#일단 가장 왼쪽에 있는 원소를 꺼내긴 해야 함.
        #current는 현재 튜플로 꺼내진다. 예 (0,2)

        #current[1]의 값보다 나머지 queue의 값이 큰게 있을 때 -> append
        if any(current[1]<doc[1] for doc in queue):
            queue.append(current)
        else:
            count+=1

            if current[0] == M:
                print(count)
                break



