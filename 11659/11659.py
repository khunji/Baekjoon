#문제
#수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하자.

#입력
#첫째 줄에 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다.
#수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

#출력
#총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

import sys
input = sys.stdin.readline
N,M = map(int,input().split())#N(개수), M(합을 구해야 하는 횟수)
num = list(map(int,input().split()))

#누적합이라는 개념을 이용해서 해결하기
#i부터 j까지의 인덱스의 합 = 1부터 j까지의 합 - 1부터 i-1까지의 합

prefix_sum = [0]*(N+1)
prefix_sum[1] = num[0]

for i in range(2,N+1):
    prefix_sum[i] = prefix_sum[i-1]+num[i-1]
for _ in range(M):
    a,b = map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])









