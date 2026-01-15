#문제
#총 N개의 문자열로 이루어진 집합 S가 주어진다.
#입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인가?


#입력
#첫째 줄에 문자열의 개수 N과 M이 주어진다.
#다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
#M개의 줄에는 검사해야 하는 문자열들이 주어진다.
#입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500넘지 x
#집합 s에 같은 문자열이 여러 번 주어지는 경우x

#출력
#첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력해라.

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S=[]#집합:S
sum=0

for i in range(N):
    a = input().rstrip()
    S.append(a)

for i in range(M):
    b = input().rstrip()
    if b in S:
        sum+=1
print(sum)

