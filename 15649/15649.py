#문제
#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

#출력
#한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력한다.
#수열은 사전 순으로 증가하는 순서로 출력해야 한다. 

import sys
input=sys.stdin.readline

def dfs():
    #[종료 조건]
    if len(result)==M:
        print(*result)
        return
    
    for i in range(1,N+1):
        #이미 방문한 숫자(visited_check[i] == True라면 건너뛰기)
        if visited_check[i] == True:
            continue

        visited_check[i] = True
        result.append(i)

        dfs()#다음 단계

        result.pop()
        visited_check[i] = False




    
N,M = map(int,input().split()) #1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

visited_check=[False]*(N+1)#인덱스 1~N을 쓰기 위해 크기 N+1로 생성
result=[]
dfs()