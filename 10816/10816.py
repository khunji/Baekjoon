#숫자카드2

#문제
#숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
#정수 M개가 주어졌을 때, 이 수가 적혀 있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 상근이가 가지고 있는 숫자 카드이 개수 N이 주어진다.
#둘째 줄에는 숫자 카드에 적혀 있는 정수가 주어진다. 


#출력
#첫째 줄에 입력으로 주어진 M개의 수에 대해서
#각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())#상근이가 가지고 있는 숫자 카드의 개수
card=list(map(int,input().split()))


M = int(input())#상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수
num=list(map(int,input().split()))


cnt = Counter(card)
result=[]#몇 개 있는지 저장할 리스트

for i in num:#num에 들어있는 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수를 하나씩 뽑고
    result.append(cnt[i])
print(*result)

