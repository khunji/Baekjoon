import sys #시간 초과 오류가 나서
input = sys.stdin.readline

N = int(input())
sang_card = set(map(int,input().split()))

M = int(input())
card = list(map(int,input().split()))


for i in card:
    if i in sang_card:
        print('1',end=' ')
    else:
        print('0',end=' ')