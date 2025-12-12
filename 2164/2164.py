#1번카드가 제일 위에, N번 카드가 제일 아래, 카드가 한 장 남을 때까지 반복하게 된다.
#우선 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

#예를 들어 N=4인 경우를 생각해보자. 처음:1234 -> 1을 버리면 234 -> 여기서 2를 제일 아래로 옮기면 342
#3을 버리면 42, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
#제일 마지막에 남게 되는 카드를 구해보자.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #첫째 줄에 정수(N장의 카드(1부터 N까지 번호 있음.))

queue = deque()
for i in range(1,N+1):
    queue.append(i)

while True:
    if len(queue)==1:
        print(queue[0])
        break
    queue.popleft()
    temp = queue[0]
    queue.popleft()
    queue.append(temp)
        





