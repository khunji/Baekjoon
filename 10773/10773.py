#재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 한다.
#재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.

#가장 최근에 재민이가 쓴 수를 지운다.--> 스택의 pop()

import sys
input = sys.stdin.readline

K = int(input())

stack=[]#여기에 입력한 num을 판단하고 저장할 예정
stack_sum = 0

for _ in range(K):

    num = int(input())

    if num == 0:
        if stack: #스택이 비어있는가?
            stack.pop()
    else:
        stack.append(num)

for i in stack:
    stack_sum+=i

print(stack_sum)




