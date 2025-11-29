from collections import deque
from typing import Any
import sys

class Deque:

    def __init__(self)->None:
        '''덱 초기화'''
        self.__deque = deque()
    
    def push_front(self, value:Any)->None:
        '''정수 x를 덱의 앞에 넣는다.'''
        self.__deque.appendleft(value)
    
    def push_back(self,value:Any)->None:
        '''정수 x를 덱의 뒤에 넣는다.'''
        self.__deque.append(value)
    
    def pop_front(self)->int:
        '''덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.'''
        if(len(self.__deque)==0):
            print(-1)
            return
        print(self.__deque.popleft())
    
    def pop_back(self)->int:
        '''덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.'''
        if(len(self.__deque)==0):
            print(-1)
            return
        print(self.__deque.pop())
    
    def size(self)->int:
        '''덱에 들어있는 정수의 개수'''
        print(len(self.__deque))
    
    def empty(self)->bool:
        '''덱이 비어있으면 1을 아니면 0을 출력한다.'''
        print(1 if(len(self.__deque))==0 else 0)
    
    def front(self)->int:
        '''덱의 가장 앞에 있는 정수를 출력한다.'''
        if len(self.__deque)==0:
            print (-1)
            return
        print(self.__deque[0])
    
    def back(self)->int:
        '''덱의 가장 뒤에 있는 정수를 출력한다.'''
        if len(self.__deque)==0:
            print (-1)
            return
        print(self.__deque[-1])



N = int(sys.stdin.readline())

deque = Deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_back":
        x = cmd[1]
        deque.push_back(x)
    
    elif cmd[0] == "push_front":
        x = cmd[1]
        deque.push_front(x)

    elif cmd[0] == "pop_front":
        deque.pop_front()
    
    elif cmd[0] == "pop_back":
        deque.pop_back()

    elif cmd[0] == "size":
        deque.size()
    
    elif cmd[0] == "empty":
        deque.empty()

    elif cmd[0] == "front":
        deque.front()
    
    else:
        deque.back()

    

    



    

