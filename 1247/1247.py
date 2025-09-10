import sys

input = sys.stdin.readline #빠른 입출력 속도 때문에 


for i in range(3):  #3개의 테스트 케이스
    N = int(input())
    total=0
    for j in range(N):
        total+=int(input())

    if total>0:
        print("+")
    elif total<0:
        print('-')
    else:
        print("0")
