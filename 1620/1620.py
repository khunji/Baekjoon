#문제
#첫째 줄 : 포켓몬의 개수 : N, 내가 맞춰야 하는 문제의 개수 : M
#둘째 줄 : N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어온다.
# 포켓몬의 이름은 영어로만 이루어져 있고, 첫글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있다. 일부 포켓몬은 마지막 문자만 대문자일 수도 있다.
#그 다음 줄부터 M개의 줄에 내가 맞춰야 하는 문제가 입력으로 들어온다. 
#알파벳-->번호/ 번호-->알파벳

import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())#N:포켓몬 개수, M : 맞춰야 하는 문제의 개수
pocketmon={}#딕셔너리 생성

for i in range(1,N+1):
    name = input().strip()

    #딕셔너리 양방향 저장
    pocketmon[i] = name
    pocketmon[name] = i

for _ in range(M):
    problem = input().strip()

    if problem.isdigit():#입력한 문자열이 25와 같이 숫자로 변환가능하면?
        print(pocketmon[int(problem)])
    else:
        print(pocketmon[problem])




