from collections import deque
from typing import Any
import sys

class Stack:

    def __init__(self)->None:
        '''스택 초기화'''
        self.__stk = deque()

    def push(self, value:Any)->None:
        '''스택에 value를 푸시'''
        self.__stk.append(value)
    
    def pop(self)->Any:
        '''스택에서 value를 팝'''
        if len(self.__stk) == 0:
            return -1
        return self.__stk.pop()
    
    def size(self)->int:
        '''스택에 들어 있는 정수의 개수'''
        return len(self.__stk)
    
    def is_empty(self)->bool:
        '''스택이 비어있으면 1, 아니면 0'''
        return 1 if len(self.__stk) ==0 else 0
    
    def top(self)->Any:
        '''스택의 가장 위에 있는 정수'''
        if len(self.__stk) == 0:
            return -1
        return self.__stk[-1]



N = int(sys.stdin.readline())    #명령 수
stack = Stack()     #스택 객체 생성

for _ in range(N):  #N번 반복
    cmd = sys.stdin.readline().split()   #["push", "3"] 리스트화

    if cmd[0] == "push":
        value = cmd[1]
        stack.push(value)
    
    elif cmd[0] ==  "pop":
        print(stack.pop())
    
    elif cmd[0] == "size":
        print(stack.size())
    
    elif cmd[0] == "empty":
        print(stack.is_empty())
    
    else:
        print(stack.top())
    


