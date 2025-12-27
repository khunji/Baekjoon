#비어 있는 공집합 S
#add x : S에 x를 추가한다. S에 x가 이미 있는 경우 연산 무시
#remove x : S에서 x를 제거한다. S에 x가 없는 경우에는 연산을 무시
#check x : S에 x가 있으면 1을, 없으면 0을 출력
#toggle x : S에 x가 있으면 x를 제거하고, 없으면 x를 추가
#all : S를 {1,2,3,...,20}으로 바꾼다.
#empty : S를 공집합으로 바꾼다.

import sys
input=sys.stdin.readline
S = set()

M = int(input())#수행해야 하는 연산의 수

for _ in range(M):
    cmd = sys.stdin.readline().strip().split()#명령

    if len(cmd)==1:
        if cmd[0] == "all":
            S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        else:
            S = set()
    else:#S의 원소의 개수가 1이 아님
        command = cmd[0]
        num = int(cmd[1])

        if command=="add":
            if num in S:
                pass
            else:
                S.add(num)
    
        if command == "remove":
            if num not in S:
                pass
            else:
                S.remove(num)
    
        if command == "check":
            if num in S:
                print("1")
            else:
                print("0")
        if command == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)
